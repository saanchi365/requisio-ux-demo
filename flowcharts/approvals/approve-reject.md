# Approvals: approve, reject or ask for changes

| | |
|---|---|
| **Status** | Draft — made-up demo content |
| **Area** | Approvals (#10) |
| **Based on** | Issues #10, #11, #12, #13 · Use cases 4–6 · Journey map stage 6 |
| **Diagram type** | Flowchart |

**How to read it:** rounded rectangle = start or end · rectangle = a step · diamond = a decision · a **dashed border** means it is an assumption.

<!-- --8<-- [start:flow] -->
```mermaid
flowchart TD
    a("Approver opens a waiting request")
    b["Read details, quote and history"]
    c{"Decision"}
    d{"More approvers in the route?"}
    e("Sent to the next approver")
    f("Approved: requester notified")
    g["Enter a reason<br/>#11"]
    h("Rejected: requester notified")
    i["Write what to change<br/>#12"]
    j["Requester edits and resubmits"]
    k["Choose a colleague and dates<br/>#13"]
    l("Delegated")
    a --> b --> c
    c -->|Approve| d
    d -->|Yes| e
    d -->|No| f
    c -->|Reject| g --> h
    c -->|Ask for changes| i --> j --> a
    c -->|Delegate| k --> l
```
<!-- --8<-- [end:flow] -->

## What comes from the documents
- Reject needs a reason (#11)
- Changes and resubmit keep history (#12)
- Delegation with dates (#13)

## Assumptions

## Open questions
- Do approvers decide one after another, or at the same time?

## Decisions
_None yet._ When you change this flowchart yourself, add one line here: `date — what changed — who — why`
