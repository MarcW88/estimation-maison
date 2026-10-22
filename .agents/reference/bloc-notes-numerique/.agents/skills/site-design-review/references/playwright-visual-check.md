# Vérification visuelle avec Playwright

## Installation

Depuis la racine du dépôt :

```bash
npm install
npm run visual:install
```

La seconde commande télécharge la version de Chromium attendue par la version de Playwright verrouillée dans `package-lock.json`.

## Audits par catégorie

Les scopes disponibles sont :

```bash
npm run visual:brands
npm run visual:comparisons
npm run visual:usages
npm run visual:guides
npm run visual:deals
```

Chaque commande lance le site statique localement, visite toutes les routes du scope en desktop (1440 × 1000) et mobile (390 × 844), puis écrit dans `.artifacts/design-review/` :

- une capture pleine page par URL et viewport ;
- une capture du menu mobile ouvert pour la première route ;
- `report.json`, avec les erreurs console/page, débordements horizontaux, titres du sommaire, dimensions de sidebar, tableaux, liens éditoriaux et présence d’un `article-answer` lorsqu’il existe.

Pour Guides et Bons plans, le rapport contrôle aussi les éléments utiles à leur design éditorial : placement responsive du sommaire, tableaux restant sans wrapper et visibilité du premier lien éditorial.

Inspecter les captures avec un outil de lecture d’image. Le rapport automatique aide à trouver les pages à regarder en priorité, mais ne remplace pas le jugement visuel.

## Routes ponctuelles

Pour limiter le contrôle à une ou plusieurs pages :

```bash
node .agents/skills/site-design-review/scripts/run-visual-review.mjs \
  --route /guides/choisir-bloc-notes-numerique/ \
  --route /bons-plans/black-friday/
```

Options utiles :

- `--scope brands|comparisons|usages|guides|deals` contrôle toute une catégorie ;
- `--base-url https://example.com` contrôle un déploiement existant sans lancer le serveur local ;
- `--output chemin` change le dossier des captures ;
- `--port 4173` change le port du serveur local.

Le script renvoie un code non nul seulement en cas d’échec technique empêchant le contrôle. Les constats de design restent à qualifier dans l’audit.

## Exécution dans GitHub

Le workflow `.github/workflows/visual-design-review.yml` lance les cinq scopes sur les pull requests et les pushes `main` qui touchent les pages ou styles concernés. Les captures et rapports sont publiés pendant 14 jours dans les artifacts :

- `brands-design-review`
- `comparisons-design-review`
- `usages-design-review`
- `guides-design-review`
- `deals-design-review`
