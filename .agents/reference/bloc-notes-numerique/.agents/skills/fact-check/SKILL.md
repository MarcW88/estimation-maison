---
name: fact-check
description: Verifieer product- en koffieclaims op italiaanse-percolator.nl in een aparte pass na de inhoudelijke rewrite.
license: MIT
---

# Fact check — italiaanse-percolator.nl

Deze pass staat los van schrijven. Een claim is niet betrouwbaar omdat hij plausibel klinkt.

## Claims die altijd gecontroleerd moeten worden

- materiaal (aluminium, RVS, coatings);
- inhoud/capaciteit en cup-aanduidingen;
- inductiecompatibiliteit;
- vaatwasserbestendigheid;
- warmtebronnen;
- afmetingen en gewicht;
- elektrische vermogens;
- veiligheidsfuncties;
- meegeleverde onderdelen;
- modelvarianten;
- garantie wanneer genoemd;
- historische merkclaims;
- vergelijkende claims zoals sneller, duurzamer, lichter of beter;
- prijzen en beschikbaarheid wanneer als actueel gepresenteerd.

## Bronnenhiërarchie

1. fabrikant / officiële handleiding;
2. officiële distributeur;
3. betrouwbare retailer voor actuele verkoopinformatie;
4. onafhankelijke tests of vakbronnen;
5. meerdere gebruikersbronnen voor ervaringspatronen.

Gebruik geen andere affiliatepagina als primaire bron voor een productspecificatie als een officiële bron beschikbaar is.

## Proces

1. Extraheer alle verifieerbare claims.
2. Label: hard fact / soft fact / vergelijking / ervaring / mening.
3. Zoek een externe bron voor elke belangrijke claim.
4. Geef status:
   - CONFIRMED
   - PARTIAL
   - UNVERIFIED
   - CONTRADICTED
   - OUTDATED
5. Corrigeer alleen op basis van bewijs.
6. Laat onzekerheid zichtbaar; vul gaten niet op met modelkennis.

## Belangrijke grens

Gebruikerservaring mag niet transformeren in eigen ervaring.

"Gebruikers melden dat..." kan gerechtvaardigd zijn na voldoende brononderzoek.
"Wij merkten dat..." is verboden zonder aantoonbare eigen test.

## Output

Maak een compact verificatielog:

| Claim | Status | Source | Action |
|---|---|---|---|

Eindig met:
- **Overall confidence**
- **Corrections required**
- **Claims to remove if unverifiable**

Pas daarna mag `natural-writing` draaien.
