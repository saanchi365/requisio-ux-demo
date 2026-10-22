# Track: find a request and see its details

| | |
|---|---|
| **Status** | Draft — made-up demo content |
| **Area** | Request list & details (#14) |
| **Based on** | Issues #14, #15, #16 · Use cases 7–8 · Journey map stage 5 |
| **Diagram type** | Flowchart |

**How to read it:** rounded rectangle = start or end · rectangle = a step · diamond = a decision · a **dashed border** means it is an assumption.

```mermaid
flowchart TD
    a("User opens Requests")
    b{"How to find it?"}
    c["Search by item or number<br/>#15"]
    d["Status tabs: Draft, Waiting,<br/>Approved, Rejected<br/>#15"]
    e{"Found?"}
    f["No results: tips to change the search"]
    g["Open the request"]
    h["Details: status, current approver,<br/>route, history<br/>#16"]
    i{"Needs action?"}
    j["Edit and resubmit"]
    k("Done: information only")
    a --> b
    b -->|Search| c --> e
    b -->|Tabs| d --> e
    e -->|No| f --> b
    e -->|Yes| g --> h --> i
    i -->|Yes| j
    i -->|No| k
    class f guess
    classDef guess stroke-dasharray: 5 5
```

## What comes from the documents
- Search, filters and status tabs (#15)
- Details with route and history (#16)

## Assumptions

## Open questions
- Should requesters see other people's requests?

## Decisions
_None yet._ When you change this flowchart yourself, add one line here: `date — what changed — who — why`
