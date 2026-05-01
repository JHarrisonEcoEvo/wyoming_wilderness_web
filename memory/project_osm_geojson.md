---
name: OSM polygon sourcing for WSA/wilderness maps
description: How to get and process WSA/wilderness polygons from OpenStreetMap for this site
type: project
---

WSA and wilderness polygons come from two sources:

1. **Existing GeoJSON files** in `static/data/` — run `python3 scripts/dissolve_geojson.py` after any changes to union duplicate features (requires `shapely`).

2. **OpenStreetMap via Overpass API** — used for USFS WSAs not in the BLM GeoJSON (Shoal Creek, Palisades, Pryor Mountain, Bighorn Tack-On). Find the relation ID first, then fetch with `out geom` and assemble rings by chaining ways end-to-end.

**Why:** OSM `out geom` returns individual member ways; naively treating each as a separate polygon creates fragmented MultiPolygons. Ways must be stitched end-to-end (reversing where needed) to form closed rings before passing to Shapely.

**Why:** The dissolve script uses `buffer(0)` to repair self-intersecting geometries before `unary_union`.

**Remaining gap:** High Lakes WSA (USFS, Beartooth Plateau) has no OSM polygon — only a dot marker on the homepage map. Palisades WSA western edge (Idaho state line) may still be slightly simplified.
