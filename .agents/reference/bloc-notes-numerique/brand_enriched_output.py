from brand_data import VERIFIED_AT
from brand_render_common import internal_link


def _source_list(items):
    return '<ul class="source-list">' + ''.join(
        f'<li><a href="{url}" rel="noopener noreferrer">{label}</a></li>'
        for label, url in items
    ) + '</ul>'


def _remarkable_accessories():
    sources = [
        ('reMarkable — Markers nouvelle génération', 'https://blog.remarkable.com/products/remarkable-paper/markers'),
        ('reMarkable — mines Marker nouvelle génération', 'https://remarkable.com/fr-FR/products/remarkable-paper/marker-tips'),
        ('reMarkable — Paper Pure et ses accessoires', 'https://remarkable.com/products/remarkable-paper/pure'),
        ('reMarkable — Sleeve Folio Paper Pure', 'https://remarkable.com/fr-FR/products/remarkable-paper/pure/sleeve-folio'),
        ('reMarkable — Book Folio Paper Pro Move', 'https://remarkable.com/fr-FR/products/remarkable-paper/pro-move/folio'),
        ('reMarkable — Book Folio Paper Pro', 'https://remarkable.com/fr-FR/products/remarkable-paper/pro/folio'),
        ('reMarkable — Type Folio Paper Pro', 'https://remarkable.com/fr-FR/products/remarkable-paper/pro/type-folio?region_id=000250'),
        ('reMarkable — Folios reMarkable 2', 'https://remarkable.com/products/remarkable-2/folios'),
        ('reMarkable — Type Folio reMarkable 2', 'https://remarkable.com/products/remarkable-2/type-folio'),
        ('reMarkable — reMarkable 2 et accessoires encore disponibles', 'https://remarkable.com/products/remarkable-2'),
    ]
    return f'''
<p class="article-answer"><strong>Chez reMarkable, la première question n’est pas « quel accessoire acheter ? », mais « avec quelle génération est-il réellement compatible ? »</strong> Paper Pure, Paper Pro Move, Paper Pro et reMarkable 2 n’utilisent pas tous les mêmes étuis ni les mêmes claviers, et les Markers de l’ancienne génération ne sont pas interchangeables avec les nouveaux.</p>
<h2 id="matrice">Compatibilité des principaux accessoires reMarkable</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Modèle</th><th>Stylet compatible</th><th>Protection officielle</th><th>Clavier</th><th>Point d’attention</th></tr></thead><tbody>
<tr><td><strong>Paper Pure</strong></td><td>Marker ou Marker Plus nouvelle génération</td><td>Sleeve Folio Paper Pure</td><td>Aucun Type Folio compatible documenté</td><td>le Marker standard est inclus avec la tablette ; les étuis des autres reMarkable ne sont pas à considérer comme interchangeables</td></tr>
<tr><td><strong>Paper Pro Move</strong></td><td>Marker ou Marker Plus nouvelle génération</td><td>Book Folio Paper Pro Move</td><td>Pas de Type Folio : le modèle ne dispose pas de l’interface prévue pour ce clavier</td><td>le Book Folio Paper Pro ou reMarkable 2 ne convient pas à cause des dimensions différentes</td></tr>
<tr><td><strong>Paper Pro</strong></td><td>Marker ou Marker Plus nouvelle génération</td><td>Book Folio Paper Pro</td><td>Type Folio Paper Pro</td><td>Book Folio et Type Folio sont spécifiques au Paper Pro</td></tr>
<tr><td><strong>reMarkable 2</strong></td><td>Marker / Marker Plus de génération reMarkable 2</td><td>Folio ou Book Folio reMarkable 2</td><td>Type Folio reMarkable 2</td><td>les nouveaux Markers Paper ne sont pas compatibles avec reMarkable 2, et inversement</td></tr>
</tbody></table></div>
<h2 id="marker">Marker ou Marker Plus : que paie-t-on en plus ?</h2>
<p>Sur la génération Paper actuelle, Marker et Marker Plus utilisent la même famille de mines, se fixent magnétiquement et se rechargent sans fil sur les modèles compatibles. La différence la plus concrète est la gomme intégrée au dos du Marker Plus. Si vous utilisez déjà les outils de sélection ou d’effacement à l’écran sans gêne, ce supplément n’est pas indispensable.</p>
<p>Les mines de la nouvelle génération sont conçues exclusivement pour les Markers de Paper Pure, Paper Pro Move et Paper Pro. Pour une reMarkable 2, il faut rester sur les consommables de son ancienne génération.</p>
<h2 id="folios">Sleeve Folio, Book Folio ou Type Folio ?</h2>
<p><strong>Sleeve Folio</strong> est la protection dédiée au Paper Pure : la tablette se glisse dans une housse rembourrée. <strong>Book Folio</strong> reste fixé à la tablette pendant l’utilisation et existe dans une version propre au Paper Pro Move, au Paper Pro et à reMarkable 2. Les dimensions diffèrent suffisamment pour empêcher de réutiliser le même étui entre ces familles.</p>
<p><strong>Type Folio</strong> est un choix plus engageant : il ajoute un vrai clavier physique. Il existe pour Paper Pro et pour reMarkable 2, mais pas pour Paper Pro Move. Le Type Folio du Paper Pro pèse environ 485 g à lui seul ; il transforme donc nettement la portabilité d’un appareil acheté au départ comme carnet numérique.</p>
<h2 id="panier">Quel panier a réellement du sens ?</h2>
<ul>
<li><strong>Prise de notes principalement manuscrite :</strong> tablette + Marker suffisent dans beaucoup de cas ; ajoutez une protection si l’appareil voyage.</li>
<li><strong>Corrections fréquentes au stylet :</strong> Marker Plus peut être utile grâce à sa gomme intégrée.</li>
<li><strong>Déplacements quotidiens :</strong> privilégiez la protection exactement conçue pour votre modèle plutôt qu’un étui générique mal ajusté.</li>
<li><strong>Rédaction longue au clavier :</strong> Type Folio n’a de sens que si vous comptez réellement taper sur Paper Pro ou reMarkable 2 au lieu de reprendre un ordinateur.</li>
</ul>
<p>Pour comparer le coût total avec d’autres marques, voir {internal_link('/guides/prix-bloc-notes-numerique/', 'le guide sur le prix d’un bloc-notes numérique')} et {internal_link('/marques/remarkable/remarkable-paper-pro/', 'la fiche du Paper Pro')}.</p>
<h2 id="achat-occasion">Attention aux accessoires en occasion</h2>
<p>reMarkable 2 est discontinuée, mais reMarkable indique continuer à vendre ses Markers, Book Folios, Type Folios et mines. Cela évite qu’un achat d’occasion soit immédiatement bloqué par l’absence d’accessoires, mais il faut malgré tout vérifier la génération exacte du stylet ou du Folio proposé avec la tablette.</p>
<h2 id="sources">Sources consultées</h2>
<p>Compatibilités et accessoires vérifiés le {VERIFIED_AT}. Les prix et bundles peuvent évoluer ; la matrice ci-dessus porte sur la compatibilité, pas sur les promotions du moment.</p>
{_source_list(sources)}
'''


def _boox_accessories():
    sources = [
        ('BOOX — Go 10.3 (Gen II)', 'https://shop.boox.com/collections/all-products/products/go103gen2'),
        ('BOOX — Magnetic Case for Go 10.3 Series', 'https://shop.boox.com/products/go103series-magnetic-case'),
        ('BOOX — Note Air5 C', 'https://shop.boox.com/products/noteair5c'),
        ('BOOX — Magnetic Keyboard Cover for Note Air5 C', 'https://shop.boox.com/products/magnetic-keyboard-cover-for-note-air5-c'),
        ('BOOX — Note Max', 'https://shop.boox.com/products/notemax'),
        ('BOOX — Magnetic Case for Note Max / Tab X C', 'https://shop.boox.com/products/note-max-magnetic-case'),
        ('BOOX — Magnetic Keyboard Cover for Note Max / Tab X C', 'https://shop.boox.com/products/note-max-magnetic-keyboard-cover'),
        ('BOOX — Tab X C', 'https://shop.boox.com/products/tabxc'),
        ('BOOX — Tab Ultra C Pro', 'https://shop.boox.com/products/tabultracpro'),
        ('BOOX — Keyboard Cover for Tab Ultra C Pro', 'https://shop.boox.com/products/keyboard-cover-for-tab-ultra-c-pro'),
    ]
    return f'''
<p class="article-answer"><strong>Les accessoires BOOX ne sont pas universels : le stylet, l’étui, le clavier et même l’extension de stockage changent selon le modèle.</strong> Une compatibilité correcte exige donc de partir du nom exact de l’appareil — Go 10.3 Gen II, Note Air5 C, Note Max, Tab X C ou Tab Ultra C Pro — plutôt que d’acheter un accessoire simplement marqué « BOOX ».</p>
<h2 id="matrice">Compatibilité des accessoires BOOX par modèle</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Modèle</th><th>Stylet</th><th>Étui / protection</th><th>Clavier officiel</th><th>microSD</th></tr></thead><tbody>
<tr><td><strong>Go 10.3 Gen II</strong></td><td>InkSense Plus, inclus dans le pack standard</td><td>BOOX Magnetic Case for Go 10.3 Series</td><td>Aucun clavier magnétique dédié mis en avant</td><td>pas de slot microSD indiqué dans les spécifications officielles actuelles</td></tr>
<tr><td><strong>Note Air5 C</strong></td><td>Pen3, inclus</td><td>Note Air5 C Magnetic Protective Case</td><td>Magnetic Keyboard Cover for Note Air5 C</td><td>oui, jusqu’à 2 To annoncés</td></tr>
<tr><td><strong>Note Max</strong></td><td>Pen Plus, inclus</td><td>Magnetic Case partagé avec Tab X C</td><td>Magnetic Keyboard Cover partagé avec Tab X C</td><td>pas de slot microSD indiqué dans les spécifications officielles actuelles</td></tr>
<tr><td><strong>Tab X C</strong></td><td>InkSpire, inclus</td><td>Magnetic Case partagé avec Note Max</td><td>Magnetic Keyboard Cover partagé avec Note Max</td><td>pas de slot microSD indiqué dans les spécifications officielles actuelles</td></tr>
<tr><td><strong>Tab Ultra C Pro</strong></td><td>Pen2 Pro dans le pack standard actuel ; BOOX documente aussi un stylet magnétique avec gomme dans certains bundles</td><td>Three-Fold Case / protection dédiée selon bundle</td><td>Magnetic Keyboard Cover with Trackpad</td><td>oui</td></tr>
</tbody></table></div>
<h2 id="stylets">Le stylet est le point le plus facile à rater</h2>
<p>BOOX utilise plusieurs générations de stylets. Le Go 10.3 Gen II est explicitement limité à l’InkSense Plus, alors que le Note Air5 C est fourni avec le Pen3. Note Max est livré avec un Pen Plus, et Tab X C utilise le nouvel InkSpire avec recharge magnétique sans fil. Acheter un second stylet « BOOX » sans vérifier le modèle exact peut donc conduire à une incompatibilité ou à des fonctions perdues.</p>
<h2 id="claviers">Quels modèles méritent réellement un clavier ?</h2>
<p>Le <strong>Note Air5 C</strong> dispose d’un clavier magnétique dédié, connecté par pogo pins, avec un port USB-C permettant la recharge traversante. BOOX le présente comme un outil de productivité légère pour les e-mails, rapports courts ou feuilles de calcul. Il pèse toutefois près de 485 g : sur un appareil d’environ 440 g, le clavier change complètement le poids et l’usage du setup.</p>
<p><strong>Note Max et Tab X C</strong> partagent un clavier magnétique pleine taille, logique pour leur écran 13,3 pouces. <strong>Tab Ultra C Pro</strong> possède son propre clavier avec trackpad, vendu séparément. Pour un usage principalement manuscrit ou PDF, ces claviers ne sont pas automatiquement un bon achat : ils répondent surtout à un besoin de saisie prolongée.</p>
<h2 id="protections">Les étuis ne suivent pas toujours les familles de produits</h2>
<p>Le Magnetic Case du Go 10.3 Series couvre Go 10.3 Gen II et les autres variantes explicitement listées par BOOX. Note Max et Tab X C partagent quant à eux le même Magnetic Case malgré leurs technologies d’écran différentes. À l’inverse, le Note Air5 C dispose de protections conçues pour sa propre géométrie.</p>
<p>Cette logique rend les achats d’occasion plus délicats : un étui d’un ancien Note Air ou d’un ancien Go n’est pas à considérer comme compatible par défaut, même si la diagonale d’écran est identique.</p>
<h2 id="stockage">microSD : utile sur certains modèles, absente sur d’autres</h2>
<p>Le Note Air5 C possède un slot microSD et BOOX annonce une extension jusqu’à 2 To. Le Tab Ultra C Pro possède également un slot microSD. À l’inverse, les fiches techniques actuelles du Go 10.3 Gen II, du Note Max et du Tab X C n’en listent pas. Si vous transportez une grosse bibliothèque de PDF localement, cette différence peut compter davantage qu’un étui ou un clavier.</p>
<h2 id="panier">Construire le panier par usage</h2>
<ul>
<li><strong>Notes manuscrites :</strong> gardez d’abord le stylet livré avec le modèle ; ajoutez une protection si l’appareil se déplace souvent.</li>
<li><strong>PDF volumineux :</strong> privilégiez la taille d’écran et le stockage avant le clavier.</li>
<li><strong>Saisie de texte :</strong> choisissez un modèle pour lequel BOOX propose réellement un clavier adapté, plutôt qu’un clavier Bluetooth générique ajouté après coup.</li>
<li><strong>Bibliothèque locale :</strong> vérifiez la présence du microSD avant achat si le stockage interne ne suffit pas.</li>
</ul>
<p>Pour replacer ces accessoires dans le coût total, voir {internal_link('/guides/prix-bloc-notes-numerique/', 'le guide sur les prix')} ainsi que {internal_link('/marques/boox/boox-note-air/', 'la famille Note Air')} et {internal_link('/marques/boox/boox-tab-ultra/', 'la famille Tab Ultra')}.</p>
<h2 id="sources">Sources consultées</h2>
<p>Compatibilités vérifiées le {VERIFIED_AT} à partir des pages officielles BOOX. Les bundles et disponibilités peuvent évoluer ; les inclusions mentionnées correspondent aux fiches officielles consultées.</p>
{_source_list(sources)}
'''


def _boox_review():
    official = [
        ('BOOX — politique de mises à jour firmware', 'https://help.boox.com/hc/en-us/articles/10701135807124-Firmware-Updates'),
        ('BOOX — garantie', 'https://shop.boox.com/pages/warranty'),
        ('BOOX — politique de retours', 'https://shop.boox.com/pages/return'),
        ('BOOX — compte ONYX et serveurs', 'https://help.boox.com/hc/en-us/articles/10701174893972-ONYX-Account-Sign-up-and-Deletion'),
        ('BOOX — fonctionnement du cloud tiers', 'https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage'),
        ('BOOX — données et confidentialité', 'https://help.boox.com/hc/en-us/articles/360046663532-BOOX-Privacy-Do-We-Collect-Your-Personal-Information'),
        ('BOOX — Note Air5 C', 'https://shop.boox.com/products/noteair5c'),
    ]
    independent = [
        ('TechRadar — Onyx BOOX Note Air5 C review', 'https://www.techradar.com/tablets/ereaders/onyx-boox-note-air5-c-review'),
        ('Digital Trends — BOOX Note Air5 C hands-on review', 'https://www.digitaltrends.com/tablets/i-tested-an-ai-powered-kindle-scribe-rival-and-it-shows-how-far-behind-amazon-is/'),
        ('Trustpilot — avis clients du BOOX Shop', 'https://www.trustpilot.com/review/shop.boox.com'),
        ('Trustpilot — avis clients boox.com', 'https://www.trustpilot.com/review/boox.com'),
    ]
    return f'''
<p class="article-answer"><strong>Notre avis sur BOOX en 2026 : la marque reste l’une des plus intéressantes pour qui veut Android, des PDF avancés et des applications tierces sur E Ink, mais l’achat demande davantage de vérifications qu’un reMarkable ou un Kindle.</strong> Le modèle exact, la version Android, la politique de retour du canal d’achat et la durée de support logiciel comptent presque autant que l’écran lui-même.</p>
<h2 id="produits">Sur les appareils : beaucoup de liberté, davantage de complexité</h2>
<p>Le principal avantage de BOOX reste Android. Google Play, NeoReader, l’application Notes, les clouds tiers et les nombreux réglages de rafraîchissement permettent d’adapter l’appareil à des workflows très différents. Les essais indépendants du Note Air5 C soulignent cette polyvalence et la richesse des outils.</p>
<p>La contrepartie est connue : toutes les applications Android ne sont pas conçues pour E Ink, et les réglages de contraste, vitesse ou couleur peuvent demander du temps. La gamme change aussi rapidement ; Go 10.3 Gen II et Note Air5 C tournent aujourd’hui sous Android 15, quand Note Max et Tab X C sont sous Android 13 et Tab Ultra C Pro sous Android 12.</p>
<h2 id="updates">Combien de temps BOOX promet-il des mises à jour ?</h2>
<p>BOOX indique fournir des mises à jour firmware gratuites pendant <strong>au moins trois ans à compter du lancement du modèle</strong>. Cette promesse porte sur le firmware BOOX, pas nécessairement sur un changement de version majeure d’Android. La marque précise aussi que les mises à jour sont déployées par vagues et que le calendrier peut varier selon le modèle.</p>
<p>C’est un point positif pour un appareil E Ink destiné à durer plusieurs années, mais il faut distinguer « firmware BOOX maintenu » et « version Android récente ». Pour un usage professionnel dépendant d’applications tierces, la version Android de départ reste donc un critère important.</p>
<h2 id="sav">Garantie et réparation : le canal d’achat change la situation</h2>
<p>La boutique globale BOOX annonce une garantie d’un an sur les appareils principaux ; la boutique européenne annonce une couverture de deux ans. La documentation précise également qu’une réparation payante peut rester possible au-delà de la période de garantie et que les demandes passent par le service après-vente BOOX avec preuve d’achat.</p>
<p>Ce détail rend le revendeur particulièrement important. Un appareil acheté chez un distributeur ou une marketplace doit généralement être retourné via ce vendeur plutôt que via la boutique globale BOOX. Pour un produit coûteux et fragile comme une tablette E Ink, la qualité du canal d’achat fait donc partie de la décision.</p>
<h2 id="retours">La politique de retour mérite d’être lue avant de commander</h2>
<p>La boutique BOOX permet de demander un retour dans les 30 jours, mais les conditions dépendent de l’entrepôt et de l’état du produit. La politique prévoit notamment inspection avant remboursement, éventuels frais liés au retour, à la réception ou au reconditionnement, et des règles différentes pour les commandes expédiées depuis Hong Kong ou depuis des entrepôts locaux.</p>
<p>Les avis clients publics montrent des expériences contrastées : on trouve à la fois des retours très positifs sur les appareils et des plaintes concernant la gestion de retours ou le support. Ces témoignages sont anecdotiques et ne permettent pas de mesurer un taux réel de problème, mais ils renforcent l’intérêt de vérifier les conditions exactes du vendeur avant achat plutôt que de juger uniquement le produit.</p>
<h2 id="cloud">Compte ONYX, cloud et confidentialité</h2>
<p>Un compte ONYX donne accès à 10 Go de cloud, à la synchronisation des notes et à d’autres services. BOOX utilise plusieurs serveurs et recommande de choisir celui correspondant à sa région puis de conserver le même serveur entre appareils pour éviter des synchronisations incomplètes.</p>
<p>La marque permet aussi d’intégrer Dropbox, Google Drive, OneDrive ou des services WebDAV/Nextcloud. Sa documentation indique que l’envoi de logs au support est optionnel et que les équipes techniques ne peuvent pas accéder au contenu des documents personnels via ces logs. Pour un environnement professionnel sensible, il reste pertinent de vérifier les politiques de l’entreprise et de privilégier les stockages autorisés par son organisation.</p>
<h2 id="points-forts">Les points forts de BOOX comme marque</h2>
<ul>
<li>gamme très large, du carnet 10,3 pouces aux grands écrans 13,3 pouces ;</li>
<li>Android et Google Play sur les modèles actuels ;</li>
<li>outils PDF et notes particulièrement complets ;</li>
<li>intégration de plusieurs clouds tiers ;</li>
<li>engagement public sur au moins trois ans de mises à jour firmware.</li>
</ul>
<h2 id="limites">Les limites à accepter</h2>
<ul>
<li>gamme et versions Android qui évoluent vite ;</li>
<li>courbe d’apprentissage plus élevée qu’un écosystème fermé ;</li>
<li>expérience variable des applications tierces sur E Ink ;</li>
<li>garantie, retours et support qui dépendent du canal d’achat ;</li>
<li>retours utilisateurs hétérogènes sur le SAV, à considérer comme un signal qualitatif plutôt qu’une mesure représentative.</li>
</ul>
<h2 id="verdict">Verdict : à qui fait-on confiance à BOOX ?</h2>
<p><strong>BOOX est un bon choix si vous savez pourquoi vous avez besoin d’Android et si vous acceptez de gérer un appareil plus configurable.</strong> La marque apporte une vraie valeur aux utilisateurs avancés de PDF, aux professionnels avec des applications spécifiques et à ceux qui veulent éviter un écosystème trop fermé. Pour un usage simple de carnet, cette liberté peut au contraire devenir une charge inutile.</p>
<p>Avant achat, nous vérifierions systématiquement quatre points : version Android du modèle, durée restante dans la fenêtre de mises à jour, conditions de garantie du vendeur et politique de retour applicable à l’entrepôt choisi. Pour le choix matériel, voir {internal_link('/marques/boox/', 'la gamme BOOX')} et {internal_link('/comparatifs/remarkable-vs-boox/', 'reMarkable vs BOOX')}.</p>
<h2 id="methode">Sur quoi repose cet avis ?</h2>
<p>Les informations sur les mises à jour, la garantie, les retours, le compte ONYX, le cloud et la confidentialité proviennent de la documentation BOOX consultée le {VERIFIED_AT}. Les observations sur l’expérience produit viennent d’essais indépendants. Les avis clients publics servent uniquement à identifier des thèmes récurrents à vérifier ; ils ne sont pas transformés en statistiques ni présentés comme notre propre expérience.</p>
<h2 id="sources">Sources consultées</h2>
<h3>Documentation BOOX</h3>{_source_list(official)}
<h3>Essais et retours indépendants</h3>{_source_list(independent)}
'''


def enriched_body(url, body):
    if url == '/marques/remarkable/accessoires/':
        return _remarkable_accessories()
    if url == '/marques/boox/accessoires/':
        return _boox_accessories()
    if url == '/marques/boox/avis/':
        return _boox_review()
    return body
