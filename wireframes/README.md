# Wireframes

Put wireframe pictures here (`.excalidraw.svg`, `.svg`, `.png` or `.jpg`).

## 1. Name the picture with its issue number

Start the file name with the number of the requirement (or sub-requirement) it shows, then a dash and a short name:

- `7-request-form.excalidraw.svg` → the screen for requirement **#7**
- `17-item-picker.png` → the screen for sub-requirement **#17**

The website then:
- shows it in that feature's **Wireframes** tab,
- puts it **in the same order as the flowchart** (the box with `#7` decides where screen #7 goes),
- links it from the **Wireframe** column of the Requirements table.

## 2. Optional: a description and open questions

Add a text file with **exactly the same name**, ending in `.md` instead of the picture's ending:

- picture: `7-request-form.excalidraw.svg`
- notes: `7-request-form.md`

Write it like this:

```markdown
## Description
What this screen is for, in one or two sentences.

## Open questions
- A question about this screen
```

Both parts are optional. With no notes file, the website shows "No description or open questions for this screen".

## What if

- **The name doesn't start with a number, or the number doesn't exist**: the picture is listed under "Needs fixing" on the Requirements page. Rename it.
- **Two pictures for the same requirement**: both are shown, one after the other.
- **The requirement isn't in any flowchart**: its screen goes after the ones that are, in number order.
