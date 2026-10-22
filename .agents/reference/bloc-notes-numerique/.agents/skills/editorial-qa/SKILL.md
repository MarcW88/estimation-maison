---
name: editorial-qa
description: Laatste publicatiegate voor herstelde content op italiaanse-percolator.nl.
license: MIT
---

# Editorial QA — italiaanse-percolator.nl

Gebruik als laatste stap. Deze skill schrijft de pagina niet opnieuw tenzij een kleine fout direct corrigeerbaar is.

## Gate 1 — Intent

PASS wanneer:
- pagina één duidelijke primaire intentie heeft;
- het antwoord of de beslissingshulp vroeg genoeg komt;
- secties die niets bijdragen verwijderd zijn.

## Gate 2 — Original affiliate value

PASS wanneer:
- content duidelijk meer biedt dan fabrikant/merchanttekst;
- aanbevelingen criteria en beperkingen bevatten;
- affiliate links niet de enige waarde zijn;
- er geen gefingeerde first-hand ervaring staat.

## Gate 3 — Factuality

PASS wanneer:
- belangrijke productspecificaties geverifieerd zijn;
- onzekere claims gekwalificeerd of verwijderd zijn;
- prijzen niet als duurzaam vaststaand worden gepresenteerd;
- vergelijkingen bewijsbaar of duidelijk als redactioneel oordeel gemarkeerd zijn.

## Gate 4 — Natural Dutch

PASS wanneer:
- tekst natuurlijk Nederlands leest;
- geen opvallende clusters generieke AI-formuleringen aanwezig zijn;
- zins- en alinearitme niet mechanisch is;
- producttaal niet overdreven promotioneel is;
- intro en conclusie informatie toevoegen.

## Gate 5 — SEO preservation

PASS wanneer:
- primaire intentie en onderwerp behouden zijn;
- title/H1/hoofdonderwerp coherent zijn;
- interne links logisch blijven;
- geen nieuwe cannibalisatie is ontstaan;
- relevante termen natuurlijk aanwezig zijn;
- er geen keyword stuffing is.

## Gate 6 — User usefulness

Stel de eindvraag:

**Zou deze pagina nog steeds nuttig zijn als alle affiliate links verdwenen?**

Zo nee: FAIL.

Controleer ook:
- Kan de lezer na deze pagina een betere keuze maken?
- Is duidelijk wanneer een ander product geschikter is?
- Zijn concrete details makkelijker te vinden dan vóór de rewrite?
- Is er echte informatie toegevoegd in plaats van alleen nieuwe formuleringen?

## Gate 7 — Décision d'image éditoriale

Pour les contenus de `bloc-notes-numeriques.fr`, exécuter `.agents/skills/editorial-image-planner/SKILL.md` après la rédaction et avant la publication.

PASS lorsque l'une des deux décisions est explicitement prise :

- `NOT_NEEDED` : aucune image générée n'apporte assez de valeur à la page ;
- une requête est créée dans `.content/image-requests/` avec un statut cohérent (`PENDING` pour une illustration générique à faible risque, `BLOCKED` lorsqu'une vraie image est nécessaire).

Ne jamais créer une image IA uniquement pour remplir la page. Ne jamais utiliser une image générée comme preuve d'un test, comme photo fidèle d'un produit précis, comme capture d'interface ou comme représentation de marque.

## Eindoutput

### PASS
Geef:
- status PASS;
- 3 belangrijkste verbeteringen;
- resterende kleine risico's.

### FAIL
Geef:
- status FAIL;
- failing gates;
- concrete blockers;
- naar welke skill teruggekeerd moet worden.

Een FAIL mag niet automatisch in een volledige rewrite veranderen.
