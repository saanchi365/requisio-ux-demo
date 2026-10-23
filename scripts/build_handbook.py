"""The page maker: builds the handbook pages from GitHub, before MkDocs turns them into the website.

How the handbook is organised (nothing here needs editing when you add work):
  1 · Feature          = issue made with the "1 · Feature" form, not under anything  -> its own page
  2 · Requirement      = placed under a feature                                      -> a box in the Requirements tab
  3 · Sub-requirement  = placed under a requirement (only for big ones)              -> a box inside that box
  Smaller points       = bullets in the issue's "Details" section
  Anything at the wrong level is listed under "Needs fixing" on the Requirements page.

It reads:
  - every issue (text, labels, sub-issues) and its columns on the project board
  - flowcharts/**.md   -> a flowchart belongs to the feature named in its "Feature" line, e.g. "(#5)"
  - wireframes/*       -> a picture belongs to the issue number its file name starts with, e.g. "7-form.svg"
and writes: docs/index.md, docs/requirements.md, docs/features/*.md and the menu in mkdocs.yml.

Runs on GitHub during every publish. Needs GH_TOKEN (and PROJECT_NUMBER for the board).
"""
import json
import os
import re
import shutil
import sys
import urllib.request
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REPO = os.environ.get("GITHUB_REPOSITORY", "saanchi365/requisio-ux-demo")
OWNER, NAME = REPO.split("/")
PROJECT = int(os.environ.get("PROJECT_NUMBER", "9"))
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
GH = f"https://github.com/{REPO}/issues/"
BOARD_URL = f"https://github.com/users/{OWNER}/projects/{PROJECT}"
IMAGE = (".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp")

sys.stdout.reconfigure(encoding="utf-8")


# ------------------------------------------------------------------ reading GitHub
def graphql(query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql", json.dumps({"query": query, "variables": variables}).encode(),
        {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req))


BOARD_PART = """
      projectItems(first: 10) { nodes { project { number }
        fieldValues(first: 30) { nodes {
          ... on ProjectV2ItemFieldSingleSelectValue { name field { ... on ProjectV2FieldCommon { name } } }
          ... on ProjectV2ItemFieldDateValue { date field { ... on ProjectV2FieldCommon { name } } }
          ... on ProjectV2ItemFieldTextValue { text field { ... on ProjectV2FieldCommon { name } } }
        } } } }"""
ISSUES = """
query($owner: String!, $name: String!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    issues(first: 50, after: $cursor, states: [OPEN, CLOSED], orderBy: {field: CREATED_AT, direction: ASC}) {
      pageInfo { hasNextPage endCursor }
      nodes {
        number title body state updatedAt
        labels(first: 10) { nodes { name } }
        assignees(first: 5) { nodes { login } }
        parent { number }
        subIssues(first: 50) { nodes { number } }
        BOARD
      }
    }
  }
}"""


def fetch_issues():
    """All issues. If the board can't be read with this permission, carry on without its columns."""
    with_board = True
    for attempt in (ISSUES.replace("BOARD", BOARD_PART), ISSUES.replace("BOARD", "")):
        issues, cursor, failed = [], None, False
        while True:
            data = graphql(attempt, {"owner": OWNER, "name": NAME, "cursor": cursor})
            if data.get("errors") and with_board:
                print("Note: couldn't read the project board, so board columns will be empty:",
                      data["errors"][0].get("message"))
                failed = True
                break
            if data.get("errors"):
                sys.exit(f"Couldn't read the issues: {data['errors']}")
            page = data["data"]["repository"]["issues"]
            issues += page["nodes"]
            if not page["pageInfo"]["hasNextPage"]:
                break
            cursor = page["pageInfo"]["endCursor"]
        if not failed:
            return issues, with_board
        with_board = False


STATUS = {"Done": "Done", "In Progress": "In progress", "Todo": "To do"}


def board_columns(issue):
    cols = {}
    for item in (issue.get("projectItems") or {}).get("nodes", []):
        if item["project"]["number"] != PROJECT:
            continue
        for v in item["fieldValues"]["nodes"]:
            if v and v.get("field"):
                cols[v["field"]["name"].strip()] = v.get("name") or v.get("date") or v.get("text")
    return cols


def sections(body):
    """'### Heading' blocks from an issue's text, as {heading: text}."""
    out, current = {}, None
    for line in (body or "").splitlines():
        if line.startswith("### "):
            current = line[4:].strip().lower()
            out[current] = []
        elif current:
            out[current].append(line)
    clean = {k: "\n".join(v).strip() for k, v in out.items()}
    return {k: v for k, v in clean.items() if v and v != "_No response_"}


def bullets(text):
    return [re.sub(r"^[-*]\s+(\[[ x]\]\s+)?", "", l).strip() for l in (text or "").splitlines()
            if re.match(r"^\s*[-*]\s+", l)]


def nice_date(d):
    if not d:
        return ""
    d = date.fromisoformat(d[:10])
    return f"{d.day} {d:%b %Y}"


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


raw, BOARD_READ = fetch_issues()
# Without permission for the board, GitHub quietly returns no board rows instead of an error.
if BOARD_READ and not any(board_columns(r) for r in raw):
    print("Note: the project board looks empty to the website, so it probably has no permission to read it. "
          "Add a HANDBOOK_TOKEN secret (see the handbook's setup notes).")
    BOARD_READ = False
I = {}
for r in raw:
    cols = board_columns(r)
    s = sections(r["body"])
    status = STATUS.get(cols.get("Status")) or ("Done" if r["state"] == "CLOSED" else "To do")
    I[r["number"]] = dict(
        n=r["number"], title=r["title"], labels={l["name"] for l in r["labels"]["nodes"]},
        parent=(r["parent"] or {}).get("number"), children=[c["number"] for c in r["subIssues"]["nodes"]],
        status=status, priority=cols.get("Priority", ""), start=cols.get("Start date"), target=cols.get("Target date"),
        comments=(cols.get("comments/ inputs") or "").strip(), assignees=[a["login"] for a in r["assignees"]["nodes"]],
        updated=r["updatedAt"], sections=s)


def root(n):
    while I[n]["parent"] and I[n]["parent"] in I:
        n = I[n]["parent"]
    return n


FEATURES = [i for i in I.values() if "feature" in i["labels"] and not i["parent"]]
for f in FEATURES:
    f["slug"] = slugify(f["title"])
    f["flows"], f["questions"], f["unconfirmed"], f["wireframes"] = [], bullets(f["sections"].get("open questions")), [], []
BY_N = {f["n"]: f for f in FEATURES}
ORPHANS = [i for i in I.values() if root(i["n"]) not in BY_N]


def tree(n):
    """Every issue below n, in order."""
    out = []
    for c in I[n]["children"]:
        if c in I:
            out.append(I[c])
            out += tree(c)
    return out


# ------------------------------------------------------------------ flowcharts and wireframes
def section_bullets(text, heading):
    m = re.search(rf"^## {heading}\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return [b for b in bullets(m.group(1))] if m else []


for path in sorted((ROOT / "flowcharts").rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    area = re.search(r"\|\s*\*\*(?:Feature|Area)\*\*\s*\|([^|\n]*)\|", text)
    diagram = re.search(r"```mermaid\s*\n(.*?)```", text, re.S)
    nums = [int(x) for x in re.findall(r"#(\d+)", area.group(1))] if area else []
    owners = {root(x) for x in nums if x in I} & set(BY_N)
    if len(owners) != 1 or not diagram:
        continue
    f = BY_N[owners.pop()]
    title = re.search(r"^# (.+)$", text, re.M)
    f["flows"].append(dict(title=title.group(1).strip() if title else path.stem, mermaid=diagram.group(1).rstrip(),
                           file=path.relative_to(ROOT).as_posix()))
    f["questions"] += [q for q in section_bullets(text, "Open questions") if q not in f["questions"]]
    f["unconfirmed"] += [q for q in section_bullets(text, "Assumptions") if q not in f["unconfirmed"]]

WIREFRAMES = {}
out_dir = DOCS / "wireframes"
shutil.rmtree(out_dir, ignore_errors=True)
for path in sorted((ROOT / "wireframes").glob("*")) if (ROOT / "wireframes").exists() else []:
    m = re.match(r"^(\d+)[-_ ]+(.*)$", path.name)
    if not m or not path.name.lower().endswith(IMAGE) or int(m.group(1)) not in I:
        continue
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(path, out_dir / path.name)
    n = int(m.group(1))
    label = re.sub(r"\.(excalidraw\.)?(svg|png|jpe?g|gif|webp)$", "", m.group(2), flags=re.I).replace("-", " ").replace("_", " ")
    WIREFRAMES.setdefault(n, []).append(dict(file=path.name, title=label.strip().capitalize()))
    if root(n) in BY_N:
        BY_N[root(n)]["wireframes"].append(n)


# ------------------------------------------------------------------ writing pages
PILL = {"Done": "done", "In progress": "progress", "To do": "todo"}
ICON = {"Done": ":material-check-circle:{ .st-done }", "In progress": ":material-progress-clock:{ .st-progress }",
        "To do": ":material-circle-outline:{ .st-todo }"}
pill = lambda s: f'<span class="pill pill--{PILL[s]}">{s}</span>'
DASH = '<span class="small">—</span>'
UPDATED = nice_date(max(i["updated"] for i in I.values())) if I else nice_date(datetime.now().isoformat())


def write(rel, text):
    path = DOCS / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.lstrip("\n"), encoding="utf-8", newline="\n")


def ind(text, n):
    return "\n".join((" " * n + l) if l.strip() else "" for l in text.split("\n"))


def who(i):
    return ", ".join(f"[@{a}](https://github.com/{a})" for a in i["assignees"]) or "Unassigned"


def wire_images(n, prefix="../"):
    return "\n\n".join(f"![{w['title']}]({prefix}wireframes/{w['file']}){{ .wireframe }}" for w in WIREFRAMES.get(n, []))


def issue_box(i, depth=0):
    s = i["sections"]
    parts = [s.get("requirement", "")]
    if s.get("done when"):
        parts.append("**Done when**\n\n" + s["done when"])
    if s.get("details"):
        parts.append("**Details**\n\n" + s["details"])
    facts = [pill(i["status"])] + [x for x in [i["priority"], who(i),
                                               " → ".join(filter(None, [nice_date(i["start"]), nice_date(i["target"])]))] if x]
    parts.append(" · ".join(facts))
    if i["comments"]:
        parts.append(f"**Comments / inputs:** {i['comments']}")
    if WIREFRAMES.get(i["n"]):
        parts.append(wire_images(i["n"]))
    parts.append(f"[Open #{i['n']} on GitHub]({GH}{i['n']})")
    parts += [issue_box(I[c], depth + 1) for c in i["children"] if c in I]
    kind = "Requirement" if depth == 0 else "Sub-requirement"
    title = f"{kind} #{i['n']} · {i['title']}".replace('"', "'")
    return f'??? issue "{title}"\n' + ind("\n\n".join(p for p in parts if p), 4)


def feature_page(f):
    s = f["sections"]
    tabs = []
    if f["wireframes"]:
        groups = []
        for n in dict.fromkeys(f["wireframes"]):
            groups.append(f"**#{n} {I[n]['title']}**\n\n{wire_images(n)}")
        tabs.append(("Wireframes", "\n\n".join(groups)))
    if f["flows"]:
        flows = []
        for fl in f["flows"]:
            head = f"**{fl['title']}**\n\n" if len(f["flows"]) > 1 else ""
            flows.append(f"{head}```mermaid\n{fl['mermaid']}\n```")
        tabs.append(("Flowchart", "\n\n".join(flows)))
    issues = [issue_box(I[c]) for c in f["children"] if c in I]
    tabs.append(("Requirements", "\n\n".join(issues) or "No requirements yet."))
    # use cases sit under the description, in a section that opens and closes
    uc = bullets(s.get("use cases"))
    use_cases = (f'??? usecases "Use cases · {len(uc)}"\n' + "\n".join(f"    - {u}" for u in uc)) if uc else ""
    tab_text = "\n\n".join(f'=== "{name}"\n\n{ind(body, 4)}' for name, body in tabs)
    side_issues = "\n".join(f"- {ICON[I[c]['status']]} [#{c} {I[c]['title']}]({GH}{c})" for c in f["children"] if c in I)
    listing = lambda xs: "\n".join(f"- {x}" for x in xs) or "None"
    last = nice_date(max([f["updated"]] + [i["updated"] for i in tree(f["n"])]))
    return f"""
---
hide:
  - toc
---

# {f['title']}

<div class="overview" markdown>

{s.get('what it is') or s.get('requirement') or ''}

{use_cases}

<div class="facts">
  <div><span class="label">Who uses it</span>{s.get('who uses it', '—')}</div>
  <div><span class="label">Status</span>{pill(f['status'])}</div>
  <div><span class="label">Priority</span>{f['priority'] or '—'}</div>
  <div><span class="label">Target date</span>{nice_date(f['target']) or '—'}</div>
  <div><span class="label">Feature issue</span><a href="{GH}{f['n']}">#{f['n']}</a></div>
</div>

</div>

<div class="feature-layout" markdown>

<div class="feature-main" markdown>

{tab_text}

</div>

<aside class="side-panel" markdown>

#### Requirements

{side_issues or 'None yet'}

#### Open questions

{listing(f['questions'])}

#### Not confirmed yet

{listing(f['unconfirmed'])}

#### Last updated

{last}

[:material-comment-outline: Comment on GitHub]({GH}{f['n']}){{ .md-button .md-button--primary }}

</aside>

</div>
"""


for old in (DOCS / "features").glob("*.md") if (DOCS / "features").exists() else []:
    old.unlink()
for f in FEATURES:
    write(f"features/{f['slug']}.md", feature_page(f))

feature_cards = "\n".join(
    f"-   **[{f['title']}]({f['slug']}.md)**\n\n    {f['sections'].get('what it is', '')}\n\n"
    f"    {f['sections'].get('who uses it', '')} · {pill(f['status'])}\n" for f in FEATURES)
write("features/index.md", f"""
---
hide:
  - toc
---

# Features

<p class="lead">Each feature has a short overview, then tabs for its wireframes, flowchart, requirements and use cases.</p>

<div class="grid cards" markdown>

{feature_cards}
</div>
""")

# ---- Home
cards, work = [], [i for i in I.values() if i["n"] not in BY_N and root(i["n"]) in BY_N]
for f in FEATURES:
    t = tree(f["n"])
    done = sum(1 for i in t if i["status"] == "Done")
    pct = max(round(done / len(t) * 100), 4) if t else 4
    cards.append(f"""-   **[{f['title']}](features/{f['slug']}.md)**

    {f['sections'].get('who uses it', '')} · {pill(f['status'])}

    <span class="bar bar--{PILL[f['status']]}"><span style="width:{pct}%"></span></span>
    <span class="small">{done} of {len(t)} requirements done</span>
""")
stats = [(len(FEATURES), "Features", ""), (len(work), "Requirements", "")] + [
    (sum(1 for i in work if i["status"] == s), s, PILL[s]) for s in PILL]
stat_html = "\n".join(f'  <div class="stat{" stat--" + c if c else ""}"><span class="num">{v}</span><span class="label">{l}</span></div>'
                      for v, l, c in stats)
inputs = "\n".join(f"- {q} [{f['title']}](features/{f['slug']}.md)" for f in FEATURES for q in f["questions"]) or "- Nothing waiting"
recent = "\n".join(f"- {nice_date(i['updated'])} · [#{i['n']} {i['title']}]({GH}{i['n']})"
                   for i in sorted(I.values(), key=lambda i: i["updated"], reverse=True)[:5])
write("index.md", f"""
---
hide:
  - navigation
  - toc
---

<div class="feature-layout" markdown>

<div class="feature-main" markdown>

# {os.environ.get('HANDBOOK_TITLE', 'Requisio handbook')}

<p class="lead">How Requisio works: each feature with its wireframes, flowchart, issues and use cases, in one place.
<em>Requisio is a made-up purchase-request app, used to practise UX documentation.</em></p>

<div class="stats">
{stat_html}
</div>

## Where things stand

<div class="grid cards cols-2" markdown>

{chr(10).join(cards)}
</div>

## Find your way

<div class="grid cards" markdown>

-   :material-view-dashboard-outline:{{ .lg }} **[Features](features/index.md)**

    One page per feature: an overview, then the wireframes, flowchart, issues and use cases.

-   :material-account-group-outline:{{ .lg }} **[Users](user-understanding.md)**

    Who uses Requisio, their journey, and all use cases.

-   :material-table:{{ .lg }} **[Requirements](requirements.md)**

    Every issue with the project board's columns, in one table.

</div>

</div>

<aside class="side-panel" markdown>

#### Needs your input

{inputs}

#### Recently changed

{recent}

#### Last updated

{UPDATED}

[:material-comment-outline: Give feedback on GitHub](https://github.com/{REPO}/issues){{ .md-button .md-button--primary }}

</aside>

</div>
""")


# ---- Requirements (the board's columns)
def row(i, depth, feature):
    indent = "&nbsp;&nbsp;&nbsp;&nbsp;" * max(depth - 1, 0)
    name = f"**[{i['title']}](features/{feature['slug']}.md)**" if depth == 0 else f"{indent}↳ {i['title']}"
    flow = f"[View](features/{feature['slug']}.md)" if feature["flows"] else DASH
    wire = (f"[View](features/{feature['slug']}.md)" if WIREFRAMES.get(i["n"]) else '<span class="small">None yet</span>')
    return (f"| [#{i['n']}]({GH}{i['n']}) | {name} | {feature['title']} | {pill(i['status'])} | {i['priority']} | "
            f"{who(i)} | {nice_date(i['start'])} | {nice_date(i['target'])} | {flow} | {wire} | "
            f"{i['comments'] or DASH} |")


def depth_of(i):
    d = 0
    while I[i["n"]]["parent"] and I[i["n"]]["parent"] in I:
        i, d = I[I[i["n"]]["parent"]], d + 1
    return d


HEAD = ("| # | Requirement | Feature | Status | Priority | Assignee | Start date | Target date | Flowchart | Wireframe | "
        "Comments / inputs |\n|---|---|---|---|---|---|---|---|---|---|---|")
rows = []
for f in FEATURES:
    rows.append(row(f, 0, f))
    rows += [row(i, depth_of(i), f) for i in tree(f["n"])]
# Safety check: anything sitting at the wrong level
PROBLEMS = []
for i in I.values():
    d = depth_of(i)
    if "feature" in i["labels"] and i["parent"]:
        PROBLEMS.append((i, "it's a 1 · Feature but sits under another issue. Remove it from there."))
    elif i["n"] in BY_N or root(i["n"]) not in BY_N:
        continue
    elif d >= 3:
        PROBLEMS.append((i, "it's a 4th level. Write it as a bullet in the Details of its sub-requirement instead."))
    elif d == 2 and "requirement" in i["labels"]:
        PROBLEMS.append((i, "it sits under a requirement, so its label should be sub-requirement."))
    elif d == 1 and "sub-requirement" in i["labels"]:
        PROBLEMS.append((i, "it sits directly under a feature, so its label should be requirement."))
problem_text = ""
if PROBLEMS:
    problem_text = ('\n!!! warning "Needs fixing"\n    These are at the wrong level. Open each one on GitHub to fix it.\n\n' +
                    "\n".join(f"    - [#{i['n']} {i['title']}]({GH}{i['n']}): {why}" for i, why in PROBLEMS) + "\n")
orphan_text = ""
if ORPHANS:
    orphan_text = ("\n## Not under a feature\n\n<p class=\"lead\">These aren't placed under any feature yet. "
                   "Open the feature and use Add existing issue, so each one shows on that feature's page.</p>\n\n"
                   "| # | Issue | Status | Assignee |\n|---|---|---|---|\n" +
                   "\n".join(f"| [#{i['n']}]({GH}{i['n']}) | {i['title']} | {pill(i['status'])} | {who(i)} |"
                             for i in ORPHANS))
board_note = ("" if BOARD_READ else
              '\n!!! warning "Board columns not available"\n    The website couldn\'t read the project board this time, '
              "so status, priority, dates and comments may be missing.\n")
write("requirements.md", f"""
---
hide:
  - navigation
  - toc
---

# Requirements

<p class="lead">Every issue, with the <a href="{BOARD_URL}">project board</a>'s columns, grouped by feature. Click a number to open it on GitHub and comment.</p>
{board_note}{problem_text}
<div class="req-table" markdown>

{HEAD}
{chr(10).join(rows)}

</div>
{orphan_text}
""")

# ---- the Features menu in mkdocs.yml
cfg = ROOT / "mkdocs.yml"
text = cfg.read_text(encoding="utf-8")
menu = "\n".join(f"      - {json.dumps(f['title'])}: features/{f['slug']}.md" for f in FEATURES)
text = re.sub(r"(  - Features:\n      - features/index.md\n(?:      #.*\n)?)(?: {6,}-.*\n)*", lambda m: m.group(1) + menu + "\n", text)
cfg.write_text(text, encoding="utf-8", newline="\n")

print(f"Handbook pages made: {len(FEATURES)} features, {len(work)} issues, {len(ORPHANS)} not under a feature, {len(PROBLEMS)} need fixing, "
      f"{sum(len(v) for v in WIREFRAMES.values())} wireframes, board read: {BOARD_READ}")
