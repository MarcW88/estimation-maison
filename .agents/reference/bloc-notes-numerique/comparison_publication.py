"""Explicit publication/indexation state for comparison pages.

Only routes listed here may be switched to index,follow by the comparison
publication step. New comparison pages must remain noindex until they complete
PUBLISH_REVIEW, receive human validation, and are explicitly approved for
indexation.

Human indexation approval recorded: 2026-09-09.
"""

INDEXABLE_COMPARISON_ROUTES = {
    "/comparatifs/",
    "/comparatifs/meilleur-bloc-notes-numerique/",
    "/comparatifs/tablette-e-ink/",
    "/comparatifs/bloc-notes-numerique-professionnel/",
    "/comparatifs/bloc-notes-numerique-etudiant/",
    "/comparatifs/bloc-notes-numerique-couleur/",
    "/comparatifs/bloc-notes-numerique-a4/",
    "/comparatifs/bloc-notes-numerique-sans-abonnement/",
    "/comparatifs/bloc-notes-numerique-pas-cher/",
    "/comparatifs/kindle-scribe-vs-remarkable/",
    "/comparatifs/kindle-scribe-vs-kobo-elipsa/",
    "/comparatifs/remarkable-vs-boox/",
    "/comparatifs/remarkable-vs-supernote/",
    "/comparatifs/boox-vs-supernote/",
    "/comparatifs/kobo-elipsa-vs-remarkable/",
}
