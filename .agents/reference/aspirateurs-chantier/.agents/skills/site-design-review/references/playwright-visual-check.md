# Vérification visuelle avec Playwright

## Installation

Depuis la racine du dépôt :

```bash
npm ci
npm run visual:install
```

La seconde commande télécharge la version de Chromium attendue par Playwright 1.63.0 verrouillé dans `package-lock.json`.

## Audit des pages marques

```bash
npm run visual:brands
```

Le script lance le site statique localement et visite exclusivement :

- `/marques/` ;
- `/marques/bosch/` ;
- `/marques/karcher/` ;
- `/marques/makita/` ;
- `/marques/festool/` ;
- `/marques/dewalt/` ;
- `/marques/parkside/` ;
- `/marques/nilfisk/` ;
- `/marques/mirka/`.

Il contrôle chaque route en desktop et mobile puis écrit dans `.artifacts/design-review/` :

- une capture pleine page par URL et viewport ;
- une capture du menu Marques ouvert en desktop ;
- une capture après clic sur le burger en mobile ;
- `report.json`, avec erreurs console, débordements, tableaux, H2/ancres du sommaire, sidebar, answer-box, images et état de navigation mobile.

Inspecter les captures avec un outil de lecture d’image. Le rapport automatique aide à trouver les pages à regarder en priorité, mais ne remplace pas le jugement visuel.

## Routes ponctuelles

Pour limiter le contrôle à une ou plusieurs pages :

```bash
node .agents/skills/site-design-review/scripts/run-visual-review.mjs \
  --route /marques/bosch/ \
  --route /marques/festool/
```

Options utiles :

- `--base-url https://example.com` contrôle un déploiement existant sans lancer le serveur local ;
- `--output chemin` change le dossier des captures ;
- `--port 4173` change le port du serveur local.

Le script renvoie un code non nul seulement en cas d’échec technique empêchant le contrôle. Les constats de design restent à qualifier dans l’audit.

## Exécution dans GitHub

Le workflow `.github/workflows/visual-design-review.yml` lance le même contrôle uniquement pour le scope marques. Il peut être déclenché sur pull request, push vers `main` ou manuellement. Les captures et le rapport sont disponibles dans l’artifact `brand-design-review` pendant 14 jours.
