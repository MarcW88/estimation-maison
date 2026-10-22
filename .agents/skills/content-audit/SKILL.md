---
name: content-audit
description: Auditer une page éditoriale existante avant réécriture et décider KEEP, UPDATE, MERGE, REDIRECT ou REMOVE à partir de l'intention, de la valeur originale, des performances disponibles et des chevauchements. Adapté du skill content-audit de MarcW88/italiaanse-percolator.
license: MIT
metadata:
  upstream: https://github.com/MarcW88/italiaanse-percolator/tree/main/.agents/skills/content-audit
  adapted_for: bloc-notes-numeriques.fr
---

# Content Audit — adaptation bloc-notes-numeriques.fr

Utiliser ce skill avant toute réécriture d'une page existante. Il audite et décide ; il ne rédige pas la nouvelle page.

## Principe

Une page faible ne mérite pas automatiquement une réécriture. Vérifier d'abord si l'URL possède encore une fonction propre, une intention identifiable, une valeur historique ou éditoriale et un potentiel de récupération.

Ne jamais compléter une donnée manquante par supposition. Si GSC, backlinks, historique ou autre signal n'est pas disponible, le signal reste `UNKNOWN`.

## Entrées utiles

Utiliser autant que possible :

- URL et contenu actuels ;
- requêtes cibles ou historiques ;
- données GSC historiques et récentes lorsqu'elles existent ;
- clics, impressions et positions avant/après une baisse lorsqu'ils existent ;
- backlinks et liens internes lorsqu'ils sont disponibles ;
- pages voisines du même cluster ;
- type de page et fonction éditoriale ;
- état actuel des produits, marques, services ou technologies cités.

## Décisions

### KEEP

La page est unique, actuelle, utile et sert encore une intention claire. Des corrections mineures restent possibles, mais une réécriture profonde n'est pas justifiée.

### UPDATE

L'URL garde une fonction ou un potentiel, mais présente une ou plusieurs faiblesses : informations obsolètes, valeur trop faible, structure inadaptée, preuves insuffisantes, contenu trop marchand ou dérive d'intention.

Après `UPDATE`, utiliser `content-refresh` pour choisir entre correction légère, révision majeure ou réécriture complète.

### MERGE

Deux ou plusieurs URLs servent essentiellement la même intention sans valeur distincte suffisante. Choisir la destination la plus logique à partir des performances, liens, pertinence, historique et architecture du site.

### REDIRECT

La page n'a plus de raison autonome d'exister mais un successeur pertinent existe. Le skill recommande la destination ; il n'applique pas la redirection automatiquement.

### REMOVE

Seulement si l'URL n'a plus d'intention utile, de valeur historique, de liens significatifs ni de fonction éditoriale et ne mérite pas de consolidation.

## Risques à signaler sur un site affilié

Flagger explicitement :

- paraphrase de fiches fabricant ou marchand ;
- pages dont seul le nom de marque/modèle change ;
- architecture répétée sans justification par l'intention ;
- introductions, conclusions ou sections génériques ;
- recommandations sans critères ou sans limites visibles ;
- informations obsolètes sur modèles, générations, prix, compatibilités ou disponibilité ;
- faux niveau d'expérience ou test non démontré ;
- absence de réponse claire à la question de décision du lecteur ;
- cannibalisation avec une autre URL ;
- contenu qui perd presque toute utilité si les liens affiliés disparaissent.

## Output

Retourner :

1. `Decision`: KEEP / UPDATE / MERGE / REDIRECT / REMOVE
2. `Confidence`: high / medium / low
3. `Evidence`: signaux concrets utilisés
4. `Unknowns`: données manquantes qui limitent le diagnostic
5. `Main problem`: problème principal
6. `Recovery potential`: pourquoi une récupération est ou non justifiée
7. `Next skill`: prochaine étape recommandée

Ne pas réécrire la page pendant cet audit.
