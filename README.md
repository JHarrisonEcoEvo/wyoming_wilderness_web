# Wyoming Wilderness Web

A Hugo site about Wyoming's designated Wilderness areas and Wilderness Study Areas (WSAs).

## Local Development

### Install Hugo

On macOS with Homebrew:

```sh
brew install hugo
```

For other platforms, see the [Hugo installation guide](https://gohugo.io/installation/).

### Run the dev server

```sh
hugo server -D
```

The `-D` flag includes draft pages (unvisited locations). Open `http://localhost:1313/` in your browser.

### Add a new location page

**WSA:**
```sh
hugo new wsa/some-place.md
```

**Wilderness area:**
```sh
hugo new wilderness/some-place.md
```

This creates a file with the right frontmatter template. Edit the file to add content, set `visited: true`, add statistics, and change `draft: false` when ready to publish.

Frontmatter fields for location pages:

```yaml
---
title: "Place Name WSA"
type: wsa           # or "wilderness"
visited: true       # true = has content and shows as a link on the homepage
acreage: 6003
acreage_km2: 24.29
elevation_range: "6,580–7,986"
draft: false        # false = published, true = hidden in production
---
```

### Add a new blog post

```sh
hugo new blog/my-post-title.md
```

Add a `date` field in the frontmatter. Set `draft: false` when ready to publish.

## GitHub Pages Deployment

The site auto-deploys on every push to `main` via GitHub Actions (`.github/workflows/deploy.yml`).

The workflow:
1. Installs Hugo on a GitHub runner
2. Builds the site with `hugo --gc --minify`
3. Uploads the built site as a GitHub Pages artifact
4. Deploys to GitHub Pages

### First-time setup

1. Go to your repo **Settings > Pages**
2. Under **Source**, select **GitHub Actions**
3. Push to `main` — the workflow will run and deploy automatically

## Project Structure

```
content/
  _index.md          # Homepage
  about/index.md     # About page
  blog/              # Blog posts
  wsa/               # WSA pages (one .md per area)
  wilderness/        # Wilderness pages (one .md per area)
layouts/             # Hugo templates
static/css/          # Stylesheet
static/images/       # Images (add your own here)
archetypes/          # Templates for hugo new
hugo.toml            # Site configuration
```
