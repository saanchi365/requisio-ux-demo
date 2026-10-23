# How to add things to the handbook

Everything on the handbook website comes from this project. You never edit the website itself:
change the issue, the board or the file, and the website updates within a minute (board-only changes within the hour, or straight away with **Actions → Build handbook → Run workflow**).

## Where each part of the website comes from

| On the website | Where you write it | How |
|---|---|---|
| Project name and brief | `handbook.yml` | Pencil icon, edit, commit |
| Stages (groups in the left menu) | `handbook.yml` **and** the Stage list in `.github/ISSUE_TEMPLATE/1-feature.yml` | Keep both lists the same |
| About users | `docs/user-understanding.md`, `docs/journey-map.md`, `docs/user-stories.md` | Edit like any document |
| A feature | An issue made with **1 · Feature** | New issue |
| A requirement | An issue made with **2 · Requirement**, inside its feature | Create sub-issue on the feature |
| A sub-requirement | An issue made with **3 · Sub-requirement**, inside its requirement | Create sub-issue on the requirement |
| Status, priority, target date, comments/inputs | Project board columns | Change on the board |
| Assigned to | The issue's Assignees | Right side of the issue |
| Given by | The "Given by" box in the form | Filled when creating |
| Open questions | The "Open questions" box in the feature or requirement | One per line, starting with "- " |
| Use cases (shown under the feature's description, open and close) | The "Use cases" box in the feature | Required for every feature; requirements don't have use cases |
| Flowcharts | A file in `flowcharts/` | See `flowcharts/README.md` |
| Wireframes | A picture in `wireframes/`, named with the issue number | See `wireframes/README.md` |
| Wireframe description and questions | A `.md` file next to the picture, same name | Optional |
| Created / updated dates, what changed recently | GitHub history | Automatic |

## The three levels

```
1 · Feature            → its own page
  2 · Requirement      → a row in the Requirements table
    3 · Sub-requirement → a row indented under its requirement (only for big requirements)
       small points    → bullets in the "Details" box, not more issues
```

## Add a feature
1. **Issues → New issue → 1 · Feature**. Fill in what it is, who uses it, stage, use cases and given by. Open questions are optional.
2. On the **board**: status, priority, target date.
3. Add its **flowchart** to `flowcharts/` and its **wireframes** to `wireframes/` (almost every feature has both).

## Add a requirement
1. Open the feature → **Sub-issues → Create sub-issue → 2 · Requirement**. (Already made it? **Add existing issue**.)
2. Big requirement? Open it → **Create sub-issue → 3 · Sub-requirement**.
3. Board: status, priority, target. Issue: Assignees.

## What if…

| What if… | What the website does | Fix |
|---|---|---|
| A feature is put inside another issue | Shows it under **Needs fixing** and does not treat it as a feature | Open it → Relationships → remove the parent |
| A requirement is not under any feature | Shows it under **Not under a feature** | Feature → Add existing issue |
| A sub-requirement was made with the Requirement form (or the reverse) | **Needs fixing**: wrong label | Change the label |
| Someone goes four levels deep | **Needs fixing** | Turn the fourth level into bullets in Details |
| An issue is closed | Shows Done, unless the board says otherwise (the board wins) | — |
| An issue is deleted | Disappears at the next update | — |
| No target date on the board | Shows "—", not counted as overdue | Add a date |
| A wireframe name has no or a wrong number | **Needs fixing: wireframes not matched** | Rename the file |
| A flowchart mentions a number that does not exist | **Needs fixing** | Correct the number |
| Someone comments on a GitHub issue | Shown on the website too, marked "from GitHub" | — |
| A website comment should become a requirement | Owner clicks **Turn into requirement**; a GitHub issue is created under that feature | Fill in its details |
| The board key expires (every 90 days) | Warning banner; board columns empty | Renew the `HANDBOOK_TOKEN` secret |
| Someone edits the website's pages directly | Overwritten at the next update | Edit the issue or file instead |

*Note: the website still shows the earlier layout. The new layout (Overview, Wireframes, Flowcharts, Requirements, Comments tabs) is being agreed in the prototype first, then built. The forms, folders and files above are already set up for it.*
