# Create request: new purchase request

| | |
|---|---|
| **Status** | Draft — made-up demo content |
| **Feature** | Create a purchase request (#5) |
| **Based on** | Issues #5, #6, #7, #8, #9 · Use cases 1–3 · Journey map stages 1–4 |
| **Diagram type** | Flowchart |

**How to read it:** rounded rectangle = start or end · rectangle = a step · diamond = a decision · a **dashed border** means it is an assumption.

<!-- --8<-- [start:flow] -->
```mermaid
flowchart TD
    a("Requester clicks New request<br/>#6")
    b{"Catalog item or custom?"}
    c["Pick a catalog item<br/>fields fill in"]
    d["Describe a custom item"]
    e["Fill details: quantity, cost,<br/>needed by, reason<br/>#7"]
    f{"Attach a vendor quote?"}
    g["Upload quote<br/>#8"]
    h["Amount read from the quote"]
    i{"All required fields filled?"}
    j["Show what is missing"]
    k["Show the approval route<br/>#9"]
    l{"Submit now?"}
    m("Saved as draft")
    n("Submitted: approvers notified")
    a --> b
    b -->|Catalog| c --> e
    b -->|Custom| d --> e
    e --> f
    f -->|Yes| g --> h --> i
    f -->|No| i
    i -->|No| j --> e
    i -->|Yes| k --> l
    l -->|Later| m
    l -->|Yes| n
```
<!-- --8<-- [end:flow] -->

## Description
How a requester raises a request: catalog or custom item, details, an optional quote, a check for missing fields, then submit or save as a draft.

## What comes from the documents
- Catalog vs custom items (Use cases 1–2)
- Quote upload with the amount read from it (#8)
- Route shown before submit (#9, journey map stage 4)

## Assumptions
- Requests can be saved as drafts

## Open questions
- Which file types are accepted for quotes?
- Can a catalog item's price be changed?

## Decisions
_None yet._ When you change this flowchart yourself, add one line here: `date — what changed — who — why`
