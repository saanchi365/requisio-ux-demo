# Overview: how Requisio's features connect

| | |
|---|---|
| **Status** | Draft — made-up demo content |
| **Area** | All features |
| **Based on** | Issues #1, #5, #10, #14 · Use cases · Journey map |
| **Diagram type** | Flowchart |

**How to read it:** rounded rectangle = start or end · rectangle = a step · diamond = a decision · a **dashed border** means it is an assumption.

```mermaid
flowchart LR
    subgraph SETUP["1 · Setup (admin, once)"]
        s1["Departments & approvers<br/>#2"]
        s2["Categories<br/>#3"]
        s3["Approval rules<br/>#4"]
        s1 --> s2 --> s3
    end
    subgraph CREATE["2 · Create a request (requester)"]
        c1("New request")
        c2["Fill details & attach quote"]
        c3["Submit"]
        c1 --> c2 --> c3
    end
    subgraph APPROVE["3 · Approvals (approver)"]
        a1{"Decision"}
        a2("Approved")
        a3["Changes requested"]
        a1 -->|Approve| a2
        a1 -->|Ask for changes| a3
    end
    subgraph TRACK["4 · Track (everyone)"]
        t1["Request list"]
        t2["Request details"]
        t1 --> t2
    end
    s3 -.->|"rules decide the route"| c3
    c3 --> a1
    a3 -->|"edit and resubmit"| c2
    a2 --> t1
```

## What comes from the documents
- Four areas and who uses each (User understanding)
- Request → approval → tracking (Journey map)

## Assumptions
- Admins finish setup before the first request is raised

## Open questions
- Can requesters see the approval route before submitting? (#4 says yes)

## Decisions
_None yet._ When you change this flowchart yourself, add one line here: `date — what changed — who — why`
