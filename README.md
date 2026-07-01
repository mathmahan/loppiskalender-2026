# Loppiskalender 2026

En enkel, mobilvänlig kalender över antik- och loppisbutiker i **Skåne, Blekinge,
Småland & Halland**, baserad på *Antikt och Loppisguiden 2026*.

- **Veckokalender** – se vilka butiker som är öppna varje veckodag.
- **Lista** – alla butiker med öppettider, adress och länkar (🌐 webbplats · 📘 Facebook · 📷 Instagram).
- Sök och filtrera på kommun/region och typ (antikt, loppis, café, auktion).

Butiker utan fasta veckotider visas separat (rörliga/aviserade tider), och de som saknar
angivna tider i guiden listas under **N/A**.

## Bygga sidan

Allt innehåll och all layout ligger i `gen.py` (endast Python-standardbibliotek – inga
beroenden). Kör:

```sh
python3 gen.py
```

Det genererar `index.html`. Öppna filen i en webbläsare, eller besök den publicerade
versionen (GitHub Pages).

## Utveckling: git-flöde & versionering

Projektet använder [semantisk versionering](https://semver.org/lang/sv/) och en gren per
funktion.

- `main` är den stabila grenen och publiceras via GitHub Pages.
- Varje ny funktion görs i en egen gren, t.ex. `feat/responsive-mobile`.
- Grenen slås ihop till `main` med `--no-ff` och taggas med en ny version:
  - `v0.1.0` – första utgåvan (kalendern som den var).
  - minor-höjning (`0.x`) per funktion.
- Ändras `gen.py` ska `index.html` regenereras och checkas in i samma commit.

## Filer

| Fil | Beskrivning |
| --- | --- |
| `gen.py` | Generator – data, CSS och JS. Enda filen med logik. |
| `index.html` | Genererad sida (publiceras). |
| `DEFERRED.md` | Backlogg (bl.a. kartfunktionen som pausats). |
| `Antikt-och-loppisguiden-2026.pdf` | Källa (lokal, ej i git – upphovsrättsskyddad). |
