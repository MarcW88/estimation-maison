# Maintenance mensuelle depuis le chat

Commande utilisateur : **« Lance la maintenance mensuelle de aspirateurs-chantier »**.

Sans API IA ni service supplémentaire : Actions prépare une file ; l'agent du chat exécute les skills du dépôt. Une Action verte signifie seulement « dossier préparé », jamais « contenu audité ». Pas de cron : lancement à la demande.

## Préparation

Actions → **Prepare monthly content maintenance (chat)** → Run workflow sur main.
Choisir le nombre maximal de pages (10 par défaut), éventuellement des chemins séparés par des virgules.
Le résumé et l'artefact contiennent `plan.json` et `handoff.md`.
Si le chat ne dispose pas d'une capacité de déclenchement Actions, exécuter exactement le même préparateur dans son checkout :

```bash
python scripts/maintenance_orchestrator.py prepare
python scripts/maintenance_orchestrator.py prepare --urls /guides/classes-l-m-h/ --max-pages 1
```

L'inventaire parcourt les vrais `index.html`, y compris les produits imbriqués. Les cinq index de cluster sont exclus par défaut (réactivables via overrides). Les cinq clusters routent vers leurs paires de workflows existantes. Homepage, accessoires et pages de confiance restent hors maintenance automatique : aucun workflow spécialisé n'est inventé. Modifier les cadences dans `maintenance.config.json`. `overrides` permet une cadence ou `enabled: false` par URL.

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
{"pages": [{"url": "/guides/classes-l-m-h/", "reviewed_at": "2026-09-30", "decision": "KEEP", "audit_report": ".content/reviews/maintenance-classes-l-m-h-2026-09-30.md"}]}
```

Seules les pages réellement terminées sont enregistrées. Les restantes reviennent au prochain lot. Le registre et l'historique doivent être inclus dans la PR, même pour KEEP. Leur persistance nécessite le merge de cette PR.

4. KEEP : aucune modification éditoriale. LIGHT_UPDATE/DEEP_REWRITE : lire et exécuter le content-workflow indiqué, préserver la valeur et limiter le scope. MERGE/NOINDEX : rapport pour décision humaine ; aucune suppression, redirection ou modification robots automatique.
5. Mettre à jour les sources de génération et registres utilisés par le content-workflow, pas uniquement le HTML susceptible d'être écrasé. Exécuter sa chaîne de génération/QA existante puis le validateur indiqué et le même analysis-workflow en PUBLISH_REVIEW. Conserver les preuves de résultat. Ne pas lancer aveuglément les autres générateurs.
6. Ouvrir une branche et une PR incluant corrections, rapports, registre et historique : motif, fichiers, sources, validations et éléments attendant validation humaine. Conserver canonical, URL et état d'indexation. PASS machine ne remplace pas `PASS — READY_FOR_HUMAN_VALIDATION`. Pas de publication automatique.

Aucun audit n'est exécuté ni simulé par le script : les SKILL.md nécessitent l'agent du chat. La préparation est reproductible et n'utilise que Python standard. Aucun secret modèle à configurer.

## Particularités aspirateurs-chantier

`/modeles/` est **audit_only** : suivre model-analysis-workflow, conserver un handoff et les preuves. Ne pas modifier les pages modèles ni `_generate_model_overrides.py` ; le workflow actuel prévoit une migration séparée du renderer. Le registre route les mises à jour modèles vers HUMAN_DECISION.

Pour les autres clusters, suivre leurs vraies sources de contenu : notamment les fragments `.content/guides/v2/`, `.content/usages/v2/`, `.content/comparisons/v2/` et leurs render-map lorsque présents. Ne jamais fabriquer un run-evidence v2 ou un PASS avec un générateur.

Les commandes du plan sont des précontrôles, pas la totalité de la QA. Lire impérativement le workflow de la page :
- guides : validate_guide_workflow.py et validate_guide_quality.py ;
- usages : validate_usage_workflow.py ;
- marques : validate_brand_skill_stack.py, validate_brand_run_evidence.py --slug <slug> --require-run, puis _validate_brands.py ;
- comparatifs : validate_comparison_skill_stack.py et validate_comparison_run_evidence.py --slug <slug> --require-run, plus QA du renderer applicable ;
- modèles (audit seulement) : validate_model_skill_stack.py ; validate_model_run_evidence.py --slug <slug> --require-run si un draft est revu.

Vérifier particulièrement classe L/M/H, certification, poussières dangereuses, silice, amiante, ATEX, variantes et compatibilités. Aucun claim de sécurité déduit d'une simple spec ou du nom commercial. Absence de preuve = UNKNOWN. Une disponibilité ou un prix exige une vérification actuelle.
