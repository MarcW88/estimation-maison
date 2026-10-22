from brand_render_common import internal_link


VERIFIED_AT = "9 septembre 2026"


def _source_list(items):
    return '<ul class="source-list">' + ''.join(
        f'<li><a href="{url}" rel="noopener noreferrer">{label}</a></li>'
        for label, url in items
    ) + '</ul>'


def _kindle_hub():
    sources = [
        ("Amazon — identifier les générations Kindle Scribe", "https://digprjsurvey.amazon.com/csad/help/node/GK33S847NN4V6Y83"),
        ("Amazon — connecter Google Drive, OneDrive et OneNote", "https://digprjsurvey.amazon.com/csad/help/node/Tuar1obhcxaS8hVUKd"),
        ("Amazon — importer depuis Google Drive ou OneDrive", "https://digprjsurvey.amazon.com/csad/help/node/TjrMJmg3DZpAQLwVuN"),
        ("Amazon — partager notes et documents vers les services connectés", "https://digprjsurvey.amazon.com/csad/help/node/TP8wuaQilIlwlITVTL"),
        ("Amazon — rechercher dans les carnets Kindle Scribe", "https://digprjsurvey.amazon.com/csad/help/node/TXEroxFZdxObrcesZO"),
        ("Amazon — fonctions d’écriture couleur du Scribe Colorsoft", "https://digprjsurvey.amazon.com/csad/help/node/TTqOsFUasbkY9S4V9x"),
        ("Amazon — calendrier des mises à jour de sécurité Kindle", "https://digprjsurvey.amazon.com/csad/help/node/GF3LDHSB5YM9BYF7"),
    ]
    return f'''
<p class="article-answer"><strong>Le Kindle Scribe reste d’abord un Kindle : c’est le point de départ le plus utile pour décider.</strong> Les modèles 2025–2026 ont nettement renforcé la prise de notes, la recherche manuscrite et les connexions à Google Drive, OneDrive et OneNote. Mais ils restent conçus autour de la bibliothèque Kindle et de flux de documents contrôlés par Amazon, pas comme des tablettes E Ink ouvertes à des applications tierces.</p>

<h2 id="bibliotheque">Commencez par votre bibliothèque, pas par le stylet</h2>
<p>Si vous lisez déjà beaucoup de livres Kindle, le Scribe évite de séparer lecture et écriture entre deux appareils. Vous pouvez conserver votre bibliothèque Kindle, annoter des livres ou documents compatibles et utiliser des carnets sur le même écran. C’est son avantage structurel face à des appareils centrés presque uniquement sur la prise de notes.</p>
<p>À l’inverse, si votre travail repose surtout sur des applications métier, des dossiers cloud synchronisés en permanence ou une organisation de connaissances très poussée, la présence du Kindle Store devient secondaire. Dans ce cas, {internal_link('/comparatifs/kindle-scribe-vs-remarkable/', 'Kindle Scribe vs reMarkable')} ou une comparaison avec BOOX est plus utile qu’un simple choix entre générations de Scribe.</p>

<h2 id="modeles">Trois Scribe récents, trois compromis différents</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Modèle</th><th>Sortie</th><th>Écran / lumière</th><th>Stockage</th><th>Ce qui change la décision</th></tr></thead><tbody>
<tr><td><strong>Kindle Scribe (3e génération)</strong></td><td>2025</td><td>noir et blanc, éclairage réglable</td><td>32 ou 64 Go</td><td>le choix le plus direct si vous voulez lecture Kindle, notes et lumière frontale sans passer à la couleur</td></tr>
<tr><td><strong>Kindle Scribe Colorsoft</strong></td><td>2025</td><td>couleur, éclairage réglable</td><td>32 ou 64 Go</td><td>utile si la couleur apporte quelque chose à vos annotations, schémas ou documents</td></tr>
<tr><td><strong>Kindle Scribe sans éclairage frontal</strong></td><td>2026</td><td>noir et blanc, sans front light</td><td>16 Go</td><td>à regarder si vous travaillez surtout en lumière ambiante et n’avez pas besoin de 32 ou 64 Go</td></tr>
</tbody></table></div>
<p>Amazon documente aussi le Scribe 2024, encore supporté, mais les connexions Google Drive, OneDrive et OneNote décrites ci-dessous nécessitent un Scribe sorti en 2025 ou après. C’est une frontière plus importante qu’une petite différence cosmétique entre générations.</p>

<h2 id="documents">Le cloud est devenu plus utile, mais ce n’est pas une synchronisation de dossier</h2>
<p>Sur les Scribe 2025+, vous pouvez importer une copie d’un fichier compatible depuis Google Drive ou Microsoft OneDrive, l’annoter, puis renvoyer une copie PDF vers le service connecté. Amazon précise que les annotations ajoutées sur le Kindle ne se synchronisent pas automatiquement vers le fichier d’origine. Le bon modèle mental est donc <strong>importer → travailler → exporter une copie</strong>, pas « ouvrir un dossier cloud qui reste synchronisé dans les deux sens ».</p>
<p>Pour les carnets, l’export vers Google Drive ou OneDrive peut conserver l’écriture en PDF, la convertir en texte ou produire un PDF interrogeable. OneNote reçoit les carnets en image PNG ou en texte selon le format choisi. Cette ouverture est réelle, mais elle reste organisée autour des fonctions prévues par Amazon.</p>
<p>Si votre choix dépend de la circulation des fichiers, voyez aussi {internal_link('/guides/synchroniser-notes-cloud/', 'comment synchroniser ses notes dans le cloud')} et {internal_link('/guides/ecosysteme-ouvert-ou-ferme/', 'la différence entre écosystème ouvert et fermé')}.</p>

<h2 id="notes">Les générations 2025+ changent davantage la recherche que l’ouverture logicielle</h2>
<p>Amazon permet désormais de rechercher dans les carnets manuscrits sur les Scribe 2025+, y compris en français. Le Colorsoft ajoute l’écriture, le surlignage et les signets en couleur. Ces fonctions améliorent directement l’usage quotidien sans transformer le Scribe en tablette Android : le catalogue d’applications reste celui d’un Kindle, et non celui de Google Play.</p>
<p>La couleur mérite donc d’être choisie pour un besoin concret — codes couleur, schémas, documents visuels — plutôt que parce qu’elle existe. Pour de longs textes noir et blanc ou de simples carnets, elle n’est pas automatiquement nécessaire.</p>

<h2 id="arbitrages">Les quatre arbitrages à faire avant achat</h2>
<p><strong>Bibliothèque Kindle ou fichiers de travail ?</strong> Plus votre usage est centré sur les livres Kindle, plus le Scribe est cohérent. Plus il dépend de dossiers, apps et outils externes, plus il faut tester la frontière de l’écosystème.</p>
<p><strong>Couleur ou noir et blanc ?</strong> Colorsoft apporte une vraie couche couleur aux notes et annotations ; elle n’est utile que si cette information visuelle compte dans vos documents.</p>
<p><strong>Lumière frontale ou simplicité maximale ?</strong> Le modèle 2026 sans éclairage retire précisément cette fonction. Il faut donc éviter de le choisir si vous lisez souvent le soir ou dans des environnements peu éclairés.</p>
<p><strong>Ancienne génération ou fonctions cloud récentes ?</strong> Le Scribe 2024 reste supporté, mais les connexions Drive/OneDrive/OneNote documentées par Amazon demandent un appareil sorti en 2025 ou après.</p>

<h2 id="sortie">Quand regarder une autre marque</h2>
<p>Si votre besoin principal est la lecture commerciale et quelques carnets, Kindle Scribe reste logiquement bien placé. Si vous voulez surtout une tablette d’écriture spécialisée, {internal_link('/marques/remarkable/', 'reMarkable')} propose une logique différente. Pour organiser des notes reliées et structurées, {internal_link('/marques/supernote/', 'Supernote')} mérite d’être regardé. Et si l’installation d’applications tierces est indispensable, {internal_link('/marques/boox/', 'BOOX')} est plus ouvert.</p>
<p>Pour un face-à-face dans un usage proche, consultez aussi {internal_link('/comparatifs/kindle-scribe-vs-kobo-elipsa/', 'Kindle Scribe vs Kobo Elipsa')}.</p>

<h2 id="sources">Sources vérifiées</h2>
<p>Générations, connexions cloud, recherche manuscrite et fonctions couleur vérifiées le {VERIFIED_AT}. Les conséquences d’usage sont des synthèses éditoriales à partir de cette documentation, pas des observations de test physique propres au site.</p>
{_source_list(sources)}
'''


def _kobo_hub():
    sources = [
        ("Kobo — Kobo Elipsa 2E", "https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e"),
        ("Kobo — utiliser la liseuse comme carnet", "https://help.kobo.com/hc/fr/articles/360062226733-Utiliser-votre-liseuse-Kobo-comme-un-carnet"),
        ("Kobo — annoter un livre avec le stylet", "https://help.kobo.com/hc/fr/articles/1500001927562-Annoter-votre-livre-avec-le-stylet-Kobo"),
        ("Kobo — exporter les annotations de livres", "https://help.kobo.com/hc/fr/articles/29991333812631-Exporte-les-annotations-de-vos-livres"),
        ("Kobo — liseuses actuellement commercialisées", "https://www.kobo.com/be/fr/ereaders"),
    ]
    return f'''
<p class="article-answer"><strong>Avec Kobo Elipsa, le vrai choix ne se joue pas entre une longue liste de modèles : il se joue entre trois types de contenu.</strong> Livres Kobo, PDF personnels et carnets ne se comportent pas de la même manière pour l’écriture, la sauvegarde et l’export. Comprendre cette différence est plus utile que de traiter l’Elipsa 2E comme une tablette E Ink généraliste.</p>

<h2 id="position">Elipsa 2E est surtout une liseuse Kobo grand format qui sait écrire</h2>
<p>La Kobo Elipsa 2E reste commercialisée comme modèle 10,3 pouces avec 32 Go, ComfortLight PRO et prise en charge du Kobo Stylus 2. Elle réunit lecture Kobo, carnets et annotation de documents sans ouvrir un environnement d’applications comme Android.</p>
<p>Cette priorité à la lecture la rapproche du Kindle Scribe davantage que de BOOX. Elle s’en distingue toutefois par son propre écosystème Kobo, par l’intégration de Google Drive et Dropbox pour certains transferts et par la façon dont Kobo sépare annotations textuelles, annotations manuscrites et PDF.</p>

<h2 id="trois-flux">Livres, PDF et carnets : trois workflows qui ne sortent pas de la même façon</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Contenu</th><th>Écriture / annotation</th><th>Sauvegarde / export</th><th>Limite décisive</th></tr></thead><tbody>
<tr><td><strong>Livre Kobo / Kobo Plus</strong></td><td>surlignages et notes textuelles ; annotations manuscrites selon appareil et contenu</td><td>les annotations textuelles éligibles peuvent être exportées depuis Kobo.com en PDF, HTML, TXT ou Markdown</td><td>Kobo précise que l’export des « markups » manuscrits n’est pas pris en charge</td></tr>
<tr><td><strong>EPUB avec écriture manuscrite</strong></td><td>écriture au stylet sur les formats compatibles</td><td>les annotations manuscrites restent sur la liseuse</td><td>elles ne s’exportent pas comme un PDF annoté vers Dropbox ou un autre emplacement</td></tr>
<tr><td><strong>PDF non protégé</strong></td><td>annotation manuscrite</td><td>le PDF peut être exporté avec les annotations</td><td>un PDF protégé par DRM ou dont l’annotation est désactivée ne permet pas ce même flux</td></tr>
<tr><td><strong>Carnet Kobo</strong></td><td>prise de notes manuscrite, avec fonctions de carnet</td><td>sauvegarde sur la liseuse et Kobo.com ; sauvegarde possible vers Google Drive ou Dropbox</td><td>ce flux est distinct des annotations écrites directement dans un livre</td></tr>
</tbody></table></div>
<p>Cette distinction corrige une confusion fréquente : Kobo permet désormais d’exporter certaines annotations de lecture depuis Kobo.com, mais cela ne signifie pas que toutes les écritures manuscrites tracées sur un EPUB deviennent exportables.</p>

<h2 id="cloud">Google Drive et Dropbox servent surtout à faire circuler des fichiers et des carnets</h2>
<p>L’Elipsa 2E intègre des services cloud pour importer ou sauvegarder des contenus compatibles. Cela évite de dépendre uniquement d’un câble USB pour certains workflows. Le cloud ne supprime cependant pas les règles propres à chaque format : un PDF annoté, un carnet et un livre Kobo gardent des capacités d’export différentes.</p>
<p>Si votre priorité est de récupérer systématiquement toutes vos notes hors de la liseuse, il faut donc vérifier le format exact avant l’achat. Pour les documents de travail, le guide {internal_link('/guides/annoter-pdf-tablette-e-ink/', 'annoter un PDF sur tablette E Ink')} est plus pertinent qu’une promesse générale de « cloud intégré ».</p>

<h2 id="choix">Quand Elipsa 2E est plus rationnelle qu’une tablette plus ouverte</h2>
<p>Elle a du sens si votre bibliothèque Kobo reste importante, si vous voulez un grand écran de lecture et si vos besoins d’écriture se limitent surtout aux carnets, aux PDF et aux annotations compatibles. Vous gagnez alors un environnement cohérent sans devoir gérer les réglages et applications d’une tablette Android.</p>
<p>Elle devient moins évidente si vous devez installer des applications métier, maintenir des dossiers synchronisés dans plusieurs outils ou construire un système dense de notes liées. Dans ce cas, le problème n’est pas une faiblesse du stylet : c’est le périmètre de l’écosystème.</p>
<p>Pour comprendre la différence côté lecture, voyez {internal_link('/usages/lecture-et-prise-de-notes/', 'lecture et prise de notes')}. Pour un duel direct, {internal_link('/comparatifs/kobo-elipsa-vs-remarkable/', 'Kobo Elipsa vs reMarkable')} et {internal_link('/comparatifs/kindle-scribe-vs-kobo-elipsa/', 'Kindle Scribe vs Kobo Elipsa')} couvrent deux alternatives proches mais différentes.</p>

<h2 id="avant-achat">Quatre vérifications évitent les mauvaises surprises</h2>
<p><strong>Le document est-il protégé ?</strong> Les PDF protégés par DRM ou dont l’annotation est désactivée ne se traitent pas comme un PDF personnel non protégé.</p>
<p><strong>Voulez-vous exporter une annotation textuelle ou un tracé manuscrit ?</strong> Kobo permet l’export de certaines annotations de livres depuis Kobo.com, mais pas l’export des markups manuscrits.</p>
<p><strong>Votre besoin est-il un carnet ou un système d’applications ?</strong> Elipsa 2E sait créer et sauvegarder des carnets ; ce n’est pas pour autant une tablette Android généraliste.</p>
<p><strong>Le stylet est-il bien inclus dans l’offre regardée ?</strong> La boutique Kobo peut vendre l’Elipsa 2E et ses accessoires selon des configurations différentes ; vérifiez le contenu exact du panier plutôt que de supposer que chaque canal propose le même bundle.</p>

<h2 id="sources">Sources vérifiées</h2>
<p>Disponibilité, caractéristiques générales et règles d’annotation/export vérifiées le {VERIFIED_AT}. Les distinctions d’usage ci-dessus sont tirées de la documentation Kobo et ne décrivent pas un test physique réalisé par le site.</p>
{_source_list(sources)}
'''


def _supernote_hub():
    sources = [
        ("Supernote — Manta", "https://supernote.com/products/supernote-manta"),
        ("Supernote — Nomad", "https://supernote.com/products/supernote-nomad"),
        ("Supernote — reconnaissance manuscrite", "https://support.supernote.com/handwriting-recognition"),
        ("Supernote — organisation avec headings, keywords et stars", "https://support.supernote.com/en_US/organizing/1759244-using-titles-keywords-and-stars"),
        ("Supernote — édition des liens dans les notes", "https://support.supernote.com/en_US/organizing/2126285-untitled-article"),
        ("Supernote — transfert de fichiers et cloud", "https://support.supernote.com/en_US/transfer-files"),
        ("Supernote — changelog Manta et Nomad, Chauvet 3.29.42", "https://support.supernote.com/changelog-for-manta-and-nomad"),
    ]
    return f'''
<p class="article-answer"><strong>Chez Supernote, la différence la plus importante n’est pas seulement le stylet : c’est la manière dont une note devient navigable.</strong> Manta et Nomad utilisent le même écosystème Chauvet autour des liens, headings, mots-clés, étoiles et reconnaissance manuscrite. Le choix matériel commence donc par le format ; le choix de marque, lui, dépend surtout de votre façon d’organiser l’information.</p>

<h2 id="format">Manta ou Nomad : le premier filtre est la taille du travail</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Modèle</th><th>Écran</th><th>Poids</th><th>Stockage</th><th>Quand il devient logique</th></tr></thead><tbody>
<tr><td><strong>Supernote Manta</strong></td><td>10,7″, 300 ppp, sans éclairage frontal</td><td>environ 375 g</td><td>32 Go + microSD jusqu’à 2 To</td><td>documents plus grands, longues notes, travail de bureau et PDF</td></tr>
<tr><td><strong>Supernote Nomad</strong></td><td>7,8″, 300 ppp, sans éclairage frontal</td><td>environ 266 g</td><td>32 Go + microSD jusqu’à 2 To</td><td>mobilité, notes quotidiennes et carnet transporté en permanence</td></tr>
</tbody></table></div>
<p>Les deux modèles reposent sur Chauvet, un système spécialisé basé sur Android 11. Les fiches officielles mettent aussi en avant une conception modulaire : batterie remplaçable et stockage microSD, avec carte mère évolutive selon le matériel. Cette logique de réparabilité fait partie du produit, mais ne compense pas un mauvais choix de taille : un Nomad reste petit pour de grands PDF, tandis qu’un Manta prend davantage de place dans un sac.</p>

<h2 id="organisation">L’intérêt de Supernote apparaît quand un carnet cesse d’être linéaire</h2>
<p>Dans les notes, Supernote permet de transformer une écriture en heading, d’ajouter des mots-clés, de marquer des pages avec des étoiles et de créer des liens. Ces éléments alimentent la navigation et la recherche plutôt que de rester de simples décorations sur la page.</p>
<p>C’est particulièrement utile lorsque vous reprenez des réunions, dossiers ou projets plusieurs semaines plus tard : un heading peut servir de table des matières, un mot-clé de point d’entrée transversal et un lien de passage vers une autre page ou note. Cette logique est plus structurée qu’un carnet numérique qui reproduit seulement l’ordre des pages.</p>
<p>Pour un usage centré sur cette organisation, le guide {internal_link('/guides/organiser-notes-numeriques/', 'organiser ses notes numériques')} complète le fonctionnement propre à Supernote.</p>

<h2 id="reconnaissance">La reconnaissance manuscrite sert surtout à sortir du manuscrit</h2>
<p>Supernote propose des notes avec reconnaissance en temps réel et permet d’exporter le résultat en TXT ou DOCX. La documentation précise que cette fonction peut être utilisée sans abonnement récurrent annoncé pour la reconnaissance elle-même. Cela permet de passer d’un brouillon manuscrit à du texte éditable sans devoir recopier chaque page.</p>
<p>Il faut toutefois distinguer reconnaissance et organisation : convertir une page en texte n’est pas la même chose que maintenir ses liens, sa navigation et sa structure manuscrite. Le bon usage dépend donc de la sortie recherchée — texte à retravailler, PDF à conserver ou base de notes à parcourir.</p>

<h2 id="fichiers">Le cloud est un moyen de transfert, pas l’identité du produit</h2>
<p>Supernote documente Supernote Cloud, Dropbox et Google Drive, ainsi que les transferts par USB-C, email et réseau local. Cette diversité est utile pour sauvegarder et déplacer des fichiers, mais la valeur de la marque reste dans la prise de notes et son organisation plutôt que dans une promesse de suite bureautique généraliste.</p>
<p>Si vos applications doivent fonctionner directement sur l’appareil, BOOX reste une comparaison importante. Si vous cherchez au contraire un environnement volontairement limité et centré sur l’écriture, {internal_link('/comparatifs/remarkable-vs-supernote/', 'reMarkable vs Supernote')} permet de comparer deux philosophies spécialisées.</p>

<h2 id="inkhub">InkHub élargit l’écosystème sans transformer Chauvet en magasin d’applications</h2>
<p>La mise à jour Chauvet 3.29.42 du 15 juin 2026 a ajouté InkHub sur Manta et Nomad. L’application sert à parcourir, télécharger et partager des ressources comme des stickers, templates, notes, digests et dessins. Elle enrichit donc les ressources disponibles dans l’environnement Supernote, mais ne doit pas être interprétée comme l’équivalent d’un catalogue Android ouvert.</p>
<p>La même mise à jour a aussi ajouté un stylo calligraphique et des réglages de sensibilité d’écriture sur Manta. Ces évolutions montrent que le logiciel continue de bouger ; elles justifient de consulter le changelog avant de conclure qu’une limitation observée sur une ancienne version de Chauvet est toujours actuelle.</p>

<h2 id="limites">Les limites sont matérielles autant que logicielles</h2>
<p>Ni Manta ni Nomad ne disposent d’éclairage frontal dans leurs spécifications actuelles, et la gamme reste en noir et blanc. Ce sont des contraintes simples mais structurantes si vous travaillez souvent le soir, lisez des documents où la couleur porte une information importante ou voulez un appareil multimédia.</p>
<p>Le choix est également moins pertinent si la lecture commerciale Kindle ou Kobo est votre activité dominante. Supernote peut intégrer Kindle, mais son cœur de produit reste le carnet structuré. Pour un environnement de lecture d’abord, regardez plutôt {internal_link('/marques/kindle-scribe/', 'Kindle Scribe')} ou {internal_link('/marques/kobo-elipsa/', 'Kobo Elipsa')}.</p>
<p>Pour comparer l’ouverture logicielle, {internal_link('/comparatifs/boox-vs-supernote/', 'BOOX vs Supernote')} pose le bon arbitrage : applications Android plus larges d’un côté, organisation spécialisée des notes de l’autre.</p>

<h2 id="sources">Sources vérifiées</h2>
<p>Matériel, organisation des notes, reconnaissance, transferts et mise à jour InkHub vérifiés le {VERIFIED_AT}. Les conséquences d’usage sont des synthèses documentaires ; elles ne sont pas présentées comme un test hands-on du site.</p>
{_source_list(sources)}
'''


def _remarkable_refresh(body):
    old = '''<h2 id="connect">Ce que l’abonnement Connect change vraiment</h2>
<p>Les fonctions de base d’écriture restent utilisables sans abonnement. Connect ajoute surtout des services cloud et applicatifs, notamment le stockage cloud illimité, la recherche manuscrite et des fonctions supplémentaires dans les applications reMarkable. Sans Connect, il faut donc vérifier si votre usage dépend de ces fonctions avant de considérer l’abonnement comme un coût obligatoire.</p>
<p>Pour le détail, voir <a href="/marques/remarkable/abonnement-connect/">reMarkable Connect</a> et le guide <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">bloc-notes numérique avec ou sans abonnement</a>.</p>'''
    new = '''<h2 id="connect">Ce que l’abonnement Connect change vraiment en 2026</h2>
<p>Les fonctions de base d’écriture restent utilisables sans abonnement, mais l’écart avec Connect s’est élargi. reMarkable documente désormais la recherche dans l’écriture manuscrite, la synchronisation et le stockage cloud illimités, des intégrations avec des services de travail et des outils d’IA. Les pages produits présentent notamment Meeting Notes Tool, Convert to Notebook et une conversion assistée par IA capable de transformer l’écriture en texte puis de produire des résumés, réflexions ou prochaines étapes selon la fonction disponible.</p>
<p>Sans Connect, reMarkable indique que seuls les fichiers utilisés et synchronisés au cours des 50 derniers jours restent stockés dans le cloud, et certaines fonctions des applications mobile/desktop ne sont pas disponibles. La bonne question n’est donc plus seulement « faut-il payer pour écrire ? » — non — mais « mon workflow dépend-il de la recherche manuscrite, du cloud illimité ou des outils connectés ? ». Pour le détail, voir <a href="/marques/remarkable/abonnement-connect/">reMarkable Connect</a> et le guide <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">bloc-notes numérique avec ou sans abonnement</a>.</p>'''
    if old not in body:
        raise RuntimeError("Expected reMarkable Connect section not found")
    body = body.replace(old, new)
    marker = '<h2 id="sources">Sources consultées</h2>'
    extra = '<p>Fonctions Connect recontrôlées le 9 septembre 2026 sur la documentation reMarkable actuelle.</p>'
    if marker in body and extra not in body:
        body = body.replace(marker, marker + '\n' + extra, 1)
    connect_source = '<li><a href="https://remarkable.com/shop/connect" rel="noopener noreferrer">reMarkable Connect — fonctions 2026</a></li>'
    if connect_source not in body:
        body = body.replace('</ul>', connect_source + '</ul>', 1)
    return body


def hub_body(url, body):
    if url == '/marques/kindle-scribe/':
        return _kindle_hub()
    if url == '/marques/kobo-elipsa/':
        return _kobo_hub()
    if url == '/marques/supernote/':
        return _supernote_hub()
    if url == '/marques/remarkable/':
        return _remarkable_refresh(body)
    return body


def hub_metadata(url, title, description):
    if url == '/marques/kindle-scribe/':
        return (
            'Kindle Scribe — Choisir entre 3e génération, Colorsoft et sans éclairage',
            'Kindle Scribe en 2026 : différences entre 3e génération, Colorsoft et version sans éclairage, cloud, notes, export et limites de l’écosystème.'
        )
    if url == '/marques/kobo-elipsa/':
        return (
            'Kobo Elipsa 2E — Notes, PDF, annotations et export',
            'Kobo Elipsa 2E : ce qui change entre livres Kobo, PDF et carnets, Google Drive, Dropbox, annotations manuscrites, export et limites.'
        )
    if url == '/marques/supernote/':
        return (
            'Supernote — Manta ou Nomad, notes liées, InkHub et cloud',
            'Supernote en 2026 : Manta vs Nomad, liens, headings, reconnaissance manuscrite, InkHub, Google Drive, réparabilité et limites.'
        )
    if url == '/marques/remarkable/':
        return (
            title,
            'Comprendre reMarkable en 2026 : Paper Pure, Paper Pro Move, Paper Pro, Connect, recherche manuscrite, outils IA, compatibilités et limites.'
        )
    return title, description


def hub_entity_summary(key, summary):
    updated = dict(summary)
    if key == 'kindle':
        updated['current_range'] = [
            ('Kindle Scribe (3e génération)', 'CURRENT', 'noir et blanc, éclairage réglable, 32/64 Go, sortie 2025', 'lecture Kindle + notes + cloud 2025+', 'pas d’applications tierces généralistes'),
            ('Kindle Scribe Colorsoft', 'CURRENT', 'couleur, éclairage réglable, 32/64 Go, sortie 2025', 'lecture et annotations couleur', 'écosystème toujours centré Kindle'),
            ('Kindle Scribe sans éclairage frontal', 'CURRENT', 'noir et blanc, 16 Go, sortie 2026', 'lecture et notes en lumière ambiante', 'pas d’éclairage frontal'),
            ('Kindle Scribe 2024', 'PREVIOUS_GENERATION', 'noir et blanc', 'ancienne génération encore supportée', 'pas les connexions cloud réservées aux modèles 2025+'),
        ]
        updated['ecosystem'] = [
            ('Bibliothèque', 'Kindle Store et bibliothèque Kindle.'),
            ('Notes', 'carnets manuscrits, recherche manuscrite sur modèles 2025+ et fonctions d’écriture selon génération.'),
            ('Documents', 'Send to Kindle et import de fichiers compatibles.'),
            ('Cloud tiers', 'Google Drive et OneDrive sur modèles 2025+, avec import/export de copies plutôt qu’une synchronisation bidirectionnelle du fichier source.'),
            ('OneNote', 'export de carnets en texte ou image selon le flux proposé.'),
            ('Couleur', 'Kindle Scribe Colorsoft ajoute écriture, surlignage et signets en couleur.'),
        ]
        updated['verified_at'] = VERIFIED_AT
    elif key == 'kobo':
        updated['ecosystem'] = [
            ('Bibliothèque', 'Kobo Store et livres Kobo.'),
            ('Carnets', 'carnets manuscrits sauvegardés sur la liseuse et Kobo.com, avec sauvegarde possible vers Google Drive ou Dropbox.'),
            ('Annotations de livres', 'certaines annotations textuelles de livres Kobo/Kobo Plus peuvent être exportées depuis Kobo.com ; les markups manuscrits ne le sont pas.'),
            ('PDF', 'les PDF non protégés peuvent être exportés avec annotations manuscrites ; les PDF protégés ou non annotables restent limitants.'),
            ('Cloud', 'Google Drive et Dropbox servent au transfert ou à la sauvegarde de contenus compatibles.'),
        ]
        updated['verified_at'] = VERIFIED_AT
    elif key == 'supernote':
        updated['ecosystem'] = [
            ('Matériel', 'Manta 10,7″ et Nomad 7,8″, tous deux 300 ppp et sans éclairage frontal.'),
            ('Modularité', 'batterie remplaçable, microSD et conception orientée réparation selon modèle.'),
            ('Système', 'Chauvet, système spécialisé basé sur Android 11.'),
            ('Organisation', 'headings, mots-clés, étoiles et liens pour naviguer dans les notes.'),
            ('OCR', 'reconnaissance manuscrite avec export TXT/DOCX.'),
            ('Cloud', 'Supernote Cloud, Dropbox et Google Drive ; transferts également par USB-C, email et réseau local.'),
            ('InkHub', 'depuis Chauvet 3.29.42, bibliothèque de ressources pour stickers, templates, notes, digests et dessins.'),
        ]
        updated['verified_at'] = VERIFIED_AT
    elif key == 'remarkable':
        eco = list(updated.get('ecosystem', []))
        eco.append(('Connect 2026', 'recherche manuscrite, cloud illimité, intégrations de travail et outils d’IA selon l’offre actuelle.'))
        updated['ecosystem'] = eco
        updated['verified_at'] = VERIFIED_AT
    return updated
