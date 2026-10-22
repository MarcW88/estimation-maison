# Maintenance mensuelle depuis le chat

Commande utilisateur : **« Lance la maintenance mensuelle de bloc-notes-numerique »**.

Sans API IA ni service supplémentaire : Actions prépare une file ; l'agent du chat exécute les skills du dépôt. Une Action verte signifie seulement « dossier préparé », jamais « contenu audité ». Pas de cron : lancement à la demande.

## Préparation

Actions → **Prepare monthly content maintenance (chat)** → Run workflow sur main.
Choisir le nombre maximal de pages (10 par défaut), éventuellement des chemins séparés par des virgules.
Le résumé et l'artefact contiennent `plan.json` et `handoff.md`.
Si le chat ne dispose pas d'une capacité de déclenchement Actions, exécuter exactement le même préparateur dans son checkout :

```bash
python scripts/maintenance_orchestrator.py prepare
python scripts/maintenance_orchestrator.py prepare --urls /guides/ocr-manuscrit/ --max-pages 1
```

L'inventaire parcourt les vrais `index.html`, y compris les produits imbriqués. Les cinq index de cluster sont exclus par défaut (réactivables via overrides). Les cinq clusters routent vers leurs paires de workflows existantes. Homepage, boutique, accessoires et pages de confiance restent hors maintenance automatique : aucun workflow spécialisé n'est inventé. Modifier les cadences dans `maintenance.config.json`. `overrides` permet une cadence ou `enabled: false` par URL.

Les pages jamais auditées dans ce registre, arrivées à échéance ou modifiées depuis l'audit sont candidates. La rotation entre clusters évite qu'un cluster monopolise le lot. Les dates des anciens rapports ne sont pas importées automatiquement comme preuve d'un nouvel audit. Préparer un lot ne change aucune date d'audit. Ni âge ni empreinte ne prouvent une erreur factuelle ou un besoin de réécriture.

## Exécution par l'agent du chat

1. Lire `AGENTS.md`, le plan, puis le SKILL.md d'analyse indiqué et les skills spécialisés qu'il appelle. Utiliser AUDIT ; comparer les pages voisines selon ce workflow ; vérifier les faits instables avec des sources actuelles. Données GSC/SERP absentes = inconnues, pas inventées.
2. Sauver un vrai rapport par page dans `.content/reviews/` : décision, preuves et dates, incertitudes, blockers, valeur à préserver, scope et prochaine étape.
3. Enregistrer les audits **avant** de modifier les pages (l'empreinte est celle de la version auditée) :

```bash
python scripts/maintenance_orchestrator.py record --plan .artifacts/maintenance/plan.json --results .artifacts/maintenance/results.json
```

Format `results.json` :

```json
{"pages": [{"url": "/guides/ocr-manuscrit/", "reviewed_at": "2026-09-30", "decision": "KEEP", "audit_report": ".content/reviews/maintenance-ocr-2026-09-30.md"}]}
```

Seules les pages réellement terminées sont enregistrées. Les restantes reviennent au prochain lot. Le registre et l'historique doivent être inclus dans la PR, même pour KEEP. Leur persistance nécessite le merge de cette PR.

4. KEEP : aucune modification éditoriale. LIGHT_UPDATE/DEEP_REWRITE : lire et exécuter le content-workflow indiqué, préserver la valeur et limiter le scope. MERGE/NOINDEX : rapport pour décision humaine ; aucune suppression, redirection ou modification robots automatique.
5. Mettre à jour les sources de génération et registres utilisés par le content-workflow, pas uniquement le HTML susceptible d'être écrasé. Exécuter sa chaîne de génération/QA existante puis le validateur indiqué et le même analysis-workflow en PUBLISH_REVIEW. Conserver les preuves de résultat. Ne pas lancer aveuglément les autres générateurs.
6. Ouvrir une branche et une PR incluant corrections, rapports, registre et historique : motif, fichiers, sources, validations et éléments attendant validation humaine. Conserver canonical, URL et état d'indexation. PASS machine ne remplace pas `PASS — READY_FOR_HUMAN_VALIDATION`. Pas de publication automatique.

Aucun audit n'est exécuté ni simulé par le script : les SKILL.md nécessitent l'agent du chat. La préparation est reproductible et n'utilise que Python standard. Aucun secret modèle à configurer.
