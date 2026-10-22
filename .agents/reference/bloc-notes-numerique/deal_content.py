"""Editorial bodies for /bons-plans/ pages.

Current price/deal claims are backed by .content/deals/*.json.
Do not edit a live offer in prose without updating its evidence record first.
"""

DEAL_STATUS_LABEL = {
    "/bons-plans/bloc-notes-numerique/": "Offres vérifiées le 10 septembre 2026",
    "/bons-plans/remarkable/": "Offres vérifiées le 10 septembre 2026",
    "/bons-plans/kindle-scribe/": "Prix vérifiés le 9 septembre 2026",
    "/bons-plans/kobo-elipsa/": "Prix vérifié le 9 septembre 2026",
    "/bons-plans/boox/": "Offres vérifiées le 10 septembre 2026",
    "/bons-plans/bloc-notes-numerique-occasion/": "Canaux vérifiés le 10 septembre 2026",
    "/bons-plans/black-friday/": "Préparation vérifiée le 10 septembre 2026",
}

DEAL_CONTENT = {
    "/bons-plans/bloc-notes-numerique/": r'''
      <p>Au 10 septembre 2026, le bundle reMarkable reste l'offre la plus simple à documenter proprement. BOOX affiche aussi un Note Air5 C à prix barré, mais le coût final dépend encore du bundle, de la TVA et du checkout. Pour Kindle et Kobo, les prix observés servent surtout de repères : ils ne doivent pas être transformés en promotions par défaut.</p>

      <h2 id="offres-verifiees">Offres actives et prix à surveiller</h2>
      <table>
        <thead><tr><th>Offre</th><th>Prix observé</th><th>Référence</th><th>Statut</th></tr></thead>
        <tbody>
          <tr><td>reMarkable Paper Pro + Marker Plus + Book Folio</td><td>849 €</td><td>898 € séparément</td><td>Active et vérifiée</td></tr>
          <tr><td>BOOX Note Air5 C</td><td>529,99 €</td><td>639,98 € barré</td><td>Actif, mais checkout à contrôler</td></tr>
          <tr><td>BOOX Note Air4 C</td><td>499,99 €</td><td>Référence incohérente selon la page BOOX</td><td>Rupture de stock</td></tr>
          <tr><td>Kindle Scribe 2024 16 Go</td><td>à partir de 389 € hors frais</td><td>429,99 € au lancement</td><td>Prix marché à surveiller, pas une promo Amazon</td></tr>
          <tr><td>Kobo Elipsa 2E</td><td>399,99 €</td><td>Prix catalogue officiel</td><td>Prix à surveiller, pas une promo</td></tr>
        </tbody>
      </table>
      <p>Le bundle reMarkable économise 49 € par rapport à la référence d'achat séparé affichée par le constructeur. Ce n'est toutefois un bon plan que si le Book Folio et le Marker Plus faisaient déjà partie du panier prévu. Ajouter un accessoire inutile pour « profiter » d'un bundle reste une dépense supplémentaire.</p>
      <p>Pour BOOX, nous évitons de convertir mécaniquement les prix barrés en pourcentage. Le Note Air5 C est affiché à 529,99 €, mais BOOX précise que le prix final peut varier selon le bundle, la TVA et le checkout. Le Note Air4 C est en rupture et les propres pages de BOOX affichent deux références barrées différentes ; nous ne retenons donc pas de remise nette tant que cette incohérence persiste.</p>

      <h2 id="ce-qui-nest-pas-un-bon-plan">Ce qui n'est pas considéré comme un bon plan</h2>
      <p>Un prix inférieur au lancement d'un ancien modèle n'est pas automatiquement une promotion. De même, un produit affiché avec une remise mais signalé épuisé ne doit pas être présenté comme achetable. Nous séparons donc les offres actives, les prix à surveiller et les promotions expirées.</p>
      <p>Cette distinction est particulièrement importante sur les gammes Kindle et BOOX, où plusieurs générations et configurations peuvent coexister. Une Kindle Scribe 2024 à 389 € sur le marché peut être intéressante, mais ce niveau ne constitue pas à lui seul une promotion Amazon. Chez BOOX, un prix barré n'est pas non plus une référence suffisante si le panier final ou la référence affichée change selon la page.</p>

      <h2 id="quand-acheter">Quand acheter maintenant et quand attendre ?</h2>
      <p>Achetez maintenant si le produit ciblé est déjà le bon pour votre usage et que la réduction porte sur une configuration que vous auriez choisie sans promotion. Attendre est plus logique si le prix actuel est simplement le tarif catalogue, si l'offre implique des accessoires non désirés, si le produit est en rupture ou si le prix final n'est pas encore suffisamment clair.</p>
      <p>Pour vérifier d'abord le budget complet — tablette, stylet, protection et éventuel abonnement — consultez notre <a href="/guides/prix-bloc-notes-numerique/">guide des prix des bloc-notes numériques</a>. Si le produit n'est pas encore choisi, le <a href="/comparatifs/meilleur-bloc-notes-numerique/">comparatif général</a> doit précéder la recherche de remise.</p>

      <h2 id="watchlist">Notre watchlist</h2>
      <ul>
        <li>Kindle Scribe 2024 sous le niveau marché actuel de 389 € à configuration comparable.</li>
        <li>BOOX Note Air4 C si le stock revient avec une référence de prix clarifiée.</li>
        <li>Kobo Elipsa 2E dès qu'elle passe clairement sous son tarif officiel de 399,99 €.</li>
        <li>Bundles reMarkable uniquement lorsque l'accessoire inclus est réellement utile.</li>
      </ul>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list">
        <li><a href="https://remarkable.com/fr-FR/products/remarkable-paper/pro" rel="noopener noreferrer">reMarkable : Paper Pro et bundles</a></li>
        <li><a href="https://euroshop.boox.com/products/noteair5c" rel="noopener noreferrer">BOOX EURO Shop : Note Air5 C</a></li>
        <li><a href="https://euroshop.boox.com/products/noteair4c" rel="noopener noreferrer">BOOX EURO Shop : Note Air4 C</a></li>
        <li><a href="https://www.idealo.fr/prix/204949872/amazon-kindle-scribe-16gb-grey-2024.html" rel="noopener noreferrer">idealo : Kindle Scribe 2024 16 Go</a></li>
        <li><a href="https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e" rel="noopener noreferrer">Rakuten Kobo : Kobo Elipsa 2E</a></li>
      </ul>
    ''',

    "/bons-plans/remarkable/": r'''
      <p>Le 10 septembre 2026, les réductions reMarkable les plus claires ne concernent pas directement le prix de base des tablettes : elles apparaissent surtout dans certains bundles Paper Pro. Le bon calcul consiste donc à comparer le pack au panier que vous auriez réellement acheté.</p>

      <h2 id="prix-reference">Prix de référence reMarkable</h2>
      <table>
        <thead><tr><th>Modèle</th><th>Prix constructeur observé</th></tr></thead>
        <tbody><tr><td>Paper Pure</td><td>à partir de 399 €</td></tr><tr><td>Paper Pro Move</td><td>à partir de 479 €</td></tr><tr><td>Paper Pro</td><td>à partir de 649 €</td></tr></tbody>
      </table>
      <p>Ces niveaux servent de référence pour juger une future promotion. Une baisse réelle doit être comparée au même modèle et à la même configuration.</p>

      <h2 id="bundles">Bundles Paper Pro : 49 € d'écart vérifié</h2>
      <p>Le pack Paper Pro avec Marker Plus et Book Folio est affiché à 849 €, contre une référence de 898 € pour les éléments séparés. Le pack avec Marker Plus et Type Folio est affiché à 899 €, contre 948 €. Dans les deux cas, l'écart observé est de 49 €.</p>
      <p>Ce gain n'a de valeur que si vous vouliez déjà l'étui ou le clavier. Pour quelqu'un qui cherche simplement la tablette et le stylet standard, le prix de départ reste plus pertinent qu'un bundle plus cher.</p>

      <h2 id="reconditionne">Et le reconditionné ?</h2>
      <p>reMarkable maintient une boutique officielle de produits reconditionnés qui liste notamment Paper Pro Move, Paper Pro et reMarkable 2. C'est une piste plus intéressante qu'une remise artificielle sur un accessoire inutile, à condition de comparer le modèle exact, la garantie et le contenu du pack au prix neuf du jour. Notre <a href="/bons-plans/bloc-notes-numerique-occasion/">guide de l'occasion et du reconditionné</a> détaille les contrôles à faire.</p>

      <h2 id="quand-attendre">Quand attendre une meilleure offre ?</h2>
      <p>Si votre priorité est uniquement de réduire le prix de la tablette, les bundles actuels ne changent pas radicalement l'équation. Attendre une campagne temporaire ou surveiller le reconditionné peut avoir plus de sens. En revanche, si un Book Folio ou un Type Folio faisait déjà partie du panier, la réduction de bundle est une économie documentée.</p>
      <p>Avant d'acheter, vérifiez aussi si l'écosystème reMarkable correspond à vos besoins. Pour un arbitrage produit, utilisez les <a href="/comparatifs/remarkable-vs-boox/">comparaisons reMarkable vs BOOX</a> ou le <a href="/comparatifs/remarkable-vs-supernote/">comparatif reMarkable vs Supernote</a> plutôt que de laisser la remise décider à votre place.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list"><li><a href="https://remarkable.com/fr-FR/shop/compare" rel="noopener noreferrer">reMarkable : comparaison des modèles</a></li><li><a href="https://remarkable.com/fr-FR/products/remarkable-paper/pro" rel="noopener noreferrer">reMarkable : Paper Pro, accessoires et bundles</a></li><li><a href="https://remarkable.com/fr-FR/shop/refurbished/remarkable-paper-pro" rel="noopener noreferrer">reMarkable : produits reconditionnés</a></li></ul>
    ''',

    "/bons-plans/kindle-scribe/": r'''
      <p>Aucune promotion Amazon actuelle suffisamment solide n'est confirmée au 9 septembre 2026 pour être présentée ici comme offre active. C'est volontaire : la gamme Kindle Scribe a plusieurs générations et une baisse sur un ancien modèle peut facilement être confondue avec une remise sur la gamme actuelle.</p>

      <h2 id="repere-prix">Les repères de prix utiles</h2>
      <p>Amazon avait lancé la génération 2024 du Kindle Scribe à partir de 429,99 €. Le marché montre aujourd'hui encore des variantes de cette génération à des prix différents selon le stockage et le vendeur. La Scribe Colorsoft 64 Go de la génération 2026 est, elle, affichée à 699,99 € chez Boulanger au moment de notre contrôle.</p>
      <p>Ces deux produits ne doivent pas être comparés comme s'ils étaient identiques : une ancienne Scribe noir et blanc bradée peut être un meilleur achat budgétaire sans pour autant constituer une remise sur la Colorsoft.</p>

      <h2 id="historique">Une vraie baisse a déjà eu lieu en août</h2>
      <p>Le 11 août 2026, Numerama rapportait une promotion Amazon à 329,99 € sur une Kindle Scribe 64 Go d'ancienne génération. Nous conservons ce prix comme repère historique : il montre que cette gamme peut connaître des baisses significatives. Mais cette offre n'est pas considérée active le 9 septembre.</p>

      <h2 id="seuil">Quel seuil surveiller ?</h2>
      <p>Pour l'ancienne génération, un retour autour de 330 € sur une configuration comparable mérite d'être regardé de près. Entre 330 € et le prix catalogue d'origine, l'intérêt dépend du stockage, de l'état du produit et de l'écart avec la génération plus récente. Pour la Colorsoft, nous n'affichons aucun « seuil magique » tant qu'un historique français suffisant n'est pas disponible.</p>

      <h2 id="avant-achat">Ne laissez pas la remise choisir le modèle</h2>
      <p>Kindle Scribe reste d'abord une liseuse Kindle avec prise de notes. Si votre besoin principal est la lecture et l'annotation, elle peut être cohérente ; si vous cherchez un environnement plus ouvert ou des workflows professionnels spécifiques, comparez d'abord les appareils. Voir <a href="/comparatifs/kindle-scribe-vs-remarkable/">Kindle Scribe vs reMarkable</a> et <a href="/comparatifs/kindle-scribe-vs-kobo-elipsa/">Kindle Scribe vs Kobo Elipsa</a>.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list"><li><a href="https://www.aboutamazon.fr/actualites/innovations/decouvrez-la-nouvelle-gamme-de-kindle-y-compris-le-premier-kindle-couleur" rel="noopener noreferrer">Amazon France : lancement Kindle Scribe 2024</a></li><li><a href="https://www.numerama.com/tech/2309717-amazon-brade-de-150-e-sa-liseuse-premium-kindle-scribe-qui-fait-carnet-de-notes.html" rel="noopener noreferrer">Numerama : promotion du 11 août 2026</a></li><li><a href="https://www.boulanger.com/ref/1240827" rel="noopener noreferrer">Boulanger : Kindle Scribe Colorsoft 64 Go</a></li></ul>
    ''',

    "/bons-plans/kobo-elipsa/": r'''
      <p>La Kobo Elipsa 2E est affichée 399,99 € sur la boutique officielle au 9 septembre 2026. Nous ne voyons pas de promotion constructeur clairement vérifiée à cette date : le tarif actuel sert donc de prix de référence, pas de « bon plan » artificiel.</p>

      <h2 id="prix-reference">399,99 € : le repère actuel</h2>
      <p>La configuration officielle inclut le Kobo Stylus 2. C'est important pour comparer correctement les offres : un marchand moins cher qui vend une configuration différente ne constitue pas forcément une économie réelle une fois le stylet ajouté.</p>

      <h2 id="bonne-remise">À partir de quand une offre devient intéressante ?</h2>
      <p>Le signal le plus simple est une baisse nette sous 399,99 € à configuration équivalente, chez Kobo ou un revendeur identifiable. Nous préférons ne pas inventer un seuil arbitraire de -10 % ou -20 % : une réduction plus petite peut être utile si elle porte sur le bon bundle, tandis qu'une grosse remise peut cacher un produit d'exposition, un stock ancien ou un pack incomplet.</p>

      <h2 id="reconditionne">Surveiller aussi le reconditionné</h2>
      <p>Kobo référence une catégorie « certifié reconditionné » dans sa gamme de liseuses. Le stock varie. Pour une Elipsa d'occasion ou reconditionnée, comparez toujours le prix au neuf du jour et vérifiez la garantie, le stylet inclus et l'état de l'écran. Notre page <a href="/bons-plans/bloc-notes-numerique-occasion/">bloc-notes numérique d'occasion</a> sert précisément à ce contrôle.</p>

      <h2 id="pour-qui">La remise ne change pas le positionnement</h2>
      <p>La Kobo Elipsa 2E reste surtout intéressante si lecture, annotation d'eBooks/PDF et prise de notes cohabitent dans le même usage. Si vous hésitez avec Kindle ou reMarkable, commencez par <a href="/comparatifs/kindle-scribe-vs-kobo-elipsa/">Kindle Scribe vs Kobo Elipsa</a> ou <a href="/comparatifs/kobo-elipsa-vs-remarkable/">Kobo Elipsa vs reMarkable</a>, puis revenez aux promotions une fois le choix cadré.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list"><li><a href="https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e" rel="noopener noreferrer">Rakuten Kobo : Kobo Elipsa 2E</a></li><li><a href="https://www.kobo.com/fr/fr/ereaders" rel="noopener noreferrer">Rakuten Kobo : gamme et reconditionné certifié</a></li></ul>
    ''',

    "/bons-plans/boox/": r'''
      <p>BOOX affiche plusieurs prix barrés, mais ce sont aussi les offres qui demandent le plus de prudence. Le stock, le bundle, l'entrepôt, la TVA et le checkout peuvent modifier le prix réellement payé. Nous séparons donc prix affiché, référence barrée et offre réellement exploitable.</p>

      <h2 id="air4c">Note Air4 C : prix affiché, rupture et références contradictoires</h2>
      <p>Le Note Air4 C est affiché à 499,99 €, mais il est signalé <strong>épuisé</strong> au moment de notre contrôle. Surtout, BOOX ne montre pas la même référence barrée partout : la collection « Mid-year sale » affiche 549,99 €, tandis que la fiche produit affiche 629,98 €.</p>
      <p>Nous conservons donc 499,99 € comme prix observé, mais nous ne calculons aucun pourcentage de remise et ne retenons pas de prix de référence unique tant que cette contradiction subsiste. Une remise visible n'est pas suffisamment défendable si sa propre base varie selon la page du marchand.</p>

      <h2 id="air5c">Note Air5 C : 529,99 €, checkout à contrôler</h2>
      <p>La fiche officielle du Note Air5 C affiche 529,99 € avec une référence barrée à 639,98 €. BOOX précise toutefois que le prix affiché après sélection d'un bundle peut ne pas inclure la TVA et que le coût final dépend du checkout. Nous classons donc ce prix comme <strong>actif mais sensible au panier final</strong>.</p>
      <p>Avant de relayer une économie ou un pourcentage, il faut vérifier la même configuration, l'entrepôt UE, la TVA et les accessoires inclus. Le prix barré reste ici un signal secondaire, pas une preuve suffisante à lui seul.</p>

      <h2 id="quand-acheter">Quand l'offre BOOX devient vraiment intéressante ?</h2>
      <p>Une offre BOOX devient exploitable lorsque le stock est confirmé et que le prix TTC final peut être comparé à une référence réellement comparable pour le même modèle et le même bundle. Un ancien modèle soldé peut être pertinent si ses fonctions suffisent ; il ne doit toutefois pas être présenté comme équivalent à la génération actuelle.</p>
      <p>Pour choisir d'abord la bonne famille de produit, consultez <a href="/comparatifs/remarkable-vs-boox/">reMarkable vs BOOX</a> ou le <a href="/guides/tablette-classique-ou-tablette-e-ink/">guide tablette classique vs E Ink</a>.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list"><li><a href="https://euroshop.boox.com/products/noteair4c" rel="noopener noreferrer">BOOX EURO Shop : Note Air4 C</a></li><li><a href="https://euroshop.boox.com/collections/mid-year-sale" rel="noopener noreferrer">BOOX EURO Shop : Mid-year sale</a></li><li><a href="https://euroshop.boox.com/products/noteair5c" rel="noopener noreferrer">BOOX EURO Shop : Note Air5 C</a></li></ul>
    ''',

    "/bons-plans/bloc-notes-numerique-occasion/": r'''
      <p>Sur un bloc-notes numérique d'occasion, la réduction affichée ne suffit pas. Le vrai bon plan dépend du modèle exact, de l'état de l'écran, de la batterie, du stylet, de la garantie et du prix neuf du même appareil. Un vieux modèle à moitié prix peut être moins intéressant qu'un reconditionné récent légèrement plus cher.</p>

      <h2 id="canaux">Les canaux officiels à vérifier en premier</h2>
      <p>reMarkable maintient une boutique officielle de produits reconditionnés. Kobo dispose également d'une catégorie « certifié reconditionné » ; au moment de notre contrôle, les exemples visibles y étaient signalés épuisés. BOOX conserve de son côté une page d'appareils d'occasion pour la gamme Note, elle aussi actuellement en rupture.</p>
      <p>La page BOOX Used devices affiche toujours un prix à partir de 359 €, mais ce niveau ne correspond pas à une offre achetable aujourd'hui puisqu'elle est signalée <strong>sold out</strong>. Nous le conservons uniquement comme repère de canal : le modèle, l'état, les accessoires, l'entrepôt, la TVA et le checkout doivent être vérifiés au retour du stock.</p>

      <h2 id="checklist">Checklist avant d'acheter d'occasion</h2>
      <ul>
        <li><strong>Écran :</strong> rechercher pixels bloqués, zones de contraste anormal, rayures et traces de pression.</li>
        <li><strong>Stylet :</strong> vérifier qu'il est inclus, reconnu et que les boutons/gomme fonctionnent si le modèle en possède.</li>
        <li><strong>Batterie :</strong> demander l'âge de l'appareil et vérifier qu'il tient une charge cohérente avec l'usage prévu.</li>
        <li><strong>Compte :</strong> s'assurer que l'ancien propriétaire a dissocié l'appareil lorsque l'écosystème l'exige.</li>
        <li><strong>Garantie :</strong> distinguer garantie constructeur, garantie revendeur et simple droit de retour.</li>
        <li><strong>Accessoires :</strong> comparer le prix avec une configuration neuve équivalente, pas seulement la tablette nue.</li>
      </ul>

      <h2 id="prix">Comment savoir si le prix est bon ?</h2>
      <p>Commencez par le prix neuf actuel du même modèle ou de son remplaçant direct. Une décote doit compenser l'âge, l'absence éventuelle de garantie et le risque sur la batterie. Si l'écart avec le neuf est faible, le reconditionné certifié ou une promotion neuve peut être plus rationnel.</p>
      <p>Pour rester dans un budget serré sans acheter trop vieux, comparez aussi les <a href="/comparatifs/bloc-notes-numerique-pas-cher/">bloc-notes numériques pas chers</a> et le <a href="/guides/prix-bloc-notes-numerique/">guide des budgets</a>.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list"><li><a href="https://remarkable.com/fr-FR/shop/refurbished/remarkable-paper-pro" rel="noopener noreferrer">reMarkable : boutique reconditionnée</a></li><li><a href="https://ereader.kobo.com/fr-fr/collections/certified-refurbished-ereaders" rel="noopener noreferrer">Kobo : liseuses certifiées reconditionnées</a></li><li><a href="https://euroshop.boox.com/products/copy-of-used-devices" rel="noopener noreferrer">BOOX EURO Shop : Used devices</a></li></ul>
    ''',

    "/bons-plans/black-friday/": r'''
      <p>Le Black Friday 2026 aura lieu le <strong>vendredi 27 novembre 2026</strong>. Au 10 septembre, aucune offre Black Friday 2026 ne doit être présentée comme active. Cette page sert donc d'abord à conserver des prix de référence datés pour les modèles à surveiller ; elle basculera vers un suivi beaucoup plus fréquent à l'approche de l'événement.</p>

      <h2 id="date">Quelle est la date du Black Friday 2026 ?</h2>
      <p>Le Black Friday tombe le vendredi 27 novembre. Les campagnes commerciales peuvent commencer avant cette date et se poursuivre après. En 2025, Amazon avait par exemple communiqué une période d'offres du 20 novembre au 1er décembre. Ce précédent aide à anticiper la fenêtre, mais ne permet pas de prédire les dates ni les remises de 2026.</p>

      <h2 id="watchlist">Les prix à garder en repère avant novembre</h2>
      <p>Ces prix ont été observés le 10 septembre 2026. Ils ne constituent pas des promotions Black Friday : ils servent de baseline pour comparer ensuite une offre portant sur la même génération, le même stockage et, lorsque nécessaire, le même bundle.</p>
      <table>
        <thead><tr><th>Modèle</th><th>Prix observé</th><th>Type de repère</th></tr></thead>
        <tbody>
          <tr><td>reMarkable Paper Pure</td><td>à partir de 399 €</td><td>Constructeur</td></tr>
          <tr><td>reMarkable Paper Pro Move</td><td>à partir de 479 €</td><td>Constructeur</td></tr>
          <tr><td>reMarkable Paper Pro</td><td>à partir de 649 €</td><td>Constructeur</td></tr>
          <tr><td>Kobo Elipsa 2E</td><td>399,99 €</td><td>Boutique officielle</td></tr>
          <tr><td>Kindle Scribe 2024 32 Go</td><td>449,99 €</td><td>Prix revendeur observé</td></tr>
          <tr><td>Kindle Scribe Colorsoft 64 Go 2026</td><td>699,99 €</td><td>Prix revendeur observé</td></tr>
          <tr><td>BOOX Note Air5 C</td><td>529,99 €</td><td>BOOX EURO Shop, checkout à contrôler</td></tr>
        </tbody>
      </table>
      <p>BOOX demande une vigilance particulière : la boutique indique que le bundle choisi, la TVA et le checkout peuvent modifier le coût final. Le Note Max reste dans notre watchlist, mais nous ne lui attribuons pas encore de baseline unique tant que la configuration comparable n'est pas suffisamment claire.</p>

      <h2 id="methode">Comment nous validerons une offre</h2>
      <p>Chaque offre devra avoir un prix actuel, une source, une heure de vérification et un prix de référence défendable. Un prix barré ne suffira pas. Nous comparerons la même génération, le même stockage et les mêmes accessoires. Une promotion en rupture passera en « sold out » et sera retirée de la sélection active.</p>
      <p>Pendant la semaine du Black Friday, la durée de validité d'une vérification sera réduite à 24 heures. Cela évite de conserver une offre disparue plusieurs jours dans une page qui se présente comme actuelle.</p>

      <h2 id="preparer">Préparer son achat avant novembre</h2>
      <p>Le meilleur moyen d'éviter l'achat impulsif est de choisir le produit avant la promotion. Notez le prix actuel de la configuration exacte que vous envisagez — modèle, stockage et accessoires — puis comparez le prix Black Friday à cette même base. Si vous hésitez encore entre plusieurs familles, commencez par le <a href="/comparatifs/meilleur-bloc-notes-numerique/">comparatif des meilleurs bloc-notes numériques</a> et le <a href="/guides/prix-bloc-notes-numerique/">guide des prix</a>.</p>

      <h2 id="sources">Sources consultées</h2>
      <ul class="source-list">
        <li><a href="https://www.timeanddate.com/holidays/us/black-friday" rel="noopener noreferrer">Timeanddate : date du Black Friday 2026</a></li>
        <li><a href="https://remarkable.com/fr-FR/shop/compare" rel="noopener noreferrer">reMarkable : comparaison et prix de départ des modèles</a></li>
        <li><a href="https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e" rel="noopener noreferrer">Rakuten Kobo : Kobo Elipsa 2E</a></li>
        <li><a href="https://www.boulanger.com/c/e-book-liseuse/brand~amazon" rel="noopener noreferrer">Boulanger : prix observés des Kindle Scribe</a></li>
        <li><a href="https://euroshop.boox.com/products/noteair5c" rel="noopener noreferrer">BOOX EURO Shop : Note Air5 C et conditions de prix</a></li>
        <li><a href="https://www.aboutamazon.fr/actualites/appareils-amazon/meilleures-offres-appareils-amazon-black-friday-2025" rel="noopener noreferrer">Amazon France : fenêtre Black Friday 2025 (historique)</a></li>
      </ul>
    ''',
}
