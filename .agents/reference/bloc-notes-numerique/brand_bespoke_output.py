from brand_render_common import internal_link


BOOX_VERIFIED_AT = "9 septembre 2026"


def _source_list(items):
    return '<ul class="source-list">' + ''.join(
        f'<li><a href="{url}" rel="noopener noreferrer">{label}</a></li>'
        for label, url in items
    ) + '</ul>'


def _boox_hub():
    official_sources = [
        ("BOOX — gamme d’appareils avec écriture", "https://shop.boox.com/collections/all-products/handwriting-tools"),
        ("BOOX Go 10.3 (Gen II) et Lumi", "https://shop.boox.com/products/go103gen2"),
        ("BOOX Note Air5 C", "https://shop.boox.com/products/noteair5c"),
        ("BOOX Note Max", "https://shop.boox.com/products/notemax"),
        ("BOOX Tab X C", "https://shop.boox.com/products/tabxc"),
        ("BOOX Tab Ultra C Pro", "https://shop.boox.com/products/tabultracpro"),
        ("BOOX — stockage cloud tiers", "https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage"),
        ("BOOX — notes manuscrites", "https://help.boox.com/hc/en-us/articles/8569373888788-Handwritten-Notes"),
        ("BOOX — synchronisation des données de lecture", "https://help.boox.com/hc/en-us/articles/25096430940436-Reading-Data-Syncing-and-Backup"),
    ]
    independent_sources = [
        ("Les Numériques — test du BOOX Note Air5 C", "https://www.lesnumeriques.com/liseuse/boox-note-air5-c-p78686/test.html"),
        ("TechRadar — Onyx BOOX Note Air5 C review", "https://www.techradar.com/tablets/ereaders/onyx-boox-note-air5-c-review"),
    ]
    return f'''
<p class="article-answer"><strong>Pour choisir un BOOX, commencez par éliminer les mauvais formats plutôt que par comparer toute la gamme.</strong> Parmi les modèles orientés écriture et prise de notes, les différences qui changent réellement l’achat sont la taille d’écran, la couleur, la présence d’un éclairage frontal, la version d’Android et les accessoires compatibles. BOOX vend aussi des liseuses plus compactes ; cette page se concentre sur les tablettes 10,3 et 13,3 pouces pertinentes pour les notes, les PDF et le travail documentaire.</p>

<h2 id="familles">BOOX n’est pas un modèle : six références ne répondent pas au même besoin</h2>
<p>La gamme d’écriture BOOX est plus difficile à lire que celle d’une marque centrée sur un ou deux appareils. En septembre 2026, les modèles à examiner en priorité sont les deux Go 10.3 Gen II, le Note Air5 C, le Note Max et le Tab X C. Le Tab Ultra C Pro reste officiellement documenté et commandable selon le canal, mais son Android 12 le place dans une génération logicielle plus ancienne.</p>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Modèle</th><th>Écran et lumière</th><th>Android</th><th>Clavier / stockage</th><th>Quand le regarder</th></tr></thead><tbody>
<tr><td><strong>Go 10.3 Gen II</strong></td><td>10,3″ N&B, 300 ppp, sans éclairage frontal</td><td>15</td><td>64 Go ; pas de microSD indiquée dans les specs officielles</td><td>notes et PDF avec priorité au poids, à la finesse et à la lecture en lumière ambiante</td></tr>
<tr><td><strong>Go 10.3 Gen II Lumi</strong></td><td>10,3″ N&B, 300 ppp, éclairage frontal réglable</td><td>15</td><td>64 Go ; pas de microSD indiquée dans les specs officielles</td><td>même logique que le Go, mais si vous travaillez aussi le soir ou dans une pièce peu éclairée</td></tr>
<tr><td><strong>Note Air5 C</strong></td><td>10,3″ Kaleido 3, 300 ppp N&B / 150 ppp couleur, éclairage frontal</td><td>15</td><td>microSD jusqu’à 2 To ; clavier officiel optionnel</td><td>couleur, applications Android et productivité légère sans passer au 13,3″</td></tr>
<tr><td><strong>Note Max</strong></td><td>13,3″ N&B, 300 ppp, sans éclairage frontal</td><td>13</td><td>128 Go ; clavier officiel optionnel partagé avec Tab X C</td><td>PDF proches du format A4, recherche, écriture et lecture de grands documents</td></tr>
<tr><td><strong>Tab X C</strong></td><td>13,3″ Kaleido 3, 300 ppp N&B / 150 ppp couleur, éclairage frontal</td><td>13</td><td>128 Go ; clavier officiel optionnel partagé avec Note Max</td><td>grands documents lorsque la couleur et l’éclairage comptent réellement</td></tr>
<tr><td><strong>Tab Ultra C Pro</strong></td><td>10,3″ Kaleido 3, éclairage frontal</td><td>12</td><td>microSD ; clavier avec trackpad disponible</td><td>à comparer surtout si vous trouvez encore cette génération à un prix ou dans une configuration qui justifie Android 12</td></tr>
</tbody></table></div>
<p>Le premier filtre est donc simple : un écran 13,3 pouces apporte de l’espace pour les documents mais alourdit fortement l’appareil ; la couleur facilite certains schémas et annotations, mais reste du Kaleido 3 à 150 ppp en couleur ; et l’éclairage frontal n’est pas présent sur tous les modèles. Le Go 10.3 Gen II Lumi mérite notamment d’être distingué du Go 10.3 Gen II classique : ils partagent Android 15 et le même format, mais pas la lumière frontale.</p>

<h2 id="android">Android est un avantage seulement si vos applications en profitent</h2>
<p>Sur les modèles actuels concernés, BOOX combine ses propres outils avec Google Play. Cela permet d’installer des applications de lecture, de stockage, de communication ou de productivité qui ne tournent pas directement sur des écosystèmes plus fermés. Le Note Air5 C et les Go 10.3 Gen II sont sous Android 15 ; Note Max et Tab X C sous Android 13 ; Tab Ultra C Pro sous Android 12.</p>
<p>Cette différence de génération est plus importante que le simple logo Android. Une version récente augmente la compatibilité avec les applications actuelles, tandis que l’E Ink impose toujours ses propres contraintes de rafraîchissement, de ghosting et de couleur. BOOX ajoute des réglages d’affichage et, sur certains modèles, sa technologie Super Refresh pour rendre le défilement plus fluide. Les tests récents du Note Air5 C par Les Numériques et TechRadar confirment l’intérêt de cette ouverture, tout en relevant les compromis de l’écran couleur E Ink et d’un usage plus proche d’une tablette.</p>
<p>Si votre besoin principal est justement d’éviter réglages, applications et arbitrages de rafraîchissement, {internal_link('/comparatifs/remarkable-vs-boox/', 'reMarkable vs BOOX')} est une comparaison plus utile que de chercher le BOOX le plus puissant.</p>

<h2 id="pdf">Pour les PDF, 10,3 ou 13,3 pouces change davantage l’usage que beaucoup de specs</h2>
<p>Un PDF A4 affiché sur 10,3 pouces oblige plus souvent à zoomer, recadrer ou travailler en paysage. Les Note Max et Tab X C se rapprochent davantage du confort d’un grand document grâce à leur écran 13,3 pouces. Ils ne répondent pourtant pas au même besoin : Note Max privilégie le noir et blanc très défini sans éclairage frontal, tandis que Tab X C ajoute la couleur et un éclairage réglable.</p>
<p>Le 10,3 pouces reste plus rationnel si l’appareil voyage beaucoup. Le Note Air5 C est alors le modèle le plus polyvalent pour combiner couleur, lumière, microSD et clavier optionnel. Les Go 10.3 Gen II sont plus dépouillés et légers ; le choix entre la version classique et la Lumi dépend surtout de votre besoin d’éclairage.</p>
<p>Pour un usage centré sur les documents, voyez aussi {internal_link('/usages/annotation-pdf/', 'l’annotation de PDF')} et {internal_link('/marques/boox/boox-note-air/', 'le détail de la famille Note Air')}.</p>

<h2 id="documents">Le vrai workflow BOOX se juge sur l’entrée et la sortie des documents</h2>
<p>BOOX ne se limite pas à ouvrir un PDF. NeoReader prend en charge de nombreux formats de lecture et permet d’annoter les documents ; l’application Notes gère l’écriture manuscrite et l’organisation des carnets. Les appareils peuvent aussi s’appuyer sur Onyx Cloud et, selon le firmware et le service, sur des intégrations comme Dropbox, Google Drive, OneDrive ou WebDAV/Nextcloud.</p>
<p>Cette ouverture devient réellement utile lorsque votre document doit circuler : récupération depuis un cloud, annotation, sauvegarde, puis réutilisation sur ordinateur ou dans un autre outil. À l’inverse, installer une application Android n’assure pas qu’elle sera agréable sur E Ink. Pour les usages professionnels, vérifiez donc le flux complet plutôt que la seule présence de l’application dans Google Play. Le guide sur {internal_link('/guides/ecosysteme-ouvert-ou-ferme/', 'les écosystèmes ouverts et fermés')} détaille ce compromis.</p>

<h2 id="situations">Quel BOOX regarder selon la situation ?</h2>
<p><strong>Vous écrivez surtout en noir et blanc et travaillez dans des endroits bien éclairés.</strong> Le Go 10.3 Gen II évite la couche d’éclairage frontal et reste le choix le plus simple dans cette famille. Si ce même usage se prolonge souvent le soir, la variante Lumi corrige précisément cette limite sans changer de format ni de génération Android.</p>
<p><strong>Vous voulez un 10,3 pouces couleur qui puisse aussi exécuter vos applications.</strong> Le Note Air5 C est le point de départ le plus cohérent : Android 15, écran Kaleido 3, éclairage, microSD et clavier optionnel. Sa couleur reste toutefois moins définie que son affichage noir et blanc, comme sur les autres écrans Kaleido 3.</p>
<p><strong>Vous lisez ou annotez régulièrement de grands PDF.</strong> Note Max privilégie un grand écran noir et blanc à 300 ppp ; Tab X C ajoute la couleur et la lumière frontale. Le gain d’espace est réel, mais ces appareils de plus de 600 g répondent davantage à un usage bureau qu’à un carnet que l’on transporte partout.</p>
<p><strong>Vous regardez une promotion ou un stock restant de Tab Ultra C Pro.</strong> Ne le comparez pas au Note Air5 C uniquement sur le prix. Son Android 12, son clavier avec trackpad, sa caméra arrière et son slot microSD correspondent à une autre génération et à une logique plus “tablet PC”. Sa disponibilité doit être vérifiée au moment de l’achat.</p>

<h2 id="avant-achat">Avant d’acheter, vérifiez la génération exacte plutôt que la marque</h2>
<p>Chez BOOX, deux appareils proches par le nom peuvent différer sur Android, le stylet, le clavier, l’éclairage ou le stockage. C’est particulièrement important pour les accessoires : Go 10.3 Gen II utilise l’InkSense Plus, Note Air5 C le Pen3, Note Max le Pen Plus et Tab X C l’InkSpire. Les étuis et claviers ne sont pas universels.</p>
<p>Vérifiez également le canal d’achat lorsque vous regardez un modèle plus ancien. Une fiche officielle peut encore exister alors que le stock varie selon la boutique ou l’entrepôt. Pour les questions de mises à jour, garantie, retours et SAV, la page {internal_link('/marques/boox/avis/', 'notre avis documentaire sur BOOX')} traite ce risque séparément. Pour le matériel, {internal_link('/marques/boox/accessoires/', 'le guide des accessoires BOOX')} cartographie les compatibilités par modèle.</p>
<p>Enfin, si Android est précisément ce que vous cherchez à éviter, ne forcez pas le choix à l’intérieur de la gamme : {internal_link('/marques/boox/alternatives/', 'les alternatives à BOOX')} partent des limites que vous voulez corriger.</p>

<h2 id="sources">Sources utilisées pour cette mise à jour</h2>
<p>Gamme, système, écrans, éclairage, stockage et accessoires vérifiés le {BOOX_VERIFIED_AT}. Les jugements sur l’ouverture Android et les compromis E Ink sont présentés comme une synthèse éditoriale appuyée par des tests indépendants, pas comme une expérience de test propre au site.</p>
<h3>Documentation BOOX</h3>
{_source_list(official_sources)}
<h3>Tests indépendants consultés</h3>
{_source_list(independent_sources)}
'''


def bespoke_body(url, body):
    if url == '/marques/boox/':
        return _boox_hub()
    return body


def bespoke_metadata(url, title, description):
    if url == '/marques/boox/':
        return (
            'BOOX — Choisir entre Go, Note Air, Note Max et Tab X',
            'Guide de la gamme BOOX pour la prise de notes : Go 10.3 Gen II/Lumi, Note Air5 C, Note Max, Tab X C, Android, PDF, éclairage et clavier.'
        )
    return title, description


def bespoke_entity_summary(key, summary):
    if key != 'boox':
        return summary

    updated = dict(summary)
    updated['current_range'] = [
        ('Go 10.3 Gen II', 'CURRENT', '10,3″ N&B, 300 ppp, sans éclairage frontal, Android 15', 'notes, PDF et mobilité', 'lecture nocturne sans lumière externe limitée'),
        ('Go 10.3 Gen II Lumi', 'CURRENT', '10,3″ N&B, 300 ppp, éclairage frontal, Android 15', 'notes, PDF et mobilité avec éclairage', 'plus épais et plus lourd que le Go standard'),
        ('Note Air5 C', 'CURRENT', '10,3″ Kaleido 3, Android 15', 'couleur, notes et productivité légère', '150 ppp en couleur contre 300 ppp en N&B'),
        ('Note Max', 'CURRENT', '13,3″ N&B, 300 ppp, Android 13', 'grands PDF et travail documentaire', 'pas d’éclairage frontal et format peu mobile'),
        ('Tab X C', 'CURRENT', '13,3″ Kaleido 3, Android 13', 'grand écran couleur et productivité', 'plus de 600 g et encombrement élevé'),
        ('Tab Ultra C Pro', 'CURRENT_DOCUMENTED_CHANNEL_SENSITIVE', '10,3″ Kaleido 3, Android 12', 'workflow type tablette avec clavier', 'génération logicielle plus ancienne ; disponibilité à vérifier'),
    ]
    updated['ecosystem'] = [
        ('Matériel', 'formats 10,3 et 13,3 pouces, noir et blanc ou Kaleido 3 couleur selon modèle.'),
        ('Stylet', 'InkSense Plus sur Go 10.3 Gen II, Pen3 sur Note Air5 C, Pen Plus sur Note Max et InkSpire sur Tab X C ; compatibilité à vérifier par modèle.'),
        ('Système', 'Android 15 sur Go 10.3 Gen II et Note Air5 C, Android 13 sur Note Max et Tab X C, Android 12 sur Tab Ultra C Pro.'),
        ('Notes', 'Notes BOOX avec écriture manuscrite, organisation et exports documentés.'),
        ('Lecture', 'NeoReader pour PDF, EPUB et de nombreux formats.'),
        ('Cloud', 'Onyx Cloud et intégrations Dropbox, Google Drive, OneDrive, WebDAV/Nextcloud selon firmware.'),
        ('Synchronisation', 'progression, annotations et sauvegardes selon les méthodes BOOX.'),
        ('Applications', 'Google Play et applications tierces sur les modèles concernés, avec une expérience qui dépend de l’optimisation E Ink.'),
    ]
    updated['verified_at'] = BOOX_VERIFIED_AT
    return updated
