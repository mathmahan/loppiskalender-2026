# Deferred / backlog — Loppiskalender 2026

Features intentionally postponed. Pick up here when revisiting the project.

## 1. Map view (with "My Location" + distance sorting) — ✅ DONE (v0.6.0)

Implemented 2026-07-04. Real coordinates were obtained by geocoding each shop's
street address (Nominatim, with cleaned queries + a southern-Sweden bounding box).
Results live in `coordinates.csv` (`num,lat,lng,approx,address`) and are read by
`gen.py` at build time. The **Karta** tab shows Leaflet markers (keyless CARTO
`dark_all` basemap) with popups; **📍 Min plats** / ort-search set a reference point
for **sort-by-distance** + distance chips across the views.

### Remaining refinement (optional)
- **36 shops are `approx=1`** (town-level only) — geocoding couldn't resolve them to a
  street, so their pin sits at the town center and is drawn as a hollow marker. To
  tighten: open them in Google My Maps, drag each pin to the right spot, export KML,
  and update the `lat`/`lng`/`approx` for those rows in `coordinates.csv`. List them
  with: `awk -F, '$4==1' coordinates.csv`.
- Geolocation ("📍 Min plats") needs a secure context — works on the GitHub Pages URL,
  but a browser may block it when opening `index.html` directly as `file://` (the
  ort-search box is the fallback there).
