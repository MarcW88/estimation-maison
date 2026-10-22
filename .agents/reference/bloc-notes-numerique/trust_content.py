"""Verified trust-page copy for the footer transparency section.

Only pages whose institutional claims can be supported by repository evidence are
included here. ABOUT, CONTACT and LEGAL remain intentionally untouched until
owner-confirmed data is available.
"""

TRUST_CONTENT = {
    "/methode-de-test/": r'''
      <p class="article-answer"><strong>Tous les produits présentés sur ce site ne sont pas automatiquement considérés comme « testés ».</strong> Une observation physique, une information issue d'un fabricant et une conclusion éditoriale n'ont pas le même niveau de preuve. Lorsque nous ne disposons pas d'une expérience directe documentée, nous parlons d'analyse documentaire et nous évitons de transformer cette analyse en faux test produit.</p>

      <h2 id="principe">Le principe : dire sur quoi repose chaque conclusion</h2>
      <p>Notre objectif n'est pas de donner l'apparence d'un laboratoire. Il est de rendre le raisonnement vérifiable. Une caractéristique technique peut être confirmée par une documentation officielle ; une compatibilité peut nécessiter plusieurs sources ; un avis sur l'adéquation à un usage reste un jugement éditorial construit à partir de critères explicites.</p>
      <p>Cette distinction est importante pour les bloc-notes numériques : une fiche technique permet de vérifier une taille d'écran, un format d'export ou l'existence d'un abonnement, mais elle ne permet pas à elle seule d'affirmer qu'un stylet « semble naturel », qu'une latence est imperceptible ou qu'un appareil reste agréable sur la durée.</p>

      <h2 id="preuves">Nos niveaux de preuve</h2>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Niveau</th><th>Ce qu'il signifie</th><th>Ce que nous pouvons écrire</th></tr></thead>
        <tbody>
          <tr><td><strong>Observation directe</strong></td><td>Une action ou un test a réellement été effectué et documenté.</td><td>Une observation de comportement peut être décrite, avec son contexte et ses limites.</td></tr>
          <tr><td><strong>Source officielle</strong></td><td>Fabricant, documentation, manuel, page de support ou politique officielle identifiable.</td><td>Une caractéristique ou une règle peut être présentée comme confirmée à la date de consultation.</td></tr>
          <tr><td><strong>Source secondaire étayée</strong></td><td>Une information est recoupée par une source tierce crédible lorsque la source primaire ne suffit pas.</td><td>La conclusion est attribuée et reste distincte d'une expérience personnelle.</td></tr>
          <tr><td><strong>Inférence éditoriale</strong></td><td>Plusieurs faits vérifiés conduisent à une conclusion utile pour un usage donné.</td><td>Nous présentons la conclusion comme une analyse, pas comme un fait mesuré.</td></tr>
          <tr><td><strong>Information inconnue</strong></td><td>Une donnée importante n'est pas vérifiée ou les sources se contredisent.</td><td>Nous signalons l'incertitude ou nous retirons la revendication.</td></tr>
        </tbody>
      </table></div>

      <h2 id="sources">Quelles sources privilégions-nous ?</h2>
      <p>Pour les caractéristiques susceptibles d'influencer une décision d'achat, la priorité va aux sources primaires : pages produit officielles, manuels, documentation de support, politiques d'abonnement et informations de compatibilité publiées par les fabricants. Les prix et disponibilités sont datés lorsqu'ils sont utilisés, car ils peuvent changer rapidement.</p>
      <p>Une source constructeur n'est toutefois pas traitée comme une preuve de supériorité. Elle peut confirmer qu'une fonction existe ; elle ne suffit pas à conclure qu'elle est meilleure que celle d'un concurrent. Les comparaisons exigent une grille commune et des preuves comparables.</p>

      <h2 id="analyse">Ce qu'une analyse documentaire peut réellement évaluer</h2>
      <p>Sans test physique documenté, nous pouvons néanmoins examiner de nombreux éléments utiles : formats pris en charge, méthodes d'import et d'export, synchronisation, cloud, applications disponibles, abonnements, accessoires indispensables, dimensions, taille d'écran, fonctions d'annotation, politiques de support, disponibilité et coût total d'une configuration.</p>
      <p>Ces informations permettent notamment de répondre à des questions de workflow : l'appareil peut-il annoter le type de PDF utilisé ? Les notes peuvent-elles être exportées ? Un abonnement est-il nécessaire pour une fonction importante ? Un écosystème fermé bloque-t-il une application indispensable ?</p>

      <h2 id="limites">Ce que nous ne déduisons pas d'une fiche technique</h2>
      <p>Nous ne devons pas transformer une donnée constructeur en sensation d'usage. Sans observation directe, nous évitons notamment de prétendre mesurer la sensation du stylet, la fatigue après une longue session, la fiabilité à long terme, le confort réel d'une interface ou la qualité d'un support client dans une situation concrète.</p>
      <p>De même, une autonomie annoncée par un fabricant reste une autonomie annoncée. Elle ne devient pas « notre autonomie mesurée » parce qu'elle est reprise dans une page.</p>

      <h2 id="comparaisons">Comment cette méthode alimente les comparatifs</h2>
      <p>Les pages comparatives utilisent une étape supplémentaire : les critères sont définis avant le classement, les preuves sont enregistrées avant le scoring et les poids sont fixés selon l'intention de la page. Un produit ne devient donc pas « meilleur » simplement parce qu'il possède davantage de fonctionnalités ou parce qu'un lien affilié existe.</p>
      <p>La page <a href="/comment-nous-comparons/">Comment nous comparons les produits</a> détaille cette logique de scoring, les données manquantes, les critères éliminatoires et le traitement du coût total.</p>

      <h2 id="mise-a-jour">Fact-check, mises à jour et corrections</h2>
      <p>Les informations susceptibles d'évoluer sont vérifiées au moment de la production ou de la révision d'une page. Une nouvelle génération de produit, un changement de tarif, une modification d'abonnement, une fonction ajoutée ou retirée, ou une source devenue obsolète peuvent déclencher une réévaluation.</p>
      <p>Nous ne revendiquons pas une fréquence fixe de révision pour toutes les pages. Le principe est plutôt de conserver la date et le niveau de preuve des informations instables et de corriger une conclusion lorsque les données qui la soutiennent changent.</p>

      <h2 id="limite-generale">La limite la plus importante de cette méthode</h2>
      <p>Une méthode structurée réduit les affirmations gratuites, mais elle ne transforme pas une analyse documentaire en expérience de terrain. Lorsque l'usage réel d'un appareil devient décisif et qu'aucune observation directe n'est disponible, la conclusion doit rester plus prudente. Nous préférons afficher cette limite plutôt que combler le manque par une expérience inventée.</p>
    ''',

    "/comment-nous-comparons/": r'''
      <p class="article-answer"><strong>Nos comparatifs suivent un ordre volontairement contraignant : critères avant gagnant, preuves avant scoring, scoring avant rédaction.</strong> Le produit classé premier doit découler de la grille de décision ; la grille ne doit pas être ajustée après coup pour justifier un produit déjà choisi.</p>

      <h2 id="intention">1. Nous commençons par la décision à prendre</h2>
      <p>« Meilleur bloc-notes numérique », « meilleur modèle pour étudiant » et « meilleur modèle sans abonnement » ne posent pas la même question. Avant de sélectionner les produits, nous définissons donc l'intention, les contraintes et le résultat recherché.</p>
      <p>Cette étape détermine les critères qui comptent réellement. Pour un étudiant, l'annotation de PDF, l'organisation, le coût total ou l'export peuvent peser davantage. Pour un usage professionnel, les intégrations, la confidentialité, les workflows de documents ou la fiabilité des exports peuvent changer la décision.</p>

      <h2 id="univers">2. Nous construisons l'univers produit avant de choisir les gagnants</h2>
      <p>Les produits éligibles sont recensés avant le classement. Un modèle peut être retenu, retenu sous conditions, considéré comme obsolète, non comparable ou exclu. Une exclusion doit avoir une raison : génération dépassée, disponibilité insuffisante, fonction indispensable absente, produit appartenant à une autre catégorie fonctionnelle ou données essentielles impossibles à vérifier.</p>
      <p>Un produit ne doit pas être ajouté uniquement parce qu'il existe un programme d'affiliation, et l'absence de lien affilié n'est pas en soi un motif d'exclusion.</p>

      <h2 id="equivalence">3. Nous vérifions que les produits sont réellement comparables</h2>
      <p>Deux appareils peuvent partager un écran E Ink tout en répondant à des usages très différents. Nous regardons donc le job-to-be-done, le format, les fonctions clés, le logiciel, les accessoires nécessaires, les coûts récurrents et les contraintes d'écosystème.</p>
      <p>Lorsque la comparaison n'est que partielle, la page doit l'expliquer au lieu de mettre artificiellement deux produits sur un pied d'égalité.</p>

      <h2 id="preuves">4. Aucun score avant le registre de preuves</h2>
      <p>Chaque critère important doit être rattaché à une information vérifiée, étayée, inférée ou explicitement inconnue. Une note sans justification n'est pas suffisante.</p>
      <div class="table-wrapper"><table class="comp-table">
        <thead><tr><th>Classe de preuve</th><th>Usage dans le comparatif</th></tr></thead>
        <tbody>
          <tr><td><strong>Vérifié</strong></td><td>Source primaire actuelle : documentation, manuel, support ou page officielle.</td></tr>
          <tr><td><strong>Étayé</strong></td><td>Source secondaire crédible lorsque la source primaire ne suffit pas.</td></tr>
          <tr><td><strong>Inféré</strong></td><td>Conclusion raisonnable construite à partir de plusieurs faits, sans la présenter comme une mesure directe.</td></tr>
          <tr><td><strong>Observation directe</strong></td><td>Utilisée uniquement lorsqu'un vrai test ou une observation est effectivement documenté.</td></tr>
          <tr><td><strong>Inconnu</strong></td><td>Une donnée non vérifiée ne peut pas soutenir silencieusement un critère déterminant.</td></tr>
        </tbody>
      </table></div>

      <h2 id="criteres">5. Les critères et leurs poids sont fixés avant le classement</h2>
      <p>Les critères viennent de l'intention et des différences susceptibles de changer la décision : écriture, annotation PDF, export, organisation, cloud, applications, taille, couleur, autonomie annoncée, simplicité, coût total, abonnement, accessoires ou disponibilité, selon la page.</p>
      <p>Les poids sont ensuite définis avant le calcul et leur somme vaut 100. Ils peuvent varier d'un comparatif à l'autre parce que l'usage varie ; ils ne doivent pas être modifiés simplement parce qu'un autre produit gagne.</p>

      <h2 id="scoring">6. Comment fonctionne le scoring ?</h2>
      <p>Le workflow utilise une échelle stable, typiquement de 0 à 10 par critère. Chaque note conserve une justification et son niveau de preuve. Le score pondéré d'un critère correspond à la note normalisée multipliée par son poids ; le total combine ensuite les critères pondérés.</p>
      <p>Le score n'est donc pas une mesure scientifique universelle. C'est une façon structurée de rendre visible un arbitrage éditorial. Sa valeur vient surtout de la transparence des critères, des poids et des preuves.</p>

      <h2 id="hard-gates">7. Certains critères sont éliminatoires</h2>
      <p>Une bonne moyenne ne doit pas masquer une incompatibilité fondamentale. Un produit peut être écarté s'il n'est pas disponible, si une fonction indispensable manque, si sa génération est obsolète, si les données essentielles sont invérifiables, si le prix dépasse une contrainte explicite ou si un abonnement obligatoire contredit directement l'intention de la page.</p>
      <p>Ces « hard gates » évitent qu'un produit très bien noté sur des critères secondaires gagne malgré une limite rédhibitoire.</p>

      <h2 id="cout-total">8. Nous comparons le coût de la solution, pas seulement le prix nu</h2>
      <p>Lorsque le prix influence la décision, nous cherchons à comparer des configurations réellement utilisables : appareil, accessoire obligatoire, protection nécessaire, abonnement utile et autres coûts indispensables. Un appareil nu ne devrait pas sembler artificiellement moins cher qu'un concurrent vendu avec le stylet ou l'accessoire nécessaire à l'usage évalué.</p>

      <h2 id="donnees-manquantes">9. Que faisons-nous des données manquantes ?</h2>
      <p>Une donnée manquante n'est pas automatiquement remplacée par une estimation. Si elle est secondaire, l'incertitude peut être signalée. Si elle porte sur un critère déterminant, elle peut réduire le niveau de confiance ou empêcher le produit de gagner tant que l'information n'est pas suffisamment vérifiée.</p>

      <h2 id="commission">10. Les commissions n'entrent pas dans le classement</h2>
      <p>Le niveau de commission d'un marchand ou d'un programme d'affiliation n'est pas un critère de scoring. Il ne doit pas modifier l'inclusion d'un produit, sa note, sa position ou la manière dont ses défauts sont formulés.</p>
      <p>Le rôle de l'affiliation est expliqué séparément dans notre page <a href="/transparence-affiliation/">Transparence affiliation</a>.</p>

      <h2 id="mise-a-jour">11. Pourquoi un classement peut-il changer ?</h2>
      <p>Un classement peut évoluer si les données changent : nouveau modèle, produit retiré du marché, prix structurel différent, abonnement modifié, fonction ajoutée ou supprimée, nouvelle source plus solide ou correction d'une erreur. Il peut aussi changer si une méthodologie est corrigée, mais ce changement doit être documenté au lieu d'être utilisé pour forcer un gagnant.</p>
      <p>Nous ne revendiquons pas une fréquence de révision identique pour tous les comparatifs. Les mises à jour sont liées aux changements de données et aux révisions éditoriales nécessaires.</p>

      <h2 id="limites">12. Ce qu'un classement ne dit pas</h2>
      <p>Un « meilleur » produit est toujours le meilleur au regard d'une intention, de critères et de données disponibles à un moment donné. Il ne devient pas universellement supérieur pour tous les lecteurs.</p>
      <p>C'est pourquoi chaque recommandation doit également exposer sa principale limite, les profils pour lesquels elle convient moins bien et l'alternative logique lorsque le critère décisif change.</p>

      <p>Pour comprendre la différence entre observation directe, sources et analyse documentaire, consultez aussi <a href="/methode-de-test/">notre méthode d'évaluation</a>.</p>
    ''',

    "/transparence-affiliation/": r'''
      <p class="article-answer"><strong>Certains liens présents sur ce site sont des liens affiliés.</strong> Lorsqu'une transaction éligible est réalisée après un clic sur l'un de ces liens, le site peut recevoir une commission. Cette rémunération ne doit pas entrer dans les critères de scoring ou de classement des produits.</p>

      <h2 id="definition">Qu'est-ce qu'un lien affilié ?</h2>
      <p>Un lien affilié contient généralement un identifiant permettant au marchand ou à une plateforme d'attribution de savoir qu'une visite provient de ce site. Si les conditions du programme sont remplies, une commission peut ensuite être attribuée au site.</p>
      <p>Nous n'affirmons pas que tous les liens vers des marchands sont affiliés. Un produit ou une source peut être cité même lorsqu'aucune rémunération n'est possible.</p>

      <h2 id="classement">La commission influence-t-elle les classements ?</h2>
      <p>Non dans la méthodologie du site : le niveau de commission ne fait pas partie des critères utilisés pour noter ou classer un produit. Les comparatifs doivent commencer par l'intention, les critères et les preuves, puis calculer le scoring avant de traiter la couche d'affiliation.</p>
      <p>De la même manière, un produit ne doit pas être exclu uniquement parce qu'il ne dispose pas de lien affilié. Une recommandation doit rester utile si tous les liens commerciaux sont retirés.</p>

      <h2 id="prix">Les liens affiliés changent-ils le prix ?</h2>
      <p>Le prix final, la disponibilité, les frais et les conditions de vente sont déterminés par le marchand. Nous évitons donc de promettre qu'un lien affilié « ne coûte rien » ou garantit exactement le même prix dans toutes les situations.</p>
      <p>Lorsqu'un prix est cité dans une page, il doit être daté s'il est susceptible d'évoluer. Pour les promotions, le site utilise en plus un registre de preuve et distingue les offres vérifiées, les prix à surveiller, les ruptures et les offres expirées.</p>

      <h2 id="liens">Comment les liens commerciaux sont-ils signalés ?</h2>
      <p>Les contenus du site distinguent l'information éditoriale de l'action commerciale. Les liens affiliés doivent utiliser l'attribut <code>rel="sponsored"</code> lorsque cette qualification s'applique, et la présence d'affiliation est rappelée dans l'interface et dans cette page.</p>

      <h2 id="sans-affiliation">Et si un produit n'a pas de programme d'affiliation ?</h2>
      <p>L'absence de programme d'affiliation ne constitue pas un motif suffisant pour retirer un produit pertinent d'un comparatif. L'univers produit doit être construit avant le classement, en fonction de la catégorie, de la disponibilité, de la comparabilité et des besoins de l'utilisateur.</p>

      <h2 id="inconnues">Ce que nous ne prétendons pas encore</h2>
      <p>Cette page ne publie pas encore une liste de programmes d'affiliation actifs, car cette liste doit être confirmée avant d'être présentée comme exhaustive. Nous ne formulons pas non plus, à ce stade, de promesse générale concernant les produits prêtés ou offerts, les contenus sponsorisés ou l'existence de relations commerciales directes avec des marques.</p>
      <p>Ces points sont volontairement laissés explicites plutôt que remplis par supposition. Si un produit est prêté, offert, fourni avec un accès presse ou intégré à une opération sponsorisée, cette relation devra être documentée et signalée avant que le contenu concerné puisse être présenté comme conforme à cette politique.</p>

      <h2 id="bons-plans">Une promotion peut-elle modifier une recommandation ?</h2>
      <p>Une baisse de prix peut rendre une offre plus intéressante, mais elle ne transforme pas automatiquement le produit en meilleur choix absolu. Les pages <a href="/bons-plans/">Bons plans</a> évaluent l'offre et sa fraîcheur ; les pages <a href="/comparatifs/">Comparatifs</a> évaluent le produit au regard de critères et d'un usage.</p>

      <h2 id="methode">Notre règle de séparation</h2>
      <p>Le principe utilisé dans le dépôt est simple : <strong>critères avant gagnant, preuves avant scoring, scoring avant rédaction, affiliation après décision.</strong> Cette séparation n'élimine pas le modèle économique du site ; elle vise à empêcher qu'il décide silencieusement du contenu.</p>

      <p>Pour voir comment cette règle est appliquée aux classements, consultez <a href="/comment-nous-comparons/">Comment nous comparons les produits</a>.</p>
    ''',
}

TRUST_PAGE_META = {
    "/methode-de-test/": {
        "title": "Notre méthode d'évaluation des bloc-notes numériques",
        "description": "Comment nous distinguons tests physiques, sources officielles, analyse documentaire et inférences éditoriales.",
        "status_label": "Méthode documentée — 9 septembre 2026",
    },
    "/comment-nous-comparons/": {
        "title": "Comment nous comparons les bloc-notes numériques",
        "description": "Critères, preuves, pondération, scoring, données manquantes et rôle de l'affiliation dans nos comparatifs.",
        "status_label": "Méthode documentée — 9 septembre 2026",
    },
    "/transparence-affiliation/": {
        "title": "Transparence sur l'affiliation",
        "description": "Comment fonctionnent les liens affiliés du site, ce qu'ils peuvent financer et pourquoi les commissions n'entrent pas dans nos classements.",
        "status_label": "Politique documentée — 9 septembre 2026",
    },
}
