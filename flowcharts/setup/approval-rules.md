# Setup: approval rules

| | |
|---|---|
| **Status** | Draft — made-up demo content |
| **Area** | Setup (#1) |
| **Based on** | Issues #1, #2, #3, #4 · Use cases 9–11 |
| **Diagram type** | Flowchart |

**How to read it:** rounded rectangle = start or end · rectangle = a step · diamond = a decision · a **dashed border** means it is an assumption.

<!-- --8<-- [start:flow] -->
```mermaid
flowchart TD
    a("Admin opens Setup")
    b["Add departments and approvers<br/>#2"]
    c["Add request categories<br/>#3"]
    d["Create an approval rule<br/>#4"]
    e{"Rule depends on amount?"}
    f["Set amount limit,<br/>e.g. over 5,000"]
    g["Choose extra approver,<br/>e.g. Finance"]
    h["Choose categories it applies to"]
    i{"Clashes with another rule?"}
    j["Show the clash and ask to fix it"]
    k("Rule saved and active")
    a --> b --> c --> d --> e
    e -->|Yes| f --> g --> h
    e -->|No| h
    h --> i
    i -->|Yes| j --> d
    i -->|No| k
    class i,j guess
    classDef guess stroke-dasharray: 5 5
```
<!-- --8<-- [end:flow] -->

## What comes from the documents
- Departments, categories and rules by amount (#2, #3, #4)

## Assumptions
- The system checks for clashing rules

## Open questions
- If two rules match, which one wins?

## Decisions
_None yet._ When you change this flowchart yourself, add one line here: `date — what changed — who — why`
