# Wyoming Wilderness Web — Claude Instructions

## What this site is

A personal field guide to Wyoming's designated Wilderness areas and Wilderness Study Areas (WSAs), built with Hugo and hosted on GitHub Pages. The author has personally visited some of these areas and written up field notes. It is not a corporate site, not a travel blog, and not a government resource — it's one person's experience in the backcountry.

## Tech stack

- **Hugo** (static site generator, no external theme — all templates are in `layouts/`)
- **GitHub Pages** deployment via `.github/workflows/deploy.yml`
- **Plain CSS** in `static/css/style.css` — no frameworks, no preprocessors
- **Vanilla JS only** — small inline scripts are fine, no frameworks
- Current branch `retro-1995` has a 1990s-era visual style

## Site structure

| Section | Path | Template |
|---|---|---|
| Homepage | `content/_index.md` | `layouts/index.html` |
| WSA pages | `content/wsa/*.md` | `layouts/wsa/single.html` |
| Wilderness pages | `content/wilderness/*.md` | `layouts/wilderness/single.html` |
| Blog | `content/blog/*.md` | `layouts/blog/` |
| About | `content/about/_index.md` | `layouts/_default/single.html` |

## Location page conventions

Frontmatter for a visited page:
```yaml
---
title: "Bennett Mountain WSA"
type: wsa        # or "wilderness"
visited: true
acreage: 6003
acreage_km2: 24.29
elevation_range: "6,580–7,986"
draft: false
---
```

Frontmatter for a placeholder (not yet visited):
```yaml
---
title: "Some Place WSA"
type: wsa
visited: false
draft: true
---
```

Placeholder pages render a notice automatically — no body content needed.

## Photo galleries

Photos in the Inspiration section use the `{{< gallery >}}` shortcode (defined in `layouts/shortcodes/gallery.html`). Wrap images like this:

```
## Inspiration

{{< gallery >}}
![alt text](url)

![alt text](url)
{{< /gallery >}}
```

The shortcode + inline JS in `baseof.html` builds a click-through slideshow automatically.

## Adding content

**New WSA or Wilderness page:**
```
hugo new wsa/place-name.md
# or
hugo new wilderness/place-name.md
```

**New blog post:**
```
hugo new blog/post-title.md
```

**Dev server:**
```
hugo server
```

## Rules — do not break these

- **Do not edit the author's writing.** The prose in content files is the author's own field notes and voice. Do not rephrase, clean up, summarize, or alter it in any way. If text needs to go somewhere, place it exactly as given.
- **Do not remove, reorder, or alter photos.** Image references in content files are the author's own photos. Do not change `src`, `alt` text, order, or quantity unless explicitly asked.
- **Do not add content the author hasn't written.** Do not invent descriptions, add placeholder prose, or fill in details for unvisited locations beyond the placeholder notice already in the template.
- **Do not use a pre-built Hugo theme.** All templates are custom and intentionally simple.
- **Do not add analytics, tracking, cookie banners, comments, or any dynamic backend.**
- **Do not over-engineer the CSS.** Simple is better. The retro-1995 branch intentionally looks old.
