---
name: site-design-review
description: Auditer le design et l’implémentation frontend de bloc-notes-numeriques.fr afin de détecter les interfaces génériques ou manifestement générées par IA, les défauts UX, les problèmes de confiance éditoriale, d’accessibilité et de cohérence. Utiliser pour les audits de pages, composants, captures, previews et pull requests frontend. Ne pas utiliser pour les contenus SEO seuls ou le backend sans interface.
---

# Audit design du site

Effectuer une revue exigeante et contextualisée du frontend. Le but n’est pas de maximiser la décoration, mais de produire un média spécialisé crédible, distinctif et utile.

Avant l’audit, lire `DESIGN.md` et inspecter les composants, styles et tokens réellement présents. Si le site peut être lancé, analyser les rendus réels plutôt que le code seul.

## Portée

Déterminer si la demande concerne :

- une page ou un composant ;
- une pull request ou un diff ;
- une revue globale ;
- une capture d’écran ou une preview ;
- une validation avant publication.

Ne pas étendre l’audit à tout le site lorsqu’une modification locale suffit.

## Vérification visuelle

Une revue frontend complète inclut un rendu réel. Utiliser l’intégration Playwright du dépôt avant de conclure sur le responsive, les débordements, la densité, les états interactifs ou la hiérarchie visuelle.

Pour auditer les pages marques ou lancer des routes précises, lire [references/playwright-visual-check.md](references/playwright-visual-check.md), exécuter le script indiqué, puis inspecter les captures générées avec un outil de lecture d’image. Le fichier `report.json` sert de diagnostic complémentaire ; ne pas le traiter comme un jugement esthétique.

Pendant la vérification :

1. lancer le site avec les commandes définies par le projet ;
2. examiner au minimum un viewport mobile et un viewport desktop ;
3. parcourir les états interactifs importants ;
4. vérifier le reflow, le focus clavier, les débordements et les contenus tronqués ;
5. comparer la page aux règles de `DESIGN.md` ;
6. conserver les captures dans `.artifacts/design-review/`, qui n’est pas versionné.

Si Chromium ne peut pas être installé ou lancé, ne pas présenter la revue comme une validation visuelle complète. Signaler précisément l’échec et limiter les conclusions au code.

## Axes d’audit

### Identité

- La page évoque-t-elle un média éditorial consacré au papier numérique ?
- Possède-t-elle une direction reconnaissable sans copier une marque ?
- La composition est-elle intentionnelle ou ressemble-t-elle à un assemblage de composants standards ?

### Signes de génération automatique

Chercher les patterns décrits dans la section « Règles anti-design IA » de `DESIGN.md`. Ne pas considérer un pattern isolé comme une preuve. Évaluer leur accumulation, leur manque de justification et leur répétition.

Ne jamais affirmer qu’une interface a été créée par IA. Dire plutôt qu’elle présente des conventions génériques fréquemment observées dans des interfaces générées ou assemblées automatiquement.

### Hiérarchie et UX

- L’objectif de la page est-il immédiatement compréhensible ?
- L’action principale est-elle claire sans écraser le contenu ?
- Les comparaisons permettent-elles une décision réelle ?
- La navigation, les filtres et les liens ont-ils des libellés explicites ?
- La page reste-t-elle utilisable sur petit écran ?

### Confiance éditoriale et affiliation

- Le niveau de preuve est-il visible ?
- Les avantages et limites sont-ils équilibrés ?
- Les liens affiliés sont-ils identifiables ?
- Les prix et dates de vérification sont-ils contextualisés ?
- Le design crée-t-il une urgence ou une autorité artificielle ?

### Craft et accessibilité

- Cohérence des tokens, espacements, rayons, bordures et typographies.
- Contraste, focus, navigation clavier, textes alternatifs et HTML sémantique.
- États hover, focus, active, loading, empty et error lorsque pertinents.
- Absence de contenu tronqué, de débordement ou de rupture responsive.
- Performance visuelle raisonnable : images adaptées, mouvements limités et stabilité du layout.

## Priorisation

Classer les constats :

- **Bloquant** : empêche l’usage, trompe le lecteur ou crée un problème sérieux d’accessibilité.
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

Un audit reste en lecture seule. Ne modifier le code que si l’utilisateur demande explicitement de corriger ou d’implémenter les recommandations.

Sources d’inspiration méthodologique : Microsoft Frontend Design Review et Impeccable. Les règles propres au projet dans `DESIGN.md` prévalent.
