---
hide:
  - toc
---

# Set up approval rules

<div class="overview" markdown>

Admins set up **departments**, **categories** and **approval rules**, so every request follows the right route automatically.

<div class="facts">
  <div><span class="label">Who uses it</span>Admin</div>
  <div><span class="label">Status</span><span class="pill pill--done">Done</span></div>
  <div><span class="label">Priority</span>P1</div>
  <div><span class="label">Feature issue</span><a href="https://github.com/saanchi365/requisio-ux-demo/issues/1">#1</a></div>
</div>

</div>

<div class="feature-layout" markdown>

<div class="feature-main" markdown>

<!-- When this feature gets a wireframe, add a "Wireframes" tab ABOVE the Flowchart tab, so it opens first. -->

=== "Flowchart"

    --8<-- "flowcharts/setup/approval-rules.md:flow"

=== "Issues"

    ??? issue "Issue #2 · Set up departments and approvers"
        Admins add departments and choose each department's approver.

        **Done when**

        - Each department has at least one approver
        - Approvers can be changed later

        <span class="pill pill--done">Done</span> · [Open #2 on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/2)

    ??? issue "Issue #3 · Set up request categories"
        Admins create categories (IT equipment, Software, Services) with a few fields each.

        **Done when**

        - Categories can be added, renamed and switched off
        - Each category can have its own fields

        <span class="pill pill--done">Done</span> · [Open #3 on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/3)

    ??? issue "Issue #4 · Set up approval rules by amount"
        Requests above an amount need an extra approver (for example, over 5,000 needs Finance).

        **Done when**

        - Rules by amount and category
        - The route is shown before a request is submitted

        <span class="pill pill--done">Done</span> · [Open #4 on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/4)

=== "Use cases"

    1. **Set up departments and approvers**
    2. **Set up categories**
    3. **Set up approval rules** by amount and category

</div>

<aside class="side-panel" markdown>

#### Issues

- :material-check-circle:{ .st-done } [#2 Set up departments and approvers](https://github.com/saanchi365/requisio-ux-demo/issues/2)
- :material-check-circle:{ .st-done } [#3 Set up request categories](https://github.com/saanchi365/requisio-ux-demo/issues/3)
- :material-check-circle:{ .st-done } [#4 Set up approval rules by amount](https://github.com/saanchi365/requisio-ux-demo/issues/4)

#### Open questions

- If two rules match, which one wins?

#### Not confirmed yet

- The system checks for clashing rules

#### Last updated

22 Oct 2026

[:material-comment-outline: Comment on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/1){ .md-button .md-button--primary }

</aside>

</div>
