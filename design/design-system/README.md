# DeskTrace Design System — v2 "modern"

CSM 399 Capstone · Group 16 · owned by the UI/UX pair (Obed Opoku Junior, Louis Mawulolo)

> **v2 is a visual refresh, not a rewrite.** Every class name from v1 is unchanged,
> so anything already built against it keeps working. Cool slate neutrals, depth from
> layered shadows instead of a border on every box, larger radii, an accent ramp, and
> richer semantic hues. All six rules below survived; the full palette was re-verified
> at 44 pairs, all passing. New components: segmented control, timeline, sticky action bar.

## What is here

| File | Purpose |
|---|---|
| `desktrace.css` | The system itself — tokens and components. This is the only file the app imports. |
| `index.html` | Living style guide. Open it to see every token and component, with a light/dark toggle. |
| `README.md` | This file. |
| `../wireframes/` | Ten low-fidelity annotated screens — the reasoning behind each layout. |
| `../mockups/` | The same ten screens in this design system — the result, and the system's own test. |

## Charts

Horizontal bars, **one series per panel**, drawn in the accent. Rules that are not
negotiable, because breaking them breaks the status language:

- **Never use the SLA colours as a series colour.** Green, amber and red mean state.
  A chart that borrows red makes "red" stop meaning "breached".
- One series means **no legend** — the panel title already names what is plotted.
- Text wears text tokens. A category name is `--ds-ink-2`, never the bar's colour.
- Never a dual-axis chart. Two measures of different scale get two panels.

When the real Chart.js or Recharts build replaces these, it inherits the same rules.

## How to use it

**In the prototype:**
```html
<link rel="stylesheet" href="design-system/desktrace.css">
```

**In the React/Vite app**, once in `src/main.jsx`:
```js
import './design-system/desktrace.css'
```

Then compose with the `ds-` classes. **Never write a raw hex value, pixel size or
spacing number inside a component.** If a token is missing, add it to
`desktrace.css` and tell the pair — that is how the visual language stays one thing.

## Viewing the style guide

The page loads `desktrace.css` by relative path, so opening `index.html` directly
from the file system works in most browsers. If your browser blocks it, serve the
folder:

```powershell
python -m http.server 5500 --directory "C:\Users\HP\OneDrive\Desktop\DeskTrace"
```

Then open <http://localhost:5500/design-system/>.

## The six rules

1. **Colour is never the only signal.** Every SLA state has a colour, an icon and a
   word. About one man in twelve cannot separate our red from our green, and a
   lecture-hall projector washes out both.
2. **Verified contrast, not guessed.** Every text pair is ≥4.5:1, every control
   border and focus ring ≥3:1 (WCAG 2.1 AA). Measured values are printed on the
   swatches in the style guide.
3. **No web fonts, no icon fonts.** DeskTrace is offline-first (FR-OFF-01). A font
   that fails to load is a broken screen, so we use the system stack and text glyphs.
4. **Body and form text is 16px.** Below 16px, iOS Safari zooms the page when a
   field is focused — unusable for a requester filing a ticket one-handed.
5. **Touch targets are at least 44×44px** (WCAG 2.5.5). Technicians use this
   standing up, in a corridor, holding equipment.
6. **Three signals, three languages.** Ticket status is a *word*, priority is a
   *shape* (a four-step meter), SLA state is a *colour*. They never compete.

Rule 6 is the one most likely to be broken by accident. If you are about to colour
a status chip red, you are taking red away from SLA breaches — don't.

## Token naming

All tokens are prefixed `--ds-`:

- `--ds-bg`, `--ds-surface`, `--ds-surface-2` — backgrounds, page to inset
- `--ds-ink`, `--ds-ink-2` — primary and secondary text
- `--ds-line` (decorative edges) vs `--ds-line-control` (input borders, needs 3:1)
- `--ds-accent-tint` / `--ds-accent` / `--ds-accent-hover` — the action ramp
- `--ds-ok` / `--ds-warn` / `--ds-bad`, each with a `-soft` tint for chip
  backgrounds. In v2 the plain value passes AA both as text and as a fill, so the
  separate `-text` tokens are gone — they remain as aliases so v1 markup still works,
  but new code should use the plain name.
- `--ds-text-*`, `--ds-space-*`, `--ds-radius-*`, `--ds-shadow-1..3`

**Icon badges:** `.ds-sla::before` and `.ds-notice::before` set their fill and glyph
colours explicitly. Do not replace these with `background: currentColor` — the variant
also sets the pseudo-element's own `color`, so `currentColor` resolves to the glyph
colour and paints the badge the same shade as the chip behind it. The icon then
disappears, which breaks rule 1.

Dark mode is automatic via `prefers-color-scheme`, and can be forced with
`<html data-theme="dark">` when a manual toggle is built.

## Checking a change

Before merging anything that touches this file:

1. Open the style guide in both themes (the toggle is in the header).
2. Check the **greyscale proof** row still reads. If a new component loses its
   meaning without colour, it breaks rule 1.
3. Resize to 375px wide. Buttons should go full width, grids to one column,
   form controls stay 16px and 44px tall.
