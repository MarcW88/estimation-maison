---
name: jobs-to-be-done
description: Analyser le progrès recherché par un utilisateur dans une situation donnée avant de raisonner en produit, persona ou fonctionnalité. Utiliser pour cadrer les pages /usages/, identifier les circonstances, jobs fonctionnels/émotionnels/sociaux, forces de changement, alternatives actuelles et critères d'adoption. Adapté du skill MIT wondelai/skills/jobs-to-be-done.
license: MIT
metadata:
  upstream: https://github.com/wondelai/skills/tree/main/jobs-to-be-done
  upstream_author: Wondel.ai sp. z o.o.
  adapted_for: bloc-notes-numeriques.fr
---

# Jobs to Be Done — adaptation éditoriale

Ce skill sert à comprendre **le progrès qu'une personne cherche à accomplir dans des circonstances précises**. Il ne sert pas à fabriquer un persona marketing ni à choisir directement un produit.

Principe : partir de la situation et du progrès recherché, puis seulement relier ce besoin à des contraintes, des familles de solutions et, si nécessaire, à un comparatif séparé.

## 1. Formuler le job sans nommer la solution

Utiliser la structure :

> Quand [circonstances], je veux [progrès], afin de [résultat recherché].

Le job principal doit pouvoir être formulé sans mentionner « bloc-notes numérique », « tablette E Ink », une marque ou un modèle. Si la solution apparaît dans le job, le cadrage est trop produit-centric.

## 2. Décrire les circonstances plutôt que les seules caractéristiques du public

Une catégorie comme « étudiant », « professionnel » ou « dessinateur » n'est pas encore un job.

Décrire :
- le moment ou contexte déclencheur ;
- le type de documents ou informations manipulés ;
- la fréquence et la durée de l'activité ;
- l'environnement physique ou logiciel ;
- ce qui rend la situation actuelle difficile ;
- le résultat concret attendu.

Une même personne peut avoir plusieurs jobs selon la situation.

## 3. Examiner les trois dimensions du job

### Fonctionnelle
Ce que l'utilisateur doit réellement accomplir : écrire, annoter, retrouver, transférer, lire, dessiner, classer, partager, etc.

### Émotionnelle
Ce que l'utilisateur cherche à ressentir ou éviter : rester concentré, réduire la charge mentale, avoir confiance dans la sauvegarde, éviter la frustration d'un workflow lent, etc.

### Sociale
Ce que l'usage change dans l'interaction avec d'autres personnes : partager un document propre, travailler sans écran lumineux en réunion, présenter des notes lisibles, collaborer, etc.

**Règle de preuve :** ne pas inventer de motivation émotionnelle ou sociale. Sans donnée utilisateur ou source crédible, la marquer comme `HYPOTHESIS` et ne pas la présenter comme un fait établi dans le contenu final.

## 4. Cartographier les forces de changement

Pour chaque usage, distinguer :

- **Push** : ce qui rend la situation actuelle insatisfaisante ;
- **Pull** : ce qui attire vers une nouvelle manière de travailler ;
- **Anxiety** : les risques perçus lors du changement ;
- **Habit** : ce qui rend la solution actuelle facile à conserver.

Le contenu doit traiter les freins autant que les bénéfices. Une page usage crédible explique donc aussi pourquoi quelqu'un pourrait rester avec du papier, un ordinateur, une tablette classique ou son système actuel.

## 5. Identifier la concurrence réelle

Lister tout ce qui peut être « engagé » pour faire le même job :

- cahier papier ;
- ordinateur portable ;
- tablette LCD ;
- liseuse ;
- smartphone ;
- impression papier ;
- combinaison de plusieurs outils ;
- ne rien changer.

Ne pas limiter la comparaison aux appareils E Ink.

## 6. Séparer Big Hire et Little Hire

- **Big Hire** : la décision d'acheter ou d'adopter une solution.
- **Little Hire** : la décision répétée de l'utiliser dans la situation réelle.

Une caractéristique peut aider à vendre l'appareil sans améliorer l'usage quotidien. Pour une page `/usages/`, privilégier les critères qui changent le Little Hire : friction d'import, vitesse pour retrouver une note, lisibilité réelle du PDF, simplicité d'export, poids porté tous les jours, etc.

## 7. Transformer le job en critères de décision

À partir des circonstances et du workflow réel, classer les critères en :

- `MUST_HAVE` — sans ce critère, le job échoue ;
- `HIGH` — influence fortement l'expérience ;
- `CONDITIONAL` — important seulement dans certaines circonstances ;
- `LOW` — secondaire pour ce job ;
- `CONTRAINDICATION` — caractéristique ou contrainte qui peut rendre cette famille de solution inadaptée.

Ce skill **ne fait pas de scoring produit**. Dès qu'il faut comparer et classer des modèles, passer la main à `comparison-content-workflow`.

## 8. Niveau de preuve

Pour chaque élément important, utiliser l'un des statuts :

- `OBSERVED` — comportement ou besoin fourni par une source utilisateur/documentée ;
- `SUPPORTED` — appuyé par plusieurs sources crédibles ;
- `INFERRED` — déduction éditoriale raisonnable depuis des faits vérifiés ;
- `HYPOTHESIS` — hypothèse à confirmer ;
- `UNKNOWN` — information insuffisante.

Ne jamais transformer `INFERRED` ou `HYPOTHESIS` en expérience utilisateur réelle.

## Diagnostic rapide

Avant de considérer l'analyse prête, vérifier :

- le job peut-il être formulé sans nommer le produit ?
- les circonstances sont-elles concrètes ?
- le workflow réel est-il décrit ?
- Push, Pull, Anxiety et Habit sont-ils couverts ?
- les alternatives hors catégorie ont-elles été considérées ?
- les critères découlent-ils du job plutôt que des fiches produits ?
- les hypothèses sont-elles explicitement distinguées des preuves ?
- la page usage peut-elle rester utile sans recommander un modèle précis ?

Si plusieurs réponses sont non, l'analyse n'est pas prête pour la rédaction.

## Attribution

Adaptation éditoriale du skill `jobs-to-be-done` du dépôt public `wondelai/skills`, distribué sous licence MIT. Voir `LICENSE` dans ce dossier.