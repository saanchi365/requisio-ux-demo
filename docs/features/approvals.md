---
hide:
  - toc
---

# Approve purchase requests

<div class="overview" markdown>

Approvers decide on requests in one place: **approve**, **reject with a reason**, **ask for changes** or **delegate**.

<div class="facts">
  <div><span class="label">Who uses it</span>Approvers, Finance</div>
  <div><span class="label">Status</span><span class="pill pill--todo">To do</span></div>
  <div><span class="label">Priority</span>P0</div>
  <div><span class="label">Feature issue</span><a href="https://github.com/saanchi365/requisio-ux-demo/issues/10">#10</a></div>
</div>

</div>

<div class="feature-layout" markdown>

<div class="feature-main" markdown>

<!-- When this feature gets a wireframe, add a "Wireframes" tab ABOVE the Flowchart tab, so it opens first. -->

=== "Flowchart"

    **Approve, reject or ask for changes**

    --8<-- "flowcharts/approvals/approve-reject.md:flow"

    **Who talks to whom**

    --8<-- "flowcharts/approvals/approval-sequence.md:flow"

=== "Issues"

    ??? issue "#11 · Approve or reject a request"
        Approvers approve, or reject with a reason.

        **Done when**

        - A reason is required to reject
        - Requester is notified

        <span class="pill pill--todo">To do</span> · [Open #11 on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/11)

    ??? issue "#12 · Ask for changes and resubmit"
        Approvers can send a request back; the requester edits and resubmits.

        **Done when**

        - Comments shown to the requester
        - Resubmitted request keeps its history

        <span class="pill pill--todo">To do</span> · [Open #12 on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/12)

    ??? issue "#13 · Delegate approval"
        Approvers can hand decisions to a colleague while away.

        **Done when**

        - Delegation has start and end dates
        - Both people can see delegated requests

        <span class="pill pill--todo">To do</span> · [Open #13 on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/13)

=== "Use cases"

    1. **Approve or reject**: decide, giving a reason when rejecting.
    2. **Ask for changes**: send it back, and the requester edits and resubmits.
    3. **Delegate**: hand the decision to a colleague while away.

</div>

<aside class="side-panel" markdown>

#### Issues

- :material-circle-outline:{ .st-todo } [#11 Approve or reject a request](https://github.com/saanchi365/requisio-ux-demo/issues/11)
- :material-circle-outline:{ .st-todo } [#12 Ask for changes and resubmit](https://github.com/saanchi365/requisio-ux-demo/issues/12)
- :material-circle-outline:{ .st-todo } [#13 Delegate approval](https://github.com/saanchi365/requisio-ux-demo/issues/13)

#### Open questions

- Do approvers decide one after another, or at the same time?
- Is Finance always last?

#### Not confirmed yet

- Finance approves after the first approver

#### Last updated

22 Oct 2026

[:material-comment-outline: Comment on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/10){ .md-button .md-button--primary }

</aside>

</div>
