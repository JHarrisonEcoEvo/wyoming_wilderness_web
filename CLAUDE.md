# Instructions: Build Wyoming Wilderness Web as a Hugo site

## Overview

I'm migrating my WordPress site (https://wyomingwildernessweb.wordpress.com/) to Hugo, hosted on GitHub Pages. It's a simple site about Wyoming's designated Wilderness areas and Wilderness Study Areas (WSAs). Please scaffold the full Hugo project.

## Site structure

The site has these sections:

1. **Homepage** — intro text about the project, then two lists: WSAs (45 of them) and Wilderness areas (15). Each list item links to its page if `visited: true` in frontmatter, otherwise it's plain text. The homepage prose from the current WordPress site should be migrated over.
2. **WSA pages** (e.g., `/wsa/bennett-mountain/`) — individual location pages with these sections: a prose description, Infrastructure, Access, Safety, Flora and fauna, Statistics (acreage, elevation range), and an Inspiration section for photos. Use a shared template.
3. **Wilderness pages** (e.g., `/wilderness/bridger/`) — same template structure as WSA pages.
4. **Blog** (`/blog/`) — simple blog listing page with posts in reverse chronological order. Individual posts are just markdown with a date and title.
5. **About page** (`/about/`)

## Content to migrate

Pull content from the live WordPress site for these existing pages:
- Homepage (https://wyomingwildernessweb.wordpress.com/)
- About (https://wyomingwildernessweb.wordpress.com/about/)
- Bennett Mountain WSA (https://wyomingwildernessweb.wordpress.com/bennett-mountain-wsa/)
- Devil's Playground WSA (https://wyomingwildernessweb.wordpress.com/devils-playground-wsa/)
- Blog posts from https://wyomingwildernessweb.wordpress.com/blog/

For all WSAs and Wilderness areas that don't have pages yet, create placeholder markdown files with `visited: false` in the frontmatter and no body content. The full list of WSAs and Wilderness areas is on the homepage.

## Location page frontmatter

Each WSA/Wilderness markdown file should have frontmatter like:

```yaml
---
title: "Bennett Mountain WSA"
type: wsa  # or "wilderness"
visited: true  # false for placeholder pages
acreage: 6003
acreage_km2: 24.29
elevation_range: "6,580–7,986"
draft: false
---
```

For placeholder (not-yet-visited) pages, just include title, type, visited: false, and draft: true.

## Design and styling

- Clean, simple design. Not flashy. Think old-school web but readable. Earth tones — sage greens, warm tans, muted browns. Nothing corporate.
- The header image from the WordPress site is a landscape photo used as a banner. Replicate that concept.
- Good typography for long-form reading (the location descriptions are prose-heavy).
- Mobile responsive but don't overthink it.
- No JavaScript frameworks. Plain CSS. Keep it lightweight and fast.
- Navigation: Home, About, Blog in the top nav. Keep it minimal.

## Hugo specifics

- Use Hugo's built-in features, no external theme. Build the templates from scratch so they're simple and I can understand and edit them.
- Use Hugo archetypes for WSA and Wilderness content types so I can run `hugo new wsa/some-place.md` and get the right frontmatter template.
- The homepage should auto-generate the WSA and Wilderness lists from the content files, sorted alphabetically. Link them if visited: true, plain text if not.
- Set up a `hugo.toml` config file with sensible defaults.
- Put images in `static/images/` for now. Reference the WordPress image URLs in the migrated content as placeholders — I'll download and replace them later.

## GitHub Pages deployment

- Include a `.github/workflows/deploy.yml` GitHub Actions workflow that builds the Hugo site and deploys to GitHub Pages on push to `main`.
- Include a README.md explaining how to:
  - Install Hugo locally
  - Run the dev server (`hugo server`)
  - Add a new location page
  - Add a new blog post
  - How the GitHub Pages deploy works

## Repository setup

Initialize this as a git repo. The repo name will be `wyoming-wilderness-web`.

## What NOT to do

- Don't use a pre-built Hugo theme. Build templates from scratch.
- Don't add any CMS, admin panel, or dynamic backend.
- Don't add analytics, tracking, or cookie banners.
- Don't add comments functionality.
- Don't over-engineer the CSS. Simple is better.
