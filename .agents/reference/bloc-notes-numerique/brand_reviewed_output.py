from brand_data import VERIFIED_AT, BRAND_SOURCES, BRANDS
from brand_render_common import internal_link, range_table, ecosystem_table, sources_html

PILOT_URLS = {
    '/marques/remarkable/',
    '/marques/remarkable/remarkable-paper-pro/',
    '/marques/remarkable/remarkable-paper-pro-avis/',
}

BRAND_LINKS = {
    'boox': [
        ('famille Note Air', '/marques/boox/boox-note-air/'),
        ('famille Tab Ultra', '/marques/boox/boox-tab-ultra/'),
        ('avis BOOX', '/marques/boox/avis/'),
        ('accessoires BOOX', '/marques/boox/accessoires/'),
        ('alternatives à BOOX', '/marques/boox/alternatives/'),
        ('reMarkable vs BOOX', '/comparatifs/remarkable-vs-boox/'),
        ('BOOX vs Supernote', '/comparatifs/boox-vs-supernote/'),
    ],
    'kindle': [
        ('Kindle Scribe vs reMarkable', '/comparatifs/kindle-scribe-vs-remarkable/'),
        ('Kindle Scribe vs Kobo Elipsa', '/comparatifs/kindle-scribe-vs-kobo-elipsa/'),
        ('liseuse ou bloc-notes numérique', '/guides/liseuse-ou-bloc-notes-numerique/'),
        ('Google Drive', '/guides/bloc-notes-numerique-google-drive/'),
        ('OneDrive', '/guides/bloc-notes-numerique-onedrive/'),
    ],
    'kobo': [
        ('Kobo Elipsa vs reMarkable', '/comparatifs/kobo-elipsa-vs-remarkable/'),
        ('Kindle Scribe vs Kobo Elipsa', '/comparatifs/kindle-scribe-vs-kobo-elipsa/'),
        ('lecture et prise de notes', '/usages/lecture-et-prise-de-notes/'),
        ('annoter un PDF', '/guides/annoter-pdf-tablette-e-ink/'),
        ('formats compatibles', '/guides/formats-fichiers-compatibles/'),
    ],
    'supernote': [
        ('reMarkable vs Supernote', '/comparatifs/remarkable-vs-supernote/'),
        ('BOOX vs Supernote', '/comparatifs/boox-vs-supernote/'),
        ('modèles sans abonnement', '/comparatifs/bloc-notes-numerique-sans-abonnement/'),
        ('bloc-notes pour professionnels', '/comparatifs/bloc-notes-numerique-professionnel/'),
        ('organiser ses notes', '/guides/organiser-notes-numeriques/'),
    ],
}

BRAND_INTROS = {
    'boox': (
        'BOOX convient surtout aux utilisateurs qui veulent garder la liberté d’Android sur un écran E Ink.',
        'La marque couvre des formats très différents, du 10,3 pouces léger au 13,3 pouces, avec des modèles couleur et noir et blanc. Cette ouverture est son principal avantage, mais aussi la source d’une plus grande complexité.'
    ),
    'kindle': (
        'Kindle Scribe est d’abord un Kindle grand format auquel Amazon a ajouté une vraie couche d’écriture.',
        'Le choix est cohérent si la lecture Kindle reste centrale et que les carnets ou annotations viennent compléter cet usage. Les générations récentes ont gagné des connexions vers Google Drive, OneDrive et OneNote, sans devenir pour autant des tablettes Android.'
    ),
    'kobo': (
        'Kobo Elipsa 2E vise surtout les lecteurs Kobo qui veulent annoter des PDF et tenir des carnets sur le même appareil.',
        'Son intérêt tient davantage à la continuité entre lecture, stylet et carnets qu’à la richesse logicielle. Les limites d’export des annotations EPUB restent un point important si vos notes doivent circuler hors de la liseuse.'
    ),
    'supernote': (
        'Supernote se distingue par une approche très structurée de la prise de notes, avec liens entre pages, reconnaissance manuscrite et organisation de connaissances.',
        'Manta et Nomad répondent à deux besoins de format différents. L’écosystème est plus spécialisé qu’Android, mais il met davantage l’accent sur la durée de vie, l’organisation et la continuité des notes.'
    ),
}


def _source_list(items):
    return '<ul class="source-list">' + ''.join(
        f'<li><a href="{url}" rel="noopener noreferrer">{label}</a></li>'
        for label, url in items
    ) + '</ul>'


def _links_list(items):
    return '<ul>' + ''.join(f'<li>{internal_link(url, label)}</li>' for label, url in items) + '</ul>'


def _brand_hub(brand):
    b = BRANDS[brand]
    intro, context = BRAND_INTROS[brand]
    return f'''
<p class="article-answer"><strong>{intro}</strong> {context}</p>
<h2 id="gamme">La gamme à regarder en 2026</h2>
<p>Le nom de la marque ne suffit pas pour choisir : génération, taille d’écran, couleur et version du système peuvent modifier fortement l’usage. La gamme ci-dessous reprend les modèles actuellement documentés ou encore pertinents dans la comparaison.</p>
{range_table(brand)}
<h2 id="ecosysteme">Ce que l’écosystème change au quotidien</h2>
<p>{b['positioning'].capitalize()}.</p>
{ecosystem_table(brand)}
<p>La différence la plus utile à examiner est la circulation d’un document : comment il entre dans l’appareil, comment il est annoté ou classé, puis dans quel format il ressort. Le guide sur {internal_link('/guides/ecosysteme-ouvert-ou-ferme/', 'les écosystèmes ouverts et fermés')} permet de comparer ce point avec les autres marques.</p>
<h2 id="forces">Les points qui font réellement la différence</h2>
<ul>{''.join(f'<li>{item}</li>' for item in b['strengths'])}</ul>
<h2 id="limites">Les limites à vérifier avant d’acheter</h2>
<ul>{''.join(f'<li>{item}</li>' for item in b['limits'])}</ul>
<p>Si une de ces limites touche une tâche indispensable, mieux vaut comparer directement une autre marque plutôt que compenser après l’achat.</p>
<h2 id="profils">À qui cette marque convient-elle le mieux ?</h2>
<p><strong>Le choix est cohérent si :</strong></p>
<ul>{''.join(f'<li>{item}</li>' for item in b['choose'])}</ul>
<p><strong>Elle est moins adaptée si :</strong></p>
<ul>{''.join(f'<li>{item}</li>' for item in b['avoid'])}</ul>
<h2 id="suite">Comparer les modèles et les alternatives</h2>
{_links_list(BRAND_LINKS[brand])}
<h2 id="sources">Sources consultées</h2>
<p>Gamme, fonctions et compatibilités susceptibles d’évoluer vérifiées le {VERIFIED_AT}.</p>
{sources_html([brand], 8)}
'''


def _directory():
    rows = []
    for key in ['remarkable', 'boox', 'kindle', 'kobo', 'supernote']:
        b = BRANDS[key]
        name = b['name']
        url = {
            'remarkable': '/marques/remarkable/',
            'boox': '/marques/boox/',
            'kindle': '/marques/kindle-scribe/',
            'kobo': '/marques/kobo-elipsa/',
            'supernote': '/marques/supernote/',
        }[key]
        rows.append(f'<tr><td>{internal_link(url, name)}</td><td>{b["positioning"]}</td></tr>')
    return f'''
<p class="article-answer"><strong>reMarkable, BOOX, Kindle Scribe, Kobo Elipsa et Supernote ne répondent pas au même besoin.</strong> La différence principale se joue moins sur la technologie E Ink elle-même que sur le logiciel, les formats, le cloud, les applications et la façon d’organiser les notes.</p>
<h2 id="comparaison">Cinq écosystèmes, cinq logiques différentes</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Marque</th><th>Ce qui la distingue</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>
<h2 id="choisir">Quelle marque regarder en premier ?</h2>
<ul>
<li><strong>reMarkable</strong> si vous privilégiez une expérience spécialisée et peu distraite.</li>
<li><strong>BOOX</strong> si Android, les applications tierces et la compatibilité de formats sont prioritaires.</li>
<li><strong>Kindle Scribe</strong> si votre bibliothèque Kindle reste au centre de l’usage.</li>
<li><strong>Kobo Elipsa 2E</strong> si vous lisez surtout chez Kobo et voulez ajouter carnets et PDF annotés.</li>
<li><strong>Supernote</strong> si l’organisation des notes et des connaissances compte davantage qu’un grand catalogue d’applications.</li>
</ul>
<h2 id="criteres">Les critères qui évitent un mauvais choix</h2>
<p>Avant de comparer les modèles, notez les applications indispensables, le type de documents que vous manipulez, le cloud déjà utilisé et la façon dont vous devez exporter vos notes. Une marque peut être excellente pour l’écriture et rester inadaptée si elle bloque un de ces quatre points.</p>
<p>Vous pouvez ensuite passer au {internal_link('/comparatifs/meilleur-bloc-notes-numerique/', 'comparatif général')} ou au {internal_link('/guides/choisir-bloc-notes-numerique/', 'guide de choix')}.</p>
<h2 id="sources">Sources consultées</h2>
<p>Les gammes et écosystèmes ont été vérifiés le {VERIFIED_AT} à partir des documentations officielles des fabricants.</p>
{sources_html(['remarkable','boox','kindle','kobo','supernote'], 10)}
'''


def _remarkable_2_product():
    return f'''
<p class="article-answer"><strong>En 2026, reMarkable 2 n’est plus le modèle neuf de référence.</strong> reMarkable l’indique comme discontinuée et oriente désormais sa gamme vers Paper Pure, Paper Pro Move et Paper Pro. Elle reste surtout intéressante pour les propriétaires actuels ou en reconditionné si le prix compense clairement son âge.</p>
<h2 id="statut">Une ancienne génération encore utilisable</h2>
<p>reMarkable 2 conserve un écran 10,3 pouces noir et blanc, les carnets, l’annotation PDF, les dossiers, les étiquettes, la conversion manuscrite et les intégrations cloud déjà ajoutées au fil des mises à jour. Son statut change toutefois la décision d’achat : disponibilité des accessoires, état de la batterie et prix du reconditionné pèsent davantage qu’à l’époque où elle était le modèle principal.</p>
<h2 id="caracteristiques">Les caractéristiques qui comptent encore</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Point</th><th>reMarkable 2</th></tr></thead><tbody>
<tr><td><strong>Écran</strong></td><td>10,3 pouces Canvas, noir et blanc</td></tr>
<tr><td><strong>Éclairage</strong></td><td>aucun éclairage frontal</td></tr>
<tr><td><strong>Usage</strong></td><td>notes, PDF, conversion manuscrite</td></tr>
<tr><td><strong>Cloud</strong></td><td>Google Drive, Dropbox et OneDrive via l’écosystème reMarkable</td></tr>
<tr><td><strong>Autonomie annoncée</strong></td><td>jusqu’à deux semaines selon le fabricant</td></tr>
<tr><td><strong>Stylet</strong></td><td>Marker / Marker Plus de génération reMarkable 2</td></tr>
</tbody></table></div>
<h2 id="compatibilite">Le principal piège : les accessoires</h2>
<p>Les Markers de reMarkable 2 ne sont pas compatibles avec la génération Paper actuelle. Si vous possédez déjà un Folio ou un Marker, vérifiez donc précisément ce qui peut être réutilisé avant de comparer le coût avec un modèle plus récent.</p>
<h2 id="occasion">Que vérifier en occasion ou reconditionné ?</h2>
<ul>
<li>l’état de la batterie et la régularité de la charge ;</li>
<li>l’état de l’écran et du port USB-C ;</li>
<li>la présence et l’état du Marker ;</li>
<li>l’écart de prix réel avec Paper Pure ou un modèle actuel.</li>
</ul>
<p>À prix proche d’un modèle neuf récent, l’intérêt baisse fortement. Voir aussi {internal_link('/bons-plans/bloc-notes-numerique-occasion/', 'le guide sur l’occasion')}.</p>
<h2 id="limites">Les limites à accepter</h2>
<ul><li>produit discontinué ;</li><li>pas de couleur ;</li><li>pas d’éclairage frontal ;</li><li>ancienne génération d’accessoires.</li></ul>
<h2 id="choix">Pour qui reste-t-elle cohérente ?</h2>
<p>Elle convient encore si vous la possédez déjà, si vous trouvez un reconditionné nettement moins cher ou si vous cherchez uniquement un carnet noir et blanc très spécialisé. Pour un achat neuf au prix d’un modèle actuel, mieux vaut repartir de {internal_link('/marques/remarkable/', 'la gamme reMarkable 2026')}.</p>
<h2 id="sources">Sources consultées</h2>
<p>Statut et caractéristiques vérifiés le {VERIFIED_AT}.</p>{sources_html(['remarkable'], 6)}
'''


def _boox_note_air_product():
    return f'''
<p class="article-answer"><strong>La famille BOOX Note Air est aujourd’hui représentée par le Note Air5 C, un modèle 10,3 pouces couleur sous Android 15.</strong> Il vise ceux qui veulent combiner notes manuscrites, PDF et applications Android sans passer à un grand écran 13,3 pouces.</p>
<h2 id="modele">Le Note Air5 C est le modèle actuel à comparer</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Point</th><th>Note Air5 C</th></tr></thead><tbody>
<tr><td><strong>Écran</strong></td><td>10,3 pouces Kaleido 3, 300 ppp en noir et blanc / 150 ppp en couleur</td></tr>
<tr><td><strong>Système</strong></td><td>Android 15</td></tr>
<tr><td><strong>Mémoire</strong></td><td>6 Go de RAM / 64 Go de stockage</td></tr>
<tr><td><strong>Stylet</strong></td><td>BOOX Pen3 inclus</td></tr>
<tr><td><strong>Extension</strong></td><td>microSD et clavier cover compatibles</td></tr>
</tbody></table></div>
<h2 id="android">Ce qu’Android change réellement</h2>
<p>Le Note Air5 C peut conserver des applications de lecture, de cloud ou de productivité que reMarkable ou Kindle n’exécutent pas directement. BOOX ajoute ses propres outils Notes et NeoReader pour les PDF, mais Google Play élargit nettement les possibilités.</p>
<p>Cette ouverture demande davantage de réglages : toutes les applications Android ne sont pas conçues pour E Ink, et les modes de rafraîchissement peuvent devoir être adaptés selon l’usage.</p>
<h2 id="couleur">Couleur et clavier : utiles selon le travail</h2>
<p>Kaleido 3 apporte de la couleur pour les schémas, surlignages et documents illustrés, avec une saturation plus limitée qu’un écran LCD ou OLED. Le clavier optionnel peut être pertinent pour de la saisie ponctuelle, mais il ne transforme pas l’E Ink en écran de laptop.</p>
<h2 id="limites">Les limites à connaître</h2>
<ul><li>interface plus riche et plus complexe qu’un carnet spécialisé ;</li><li>rendu des applications tierces variable sur E Ink ;</li><li>couleur moins vive qu’un écran classique ;</li><li>gamme BOOX qui évolue rapidement, avec génération et version Android à vérifier.</li></ul>
<h2 id="choix">Pour qui le Note Air5 C est-il cohérent ?</h2>
<p>Il convient surtout si vous voulez Android, la couleur, de nombreux PDF et plusieurs services cloud sur un format 10,3 pouces. Si vous cherchez d’abord une interface minimaliste, le {internal_link('/comparatifs/remarkable-vs-boox/', 'comparatif reMarkable vs BOOX')} aide à mesurer le compromis.</p>
<h2 id="sources">Sources consultées</h2>
<p>Caractéristiques et fonctions vérifiées le {VERIFIED_AT}.</p>{sources_html(['boox'], 7)}
'''


def _boox_tab_ultra_product():
    return f'''
<p class="article-answer"><strong>BOOX Tab Ultra C Pro reste une tablette E Ink couleur très équipée, mais ce n’est plus le point de comparaison le plus récent de la gamme BOOX.</strong> Son Android 12, son clavier avec trackpad et sa caméra arrière en font un produit particulier, à comparer avec Note Air5 C ou les grands formats actuels avant achat.</p>
<h2 id="positionnement">Une logique de tablette PC E Ink</h2>
<p>La famille Tab Ultra pousse plus loin la polyvalence que les carnets E Ink classiques : applications Android, clavier, caméra et stockage extensible font partie du positionnement. Cette richesse n’est utile que si ces fonctions remplacent réellement une partie du travail fait sur ordinateur.</p>
<h2 id="caracteristiques">Les caractéristiques à retenir</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Point</th><th>Tab Ultra C Pro</th></tr></thead><tbody>
<tr><td><strong>Écran</strong></td><td>10,3 pouces Kaleido 3</td></tr>
<tr><td><strong>Système</strong></td><td>Android 12</td></tr>
<tr><td><strong>Mémoire</strong></td><td>6 Go de RAM / 128 Go</td></tr>
<tr><td><strong>Clavier</strong></td><td>cover magnétique avec trackpad</td></tr>
<tr><td><strong>Caméra</strong></td><td>16 MP arrière</td></tr>
<tr><td><strong>Stockage</strong></td><td>microSD</td></tr>
</tbody></table></div>
<h2 id="limites">Pourquoi l’ancienneté du système compte</h2>
<p>Android 12 est plus ancien que l’Android 15 du Note Air5 C. Pour un produit acheté en 2026, cela mérite d’être intégré à la durée d’usage attendue, surtout si vous dépendez d’applications tierces ou de politiques de sécurité d’entreprise.</p>
<ul><li>poids et complexité supérieurs à un carnet minimaliste ;</li><li>caméra et clavier inutiles si votre besoin reste l’écriture manuscrite ;</li><li>écran 10,3 pouces malgré un positionnement très orienté productivité.</li></ul>
<h2 id="choix">Quand le Tab Ultra C Pro garde-t-il du sens ?</h2>
<p>Il reste cohérent si vous voulez précisément le trio clavier + applications Android + E Ink sur 10,3 pouces. Si votre priorité est un Android plus récent, commencez plutôt par {internal_link('/marques/boox/boox-note-air/', 'la famille Note Air')}. Pour davantage de simplicité, comparez avec {internal_link('/marques/remarkable/', 'reMarkable')}.</p>
<h2 id="sources">Sources consultées</h2>
<p>Caractéristiques et génération vérifiées le {VERIFIED_AT}.</p>{sources_html(['boox'], 8)}
'''


def _remarkable_2_review():
    independent = [
        ('TechRadar — reMarkable 2 review', 'https://www.techradar.com/reviews/remarkable-2-tablet'),
        ('WIRED — Review: reMarkable 2', 'https://www.wired.com/review/remarkable-2/'),
        ('Tom’s Guide — reMarkable 2 review', 'https://www.tomsguide.com/reviews/remarkable-2-review'),
    ]
    return f'''
<p class="article-answer"><strong>Notre avis en 2026 : reMarkable 2 reste un très bon carnet numérique pour l’écriture, mais son statut discontinué rend un achat neuf difficile à défendre face aux modèles actuels.</strong> Cette évaluation croise la documentation reMarkable avec des essais indépendants réalisés lorsque le produit était encore au cœur de la gamme ; nous n’avons pas réalisé de test physique de notre côté.</p>
<h2 id="forces">Ce qui reste convaincant</h2>
<p>Les essais de TechRadar, WIRED et Tom’s Guide convergent sur la finesse du châssis, la qualité de l’expérience d’écriture et le caractère très focalisé de l’appareil. Pour quelqu’un qui l’utilise déjà comme carnet de réunions ou d’écriture longue, ces qualités ne disparaissent pas parce qu’un successeur existe.</p>
<h2 id="age">Ce que 2026 change dans le verdict</h2>
<p>Le problème n’est plus seulement la fiche technique. reMarkable 2 est désormais discontinuée, sans couleur ni éclairage frontal, et ses Markers appartiennent à une génération différente de la gamme Paper. Un produit qui était pertinent à son lancement peut donc devenir moins rationnel à prix proche d’un modèle récent.</p>
<h2 id="limites">Les limites qui pèsent le plus aujourd’hui</h2>
<ul><li>absence d’éclairage frontal ;</li><li>pas de couleur ;</li><li>ancienne génération d’accessoires ;</li><li>achat d’occasion ou reconditionné qui impose de vérifier batterie et état général.</li></ul>
<p>Les critiques historiques sur le manque d’applications et la spécialisation restent également valables : ce n’est pas une tablette généraliste.</p>
<h2 id="pour-qui">À qui la conseiller encore ?</h2>
<p>Aux propriétaires actuels, oui. À un acheteur reconditionné, éventuellement, si le prix est nettement inférieur à Paper Pure et que le noir et blanc suffit. Pour un achat neuf au tarif d’un modèle actuel, notre préférence va vers la {internal_link('/marques/remarkable/', 'gamme reMarkable actuelle')}.</p>
<h2 id="verdict">Verdict</h2>
<p><strong>reMarkable 2 reste agréable à utiliser, mais elle doit désormais être jugée comme une ancienne génération, pas comme le choix par défaut de la marque.</strong> Son intérêt dépend surtout du prix et de l’état de l’exemplaire.</p>
<h2 id="methode">Sur quoi repose cet avis ?</h2>
<p>Le statut 2026, les compatibilités et les fonctions encore documentées viennent de reMarkable. Les observations sur l’écriture, le design et les limites d’usage proviennent d’essais indépendants. Nous distinguons ces deux niveaux de preuve et ne revendiquons aucune expérience pratique propre.</p>
<h2 id="sources">Sources consultées</h2>
<h3>Sources officielles</h3>{sources_html(['remarkable'], 6)}
<h3>Essais indépendants</h3>{_source_list(independent)}
'''


def _boox_review():
    independent = [
        ('TechRadar — Onyx BOOX Note Air5 C review', 'https://www.techradar.com/tablets/ereaders/onyx-boox-note-air5-c-review'),
        ('Digital Trends — BOOX Note Air5 C hands-on review', 'https://www.digitaltrends.com/tablets/i-tested-an-ai-powered-kindle-scribe-rival-and-it-shows-how-far-behind-amazon-is/'),
    ]
    return f'''
<p class="article-answer"><strong>Notre avis : BOOX est l’un des choix les plus flexibles si Android, les PDF et les applications tierces sont prioritaires, mais cette liberté demande davantage de réglages qu’un reMarkable ou un Kindle Scribe.</strong> L’analyse s’appuie sur la documentation BOOX et sur des essais indépendants de modèles actuels, notamment le Note Air5 C ; nous ne présentons pas ces observations comme un test maison.</p>
<h2 id="forces">Pourquoi BOOX se distingue</h2>
<p>Android et Google Play changent profondément l’usage : services de cloud, applications de lecture, outils de productivité et logiciels métier peuvent rester disponibles sur l’appareil. BOOX ajoute ses propres outils Notes et NeoReader, particulièrement riches pour les PDF.</p>
<p>TechRadar et Digital Trends décrivent le Note Air5 C comme un appareil très polyvalent, avec une bonne expérience au stylet et un niveau de personnalisation élevé. Cette polyvalence est cohérente avec le positionnement global de la marque.</p>
<h2 id="complexite">La contrepartie : plus de réglages et plus de variations</h2>
<p>La liberté Android n’est pas gratuite. Les applications ne sont pas toutes optimisées pour E Ink, et BOOX propose de nombreux réglages de rafraîchissement, contraste et couleur. Pour un utilisateur qui veut simplement ouvrir un carnet et écrire, cette richesse peut devenir une friction.</p>
<h2 id="gamme">Une gamme qu’il faut lire modèle par modèle</h2>
<p>Go 10.3 Gen II, Note Air5 C, Note Max, Tab X C et les familles plus anciennes ne partagent ni le même format, ni toujours la même version Android. Le nom BOOX ne suffit donc pas pour juger la durée de support, le stylet ou l’usage.</p>
<h2 id="limites">Les limites à garder en tête</h2>
<ul><li>courbe d’apprentissage plus élevée ;</li><li>applications Android inégales sur E Ink ;</li><li>gamme qui évolue vite ;</li><li>arbitrage entre vitesse de rafraîchissement, qualité d’image et autonomie.</li></ul>
<h2 id="pour-qui">À qui BOOX convient-il le mieux ?</h2>
<p>Aux utilisateurs avancés de PDF, aux professionnels qui doivent conserver des applications précises et à ceux qui acceptent de configurer l’appareil. Si votre priorité est une expérience beaucoup plus cadrée, comparez avec {internal_link('/comparatifs/remarkable-vs-boox/', 'reMarkable vs BOOX')} ou {internal_link('/comparatifs/boox-vs-supernote/', 'BOOX vs Supernote')}.</p>
<h2 id="verdict">Verdict</h2>
<p><strong>BOOX offre probablement le plus de liberté parmi les grandes marques de bloc-notes E Ink, mais ce n’est pas le choix le plus simple.</strong> Sa valeur vient précisément d’Android, des formats et des réglages ; si vous n’en avez pas besoin, une solution plus spécialisée peut être plus agréable.</p>
<h2 id="methode">Sur quoi repose cet avis ?</h2>
<p>Les informations de gamme, Android, cloud, notes et formats viennent de la documentation BOOX vérifiée le {VERIFIED_AT}. Les observations sur le Note Air5 C proviennent d’essais indépendants de TechRadar et Digital Trends. Nous n’avons pas réalisé de test physique des appareils BOOX.</p>
<h2 id="sources">Sources consultées</h2>
<h3>Sources officielles</h3>{sources_html(['boox'], 8)}
<h3>Essais indépendants</h3>{_source_list(independent)}
'''


def _connect_service():
    return f'''
<p class="article-answer"><strong>reMarkable Connect n’est pas nécessaire pour écrire sur une tablette reMarkable.</strong> Il devient surtout pertinent si vous utilisez intensivement le cloud, la recherche manuscrite et les applications reMarkable sur plusieurs appareils.</p>
<h2 id="sans">Ce qui reste disponible sans abonnement</h2>
<p>Les fonctions de base d’écriture et de consultation restent sur la tablette. Sans Connect, le principal point à surveiller est le fonctionnement du cloud et des applications : reMarkable limite notamment le stockage cloud aux fichiers utilisés et synchronisés pendant une période définie.</p>
<h2 id="avec">Ce que Connect ajoute</h2>
<ul><li>stockage cloud illimité annoncé ;</li><li>recherche dans l’écriture manuscrite ;</li><li>fonctions supplémentaires dans les applications mobile et desktop ;</li><li>intégrations et services associés selon l’offre en cours.</li></ul>
<h2 id="cout">Quand le coût récurrent est-il justifié ?</h2>
<p>Si vous travaillez chaque jour entre tablette, ordinateur et téléphone, Connect peut faire partie du workflow. Si vous écrivez surtout localement et exportez ponctuellement des PDF, l’abonnement peut avoir beaucoup moins de valeur. Le bon calcul consiste donc à partir des fonctions réellement utilisées, pas du bundle commercial.</p>
<h2 id="dependance">La dépendance au cloud à vérifier</h2>
<p>Avant de vous abonner, vérifiez comment récupérer vos notes et documents si vous arrêtez le service. Les guides sur {internal_link('/guides/exporter-notes/', 'l’export des notes')} et {internal_link('/guides/bloc-notes-numerique-avec-ou-sans-abonnement/', 'les appareils avec ou sans abonnement')} permettent de replacer Connect dans un choix plus large.</p>
<h2 id="limites">Les limites à garder en tête</h2>
<ul><li>coût récurrent ;</li><li>certaines fonctions utiles restent liées au service ;</li><li>la valeur de l’abonnement dépend fortement d’un usage multi-appareils.</li></ul>
<h2 id="sources">Sources consultées</h2>
<p>Fonctions Connect vérifiées le {VERIFIED_AT}.</p>{sources_html(['remarkable'], 6)}
'''


def _accessories(brand):
    if brand == 'remarkable':
        return f'''
<p class="article-answer"><strong>Chez reMarkable, l’accessoire le plus important est d’abord celui qui est compatible avec votre génération.</strong> Marker, Folio et Type Folio ne doivent pas être considérés comme un bundle automatique.</p>
<h2 id="compatibilite">Compatibilité avant tout</h2>
<p>Les Markers de reMarkable 2 ne sont pas interchangeables avec la génération Paper actuelle. Les Folios dépendent eux aussi du modèle et de ses dimensions. Vérifiez donc le nom exact de la tablette avant d’acheter un accessoire, même officiel.</p>
<h2 id="marker">Marker ou Marker Plus ?</h2>
<p>Un Marker est nécessaire pour écrire. Le Marker Plus ajoute surtout une gomme à son extrémité. Si cette fonction n’est pas importante dans votre manière de corriger, le surcoût n’est pas indispensable.</p>
<h2 id="folio">Folio et protection</h2>
<p>Un Folio devient utile si la tablette voyage régulièrement. Pour un appareil qui reste principalement sur un bureau, la protection a moins de poids dans la décision que le stylet ou la compatibilité.</p>
<h2 id="type-folio">Type Folio : seulement si vous tapez réellement</h2>
<p>Le clavier a du sens si vous comptez rédiger de longs passages sur la tablette. Sinon, il ajoute surtout du coût et du poids à un appareil acheté pour l’écriture manuscrite.</p>
<h2 id="budget">Construire un panier réaliste</h2>
<p>Commencez par le modèle et le stylet nécessaires, puis ajoutez protection et clavier selon vos usages. Le guide sur {internal_link('/guides/prix-bloc-notes-numerique/', 'le prix réel')} permet de comparer des configurations équivalentes.</p>
<h2 id="sources">Sources consultées</h2>{sources_html(['remarkable'], 7)}
'''
    return f'''
<p class="article-answer"><strong>Les accessoires BOOX dépendent fortement du modèle et de sa génération.</strong> Stylet, étui, clavier et stockage ne sont pas universels dans une gamme qui couvre plusieurs tailles et technologies.</p>
<h2 id="compatibilite">Vérifier le modèle exact</h2>
<p>Pen3, Pen Plus ou autres stylets BOOX ne sont pas interchangeables dans tous les cas. Les étuis et claviers dépendent aussi des dimensions et des connectiques du modèle. Sur une gamme qui évolue vite, le nom commercial précis compte davantage que le logo BOOX.</p>
<h2 id="stylet">Le stylet est le premier accessoire à vérifier</h2>
<p>Il est indispensable pour l’écriture, mais son modèle varie selon les appareils. Vérifiez les fonctions de gomme, les mines et la compatibilité avant d’acheter un remplacement ou un second stylet.</p>
<h2 id="clavier">Clavier : utile surtout sur les modèles orientés productivité</h2>
<p>Un clavier est cohérent si vous utilisez réellement Android pour saisir des textes. Sur un usage centré sur PDF et notes manuscrites, il peut devenir un accessoire coûteux et peu utilisé.</p>
<h2 id="stockage">microSD et stockage</h2>
<p>Le slot microSD existe sur certains modèles et peut être pertinent pour de grosses bibliothèques de PDF ou documents locaux. Vérifiez sa présence sur le modèle choisi plutôt que de l’assumer au niveau de la marque.</p>
<h2 id="budget">Comparer le coût complet</h2>
<p>Tablette, stylet, étui et clavier doivent être comparés ensemble si ces accessoires font réellement partie de votre usage. Voir {internal_link('/guides/prix-bloc-notes-numerique/', 'le guide sur le coût total')}.</p>
<h2 id="sources">Sources consultées</h2>{sources_html(['boox'], 8)}
'''


def _alternatives(brand):
    if brand == 'remarkable':
        return f'''
<p class="article-answer"><strong>La meilleure alternative à reMarkable dépend de ce qui vous gêne dans son écosystème.</strong> Android, organisation des notes, lecture ou coût ne conduisent pas vers le même concurrent.</p>
<h2 id="android">Si vous voulez davantage d’applications : BOOX</h2>
<p>BOOX est le choix le plus logique si l’absence d’applications tierces est votre principale limite. Android, Google Play et une compatibilité documentaire large apportent plus de liberté, avec davantage de réglages en contrepartie. Voir {internal_link('/comparatifs/remarkable-vs-boox/', 'reMarkable vs BOOX')}.</p>
<h2 id="organisation">Si vous voulez mieux structurer les notes : Supernote</h2>
<p>Supernote met davantage l’accent sur les liens entre notes, l’organisation de connaissances et la continuité du travail manuscrit. Voir {internal_link('/comparatifs/remarkable-vs-supernote/', 'reMarkable vs Supernote')}.</p>
<h2 id="lecture">Si la lecture passe avant l’écriture : Kindle ou Kobo</h2>
<p>Kindle Scribe est plus cohérent pour une bibliothèque Amazon ; Kobo Elipsa 2E pour un usage centré Kobo. Ces appareils restent plus proches d’une liseuse enrichie que d’une tablette Android.</p>
<h2 id="cout">Si l’abonnement ou le coût vous gêne</h2>
<p>Comparez le coût complet, y compris stylet, protection et service cloud. Le {internal_link('/comparatifs/bloc-notes-numerique-sans-abonnement/', 'comparatif sans abonnement')} évite de remplacer un coût récurrent par un panier matériel plus cher.</p>
<h2 id="choix">Quel critère doit décider ?</h2>
<p>Partez de la limite qui vous pousse à quitter reMarkable, puis choisissez une alternative qui la corrige sans sacrifier votre usage principal. Une marque plus ouverte n’est pas automatiquement meilleure si vous perdez la simplicité qui vous convenait.</p>
<h2 id="sources">Sources consultées</h2>{sources_html(['remarkable','boox','supernote','kindle','kobo'], 10)}
'''
    return f'''
<p class="article-answer"><strong>La meilleure alternative à BOOX dépend surtout de la raison pour laquelle Android et la richesse des réglages ne vous conviennent plus.</strong> Simplicité, organisation des notes et lecture mènent vers des choix différents.</p>
<h2 id="simplicite">Si vous voulez moins de réglages : reMarkable</h2>
<p>reMarkable réduit volontairement le nombre d’applications et concentre l’expérience sur l’écriture, les documents et son propre écosystème. Le compromis est une ouverture logicielle plus faible. Voir {internal_link('/comparatifs/remarkable-vs-boox/', 'reMarkable vs BOOX')}.</p>
<h2 id="organisation">Si l’organisation des notes passe avant Android : Supernote</h2>
<p>Supernote est pertinent si liens entre notes, structure et continuité manuscrite comptent davantage que Google Play. Voir {internal_link('/comparatifs/boox-vs-supernote/', 'BOOX vs Supernote')}.</p>
<h2 id="lecture">Si vous voulez surtout lire : Kindle ou Kobo</h2>
<p>Kindle Scribe et Kobo Elipsa 2E sont plus simples si votre bibliothèque de livres est centrale et que la prise de notes reste secondaire.</p>
<h2 id="garder-boox">Quand rester chez BOOX ?</h2>
<p>Si vous utilisez réellement des applications Android, plusieurs clouds ou des fonctions PDF avancées, quitter BOOX peut créer plus de friction que de simplicité. Dans ce cas, changer de modèle au sein de la gamme peut être plus rationnel que changer d’écosystème.</p>
<h2 id="choix">Choisir selon votre besoin principal</h2>
<p>Ne comparez pas les alternatives sur le nombre total de fonctions. Comparez la tâche qui pose problème aujourd’hui : application indispensable, organisation des notes, lecture, taille d’écran ou budget.</p>
<h2 id="sources">Sources consultées</h2>{sources_html(['boox','remarkable','supernote','kindle','kobo'], 10)}
'''


def reviewed_body(url, page_data):
    if url in PILOT_URLS:
        return page_data['body']

    if url == '/marques/':
        return _directory()
    if url == '/marques/boox/':
        return _brand_hub('boox')
    if url == '/marques/kindle-scribe/':
        return _brand_hub('kindle')
    if url == '/marques/kobo-elipsa/':
        return _brand_hub('kobo')
    if url == '/marques/supernote/':
        return _brand_hub('supernote')

    if url == '/marques/remarkable/remarkable-2/':
        return _remarkable_2_product()
    if url == '/marques/boox/boox-note-air/':
        return _boox_note_air_product()
    if url == '/marques/boox/boox-tab-ultra/':
        return _boox_tab_ultra_product()

    if url == '/marques/remarkable/remarkable-2-avis/':
        return _remarkable_2_review()
    if url == '/marques/boox/avis/':
        return _boox_review()

    if url == '/marques/remarkable/abonnement-connect/':
        return _connect_service()
    if url == '/marques/remarkable/accessoires/':
        return _accessories('remarkable')
    if url == '/marques/boox/accessoires/':
        return _accessories('boox')
    if url == '/marques/remarkable/alternatives/':
        return _alternatives('remarkable')
    if url == '/marques/boox/alternatives/':
        return _alternatives('boox')

    return page_data['body']
