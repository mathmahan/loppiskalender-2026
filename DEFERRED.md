# Deferred / backlog — Loppiskalender 2026

Features intentionally postponed. Pick up here when revisiting the project.

## 1. Map view (with "My Location" + distance sorting) — REMOVED, to redo

**Status:** Removed 2026-07-01. Was showing pins in the wrong places.

**Why it was wrong:** The guide's PDF has no coordinates (only two entries printed
GPS). I approximated each place's lat/lng from the town/village name via a hand-built
lookup table + jitter. That put many pins in the wrong spot, and — because the
"My Location" / sort-by-distance feature used the same coordinates — distances were
unreliable too. So the whole location feature set was pulled, not just the map.

**What's needed to do it properly:**
- Real geocoding of each entry's street address (not just the town). Options:
  - Batch-geocode the 182 addresses once (e.g. Nominatim/Google/Mapbox), review the
    results by hand, and bake verified `lat`/`lng` into the data in `gen.py`.
  - Flag low-confidence hits (village-only / rural addresses) for manual correction.
- Then re-add:
  - Leaflet map tab with markers + popups (keyless dark basemap, e.g. CARTO
    `dark_all`, which worked from `file://`).
  - "📍 Min plats" (browser geolocation; note it's blocked over `file://` — needs a
    local server or hosting) + an ort-search fallback via geocoding.
  - Sort-by-distance + distance chips in week/list views.

**Note:** the link icons (🌐/📘/📷), dark-blue theme, week grid, list view, and the
N/A section are all still in place — only the location/map parts were removed.

The generator lives in the scratchpad `gen.py`; the previous map implementation is in
this conversation's history if useful as a starting point.
