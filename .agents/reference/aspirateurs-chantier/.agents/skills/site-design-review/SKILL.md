---
name: site-design-review
description: Auditer le design et l’implémentation frontend d’aspirateurs-chantier.fr afin de détecter les défauts UX, les conventions visuelles trop génériques, les problèmes de confiance éditoriale, d’accessibilité et de cohérence. Utiliser pour les audits de pages, composants, captures, previews et pull requests frontend. Pour les pages marques, privilégier le rendu Playwright desktop/mobile et respecter la direction technique définie dans DESIGN.md.
---

# Audit design du site

Effectuer une revue exigeante et contextualisée du frontend. Le but n’est pas de maximiser la décoration, mais de produire un média technique spécialisé crédible, distinctif et utile à la décision.

Avant l’audit, lire `DESIGN.md` et inspecter les composants, styles, générateurs et tokens réellement présents. Si le site peut être lancé, analyser les rendus réels plutôt que le code seul.

## Portée

Déterminer si la demande concerne :

- une page ou un composant ;
- une famille de pages ;
- une pull request ou un diff ;
- une revue globale ;
- une capture d’écran ou une preview ;
- une validation avant publication.

Ne pas étendre l’audit à tout le site lorsqu’une modification locale suffit. Si la demande porte uniquement sur les pages marques, ne pas produire de conclusions sur les comparatifs, guides, usages ou modèles sauf lorsqu’un élément global partagé (header, footer, CSS) explique directement un défaut observé sur les pages marques.

## Vérification visuelle

Une revue frontend complète inclut un rendu réel. Utiliser l’intégration Playwright du dépôt avant de conclure sur le responsive, les débordements, la densité, les états interactifs ou la hiérarchie visuelle.

Pour auditer les pages marques, lire [references/playwright-visual-check.md](references/playwright-visual-check.md), exécuter le script indiqué, puis inspecter les captures générées avec un outil de lecture d’image. Le fichier `report.json` sert de diagnostic complémentaire ; ne pas le traiter comme un jugement esthétique.

Pendant la vérification :

1. lancer le site statique avec les commandes définies par le projet ;
2. examiner au minimum un viewport mobile et un viewport desktop ;
3. parcourir les états interactifs importants, notamment navigation et sommaire ;
4. vérifier le reflow, le focus clavier, les débordements et les contenus tronqués ;
5. vérifier spécialement les tableaux techniques et le comportement de la sidebar ;
6. comparer la page aux règles de `DESIGN.md` ;
7. conserver les captures dans `.artifacts/design-review/`, qui n’est pas versionné.

Si Chromium ne peut pas être installé ou lancé, ne pas présenter la revue comme une validation visuelle complète. Signaler précisément l’échec et limiter les conclusions au code.

## Axes d’audit

### Identité

- La page évoque-t-elle un média technique spécialisé dans les aspirateurs de chantier ?
- La précision des données crée-t-elle l’identité plutôt qu’un décor industriel artificiel ?
- La composition est-elle intentionnelle ou ressemble-t-elle à un assemblage de composants standards ?
- Les différentes marques ont-elles une structure visuelle commune sans devenir le même template éditorial ?

### Signaux de design générique

Chercher les patterns décrits dans la section « Règles anti-design générique / IA » de `DESIGN.md`. Ne pas considérer un pattern isolé comme une preuve. Évaluer leur accumulation, leur manque de justification et leur répétition.

Ne jamais affirmer qu’une interface a été créée par IA. Dire plutôt qu’elle présente des conventions génériques fréquemment observées dans des interfaces générées ou assemblées automatiquement.

### Hiérarchie et UX

- L’angle de la marque est-il immédiatement compréhensible ?
- La différence entre gamme, technologie, classe et modèle est-elle lisible ?
- Les tableaux aident-ils réellement à décider ?
- Le sommaire reflète-t-il les vrais H2 et facilite-t-il la navigation ?
- Les liens vers modèles, usages, comparatifs et guides ont-ils des libellés explicites ?
- La page reste-t-elle utilisable sur petit écran ?

### Confiance éditoriale et affiliation

- La date de vérification et le niveau de preuve sont-ils visibles ?
- Les limites, incompatibilités et précautions sont-elles aussi lisibles que les avantages ?
- L’analyse documentaire est-elle distinguée d’un test physique ?
- Les liens affiliés sont-ils identifiables ?
- Le design crée-t-il une urgence, une note ou une autorité artificielle ?

### Données techniques

- Les classes L/M/H sont-elles compréhensibles sans dépendre uniquement de la couleur ?
- Les tableaux restent-ils lisibles et scrollables sur mobile ?
- Débit, dépression, capacité et autres valeurs sont-ils présentés avec assez de contexte ?
- Les informations techniques dominent-elles excessivement la lecture, ou sont-elles bien hiérarchisées ?

### Craft et accessibilité

- Cohérence des tokens, espacements, rayons, bordures et typographies.
- Contraste, focus, navigation clavier, textes alternatifs et HTML sémantique.
- États hover, focus et active lorsque pertinents.
- Menu mobile réellement fonctionnel.
- Absence de contenu tronqué, de débordement ou de rupture responsive.
- Performance visuelle raisonnable et stabilité du layout.

## Priorisation

Classer les constats :

- **Bloquant** : empêche l’usage, trompe le lecteur ou crée un problème sérieux d’accessibilité/navigation.
- **Majeur** : affaiblit nettement l’identité, la décision ou la crédibilité.
- **Mineur** : défaut local de cohérence ou de finition.
- **Suggestion** : amélioration facultative, dépendante d’un choix créatif.

Ne pas gonfler artificiellement le nombre de constats. Regrouper les symptômes qui proviennent d’une même cause.

## Format de restitution

Commencer par un verdict en deux ou trois phrases.

Puis fournir :

1. **Ce qui fonctionne** : maximum cinq observations concrètes.
2. **Problèmes prioritaires** : tableau avec sévérité, emplacement, preuve, impact et correction recommandée.
3. **Signaux de design générique** : uniquement ceux réellement constatés.
4. **Mobile et accessibilité** : résultats vérifiés et limites de la vérification.
5. **Ordre de correction** : liste courte, du plus important au plus cosmétique.

Citer les fichiers ou composants concernés. Pour une revue visuelle, associer les constats aux captures ou viewports examinés.

## Limites d’action

Un audit reste en lecture seule. Ne modifier le frontend que si l’utilisateur demande explicitement de corriger ou d’implémenter les recommandations.

Le workflow est adapté de `MarcW88/bloc-notes-numerique/.agents/skills/site-design-review`. Les règles propres à `aspirateurs-chantier.fr` dans `DESIGN.md` prévalent.
