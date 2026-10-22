---
name: content-refresh
description: Bepaal hoe een geselecteerde UPDATE-pagina van italiaanse-percolator.nl inhoudelijk moet worden hersteld zonder onnodige volledige rewrite.
license: MIT
---

# Content refresh — italiaanse-percolator.nl

Gebruik alleen nadat `content-audit` de beslissing UPDATE heeft gegeven.

## Principe

Behoud wat goed is. Herstel het probleem, niet automatisch de hele tekst.

## Diagnose

Classificeer de belangrijkste oorzaak:

- **Intent drift:** de pagina beantwoordt niet meer wat de zoekopdracht vraagt.
- **Thin value:** correcte maar oppervlakkige informatie zonder echte beslissingswaarde.
- **Merchant duplication:** inhoud leunt te sterk op fabrikant- of winkelbeschrijvingen.
- **Outdated:** specs, beschikbaarheid, modellen, compatibiliteit of adviezen zijn verouderd.
- **Weak structure:** cruciale informatie staat te laat of verspreid.
- **Cannibalization:** overlap met een andere URL.
- **Generic prose:** veel tekst maar weinig concrete informatie.
- **Trust gap:** productclaims of aanbevelingen zijn onvoldoende onderbouwd.

## Refreshniveau

### Light edit
Voor kleine actualisaties, slechte passages of ontbrekende antwoorden. Behoud minstens 70% van bruikbare inhoud.

### Major revision
Voor een goede URL met structurele inhoudsgaten. Herbouw secties, maar behoud sterke passages, bewezen headings en relevante interne links.

### Full rewrite
Alleen wanneer de huidige tekst grotendeels duplicatief, generiek of verkeerd gericht is. De URL en zoekintentie blijven behouden tenzij expliciet anders besloten.

## Verplichte verbeteringen

Een herstelde pagina moet waar relevant duidelijk maken:
- wat het product/type precies is;
- voor wie het geschikt is;
- wanneer je beter een alternatief kiest;
- belangrijkste verschillen met relevante alternatieven;
- praktische beperkingen;
- compatibiliteit (bijv. inductie/gas/elektrisch) als dat relevant is;
- onderhoud en gebruik alleen wanneer dit voor de keuze helpt;
- welke claims uit primaire bronnen komen en welke uit gebruikerservaringen/synthese.

## Niet doen

- extra FAQ's toevoegen puur voor SEO;
- alle headings vervangen omdat een model dat "beter" vindt;
- elk keywordvariant forceren;
- bestaande concrete informatie vervangen door vage vloeiende tekst;
- oude rankingtekst verwijderen zonder reden.

## Output

Lever eerst een **refresh plan** met:
1. wat blijft;
2. wat wordt verwijderd;
3. wat wordt herschreven;
4. welke nieuwe informatie nodig is;
5. welke claims eerst onderzocht moeten worden;
6. aanbevolen refreshniveau.
