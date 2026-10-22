---
hide:
  - toc
---

# Create a purchase request

<div class="overview" markdown>

Employees raise a request to buy something, from a **catalog item** or a **custom item**, and send it for approval.

<div class="facts">
  <div><span class="label">Who uses it</span>Requester</div>
  <div><span class="label">Status</span><span class="pill pill--progress">In progress</span></div>
  <div><span class="label">Priority</span>P0</div>
  <div><span class="label">Feature issue</span><a href="https://github.com/saanchi365/requisio-ux-demo/issues/5">#5</a></div>
</div>

</div>

<div class="feature-layout" markdown>

<div class="feature-main" markdown>

<!-- When this feature gets a wireframe, add a "Wireframes" tab ABOVE the Flowchart tab, so it opens first. -->

=== "Flowchart"

    --8<-- "flowcharts/create-request/new-request.md:flow"

=== "Issues"

    ??? issue "Issue #6 · Start a new request"
        A clear “New request” button lets the requester choose a catalog item or a custom item.

        **Done when**

        - “New request” visible on every page
        - Catalog items pre-fill fields

        <span class="pill pill--progress">In progress</span> · [Open #6 on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/6)

    ??? issue "Issue #7 · Fill in request details"
        The requester fills item, quantity, cost, needed-by date and a reason.

        **Done when**

        - Required fields are marked
        - Missing fields are shown before submitting

        <span class="pill pill--progress">In progress</span> · [Open #7 on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/7)

    ??? issue "Issue #8 · Attach a vendor quote"
        The requester can upload a quote; the amount is read from it.

        **Done when**

        - PDF and images accepted
        - Amount from the quote can be corrected

        <span class="pill pill--progress">In progress</span> · [Open #8 on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/8)

    ??? issue "Issue #9 · Submit for approval"
        The requester sees the approval route and submits.

        **Done when**

        - Route shown before submit
        - Approvers are notified

        <span class="pill pill--progress">In progress</span> · [Open #9 on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/9)

=== "Use cases"

    1. **Request a catalog item**: pick a ready-made item, and most fields fill in.
    2. **Request something custom**: describe an item that isn't in the catalog.
    3. **Attach a vendor quote**: upload it, and the amount is read from it.

</div>

<aside class="side-panel" markdown>

#### Issues

- :material-progress-clock:{ .st-progress } [#6 Start a new request](https://github.com/saanchi365/requisio-ux-demo/issues/6)
- :material-progress-clock:{ .st-progress } [#7 Fill in request details](https://github.com/saanchi365/requisio-ux-demo/issues/7)
- :material-progress-clock:{ .st-progress } [#8 Attach a vendor quote](https://github.com/saanchi365/requisio-ux-demo/issues/8)
- :material-progress-clock:{ .st-progress } [#9 Submit for approval](https://github.com/saanchi365/requisio-ux-demo/issues/9)

#### Open questions

- Which file types are accepted for quotes?
- Can a catalog item's price be changed?

#### Not confirmed yet

- Requests can be saved as drafts

#### Last updated

22 Oct 2026

[:material-comment-outline: Comment on GitHub](https://github.com/saanchi365/requisio-ux-demo/issues/5){ .md-button .md-button--primary }

</aside>

</div>
