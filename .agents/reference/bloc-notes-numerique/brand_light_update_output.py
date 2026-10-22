from brand_render_common import internal_link

VERIFIED_DATE = '9 septembre 2026'


def _source_list(items):
    return '<ul class="source-list">' + ''.join(
        f'<li><a href="{url}" rel="noopener noreferrer">{label}</a></li>'
        for label, url in items
    ) + '</ul>'


def _directory():
    sources = [
        ('reMarkable — gamme actuelle', 'https://remarkable.com/fr-fr'),
        ('BOOX — gamme actuelle', 'https://shop.boox.com/collections/all-products/reading-tools'),
        ('Amazon — connexions Kindle Scribe 2025+ à Google Drive, OneDrive et OneNote', 'https://digprjsurvey.amazon.com/csad/help/node/Tuar1obhcxaS8hVUKd'),
        ('Kobo — liseuses actuelles et Elipsa 2E', 'https://www.kobo.com/be/fr/eReaders'),
        ('Supernote — organisation des notes', 'https://supernote.com/pages/note-system-everything-you-need-to-stay-organized'),
    ]
    return f'''
<p class="article-answer"><strong>reMarkable, BOOX, Kindle Scribe, Kobo Elipsa et Supernote ne répondent pas au même besoin.</strong> La différence principale se joue moins sur la technologie E Ink elle-même que sur le logiciel, les formats, le cloud, les applications et la façon d’organiser les notes.</p>
<h2 id="comparaison">Cinq écosystèmes, cinq logiques différentes</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Marque</th><th>Ce qui la distingue</th></tr></thead><tbody>
<tr><td>{internal_link('/marques/remarkable/', 'reMarkable')}</td><td>un environnement volontairement spécialisé dans l’écriture et les documents, avec peu de distractions et un écosystème logiciel propre</td></tr>
<tr><td>{internal_link('/marques/boox/', 'BOOX')}</td><td>des tablettes E Ink Android qui privilégient les applications tierces, les formats et la flexibilité, au prix de davantage de réglages</td></tr>
<tr><td>{internal_link('/marques/kindle-scribe/', 'Kindle Scribe')}</td><td>la lecture Kindle comme point de départ, complétée par carnets et circulation de documents ; les générations 2025+ ajoutent notamment des connexions Drive, OneDrive et OneNote</td></tr>
<tr><td>{internal_link('/marques/kobo-elipsa/', 'Kobo Elipsa')}</td><td>une liseuse grand format Kobo avec stylet, carnets, annotation de PDF et services cloud intégrés</td></tr>
<tr><td>{internal_link('/marques/supernote/', 'Supernote')}</td><td>un e-notebook spécialisé dans la structuration des connaissances avec titres, mots-clés, étoiles, liens et reconnaissance manuscrite</td></tr>
</tbody></table></div>
<h2 id="choisir">Quelle marque regarder en premier ?</h2>
<ul>
<li><strong>reMarkable</strong> si vous privilégiez une expérience spécialisée et peu distraite.</li>
<li><strong>BOOX</strong> si Android et vos applications habituelles sont des prérequis.</li>
<li><strong>Kindle Scribe</strong> si votre bibliothèque Kindle reste au centre de l’usage.</li>
<li><strong>Kobo Elipsa 2E</strong> si vous lisez surtout chez Kobo et voulez ajouter carnets et PDF annotés.</li>
<li><strong>Supernote</strong> si votre problème principal est d’organiser et relier un grand volume de notes.</li>
</ul>
<h2 id="criteres">Les critères qui évitent un mauvais choix</h2>
<p>Avant de comparer les modèles, notez les applications indispensables, le type de documents que vous manipulez, le cloud déjà utilisé et la manière dont vous devez récupérer vos notes. Une marque peut être excellente pour l’écriture et rester inadaptée si elle bloque l’un de ces points.</p>
<p>Vous pouvez ensuite passer au {internal_link('/comparatifs/meilleur-bloc-notes-numerique/', 'comparatif général')} ou au {internal_link('/guides/choisir-bloc-notes-numerique/', 'guide de choix')}.</p>
<h2 id="sources">Sources consultées</h2>
<p>Les cinq écosystèmes ont été revérifiés le {VERIFIED_DATE} à partir de sources primaires propres à chaque marque.</p>
{_source_list(sources)}
'''


def _remarkable_connect():
    sources = [
        ('reMarkable — Connect : fonctionnalités', 'https://remarkable.com/shop/connect'),
        ('reMarkable — Connect : tarification et comparaison avec/sans abonnement', 'https://remarkable.com/shop/connect/pricing'),
        ('Support reMarkable — About Connect', 'https://support.remarkable.com/articles/Knowledge/About-Connect-Subscription'),
    ]
    return f'''
<p class="article-answer"><strong>Connect n’est pas nécessaire pour écrire sur une reMarkable, mais il devient une partie du coût réel si vous dépendez de la recherche manuscrite, de la synchronisation cloud sans limite, des outils de travail intégrés ou de l’édition dans les applications mobile et desktop.</strong></p>
<h2 id="sans">Sans Connect, la tablette ne cesse pas de fonctionner</h2>
<p>Les fonctions intégrées de la tablette restent disponibles sans abonnement. reMarkable conserve aussi des fonctions cloud et des applications gratuites, mais la synchronisation n’a pas le même périmètre qu’avec Connect.</p>
<p>La règle importante est celle des <strong>50 jours</strong> : après l’arrêt de Connect, les fichiers restent stockés, mais un fichier qui n’a pas été modifié pendant 50 jours cesse de se synchroniser avec les applications desktop et mobile. La création et l’édition de notes directement dans ces applications ne sont alors plus disponibles.</p>
<h2 id="avec">Ce que Connect ajoute réellement en 2026</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Besoin</th><th>Impact de Connect</th></tr></thead><tbody>
<tr><td><strong>Retrouver une note manuscrite</strong></td><td>recherche dans le contenu manuscrit et tapé</td></tr>
<tr><td><strong>Cloud et synchronisation</strong></td><td>stockage et synchronisation illimités annoncés</td></tr>
<tr><td><strong>Travailler depuis ordinateur ou téléphone</strong></td><td>création et édition de notes dans les apps reMarkable</td></tr>
<tr><td><strong>Préparer des réunions</strong></td><td>Meeting Notes Tool avec intégration calendrier</td></tr>
<tr><td><strong>Transformer des notes</strong></td><td>Convert to Notebook et outils de conversion/partage assistés par IA</td></tr>
<tr><td><strong>Continuer dans d’autres outils</strong></td><td>intégrations et envois vers des services de travail selon l’offre en cours</td></tr>
</tbody></table></div>
<h2 id="cout">Dans quels cas l’abonnement devient-il rationnel ?</h2>
<p>Le bon test n’est pas de compter les fonctions. Demandez-vous ce qui casse dans votre semaine de travail sans Connect. Si vous utilisez la tablette localement et exportez ponctuellement des documents, la valeur du service peut rester faible. Si vous cherchez chaque jour dans des carnets manuscrits, travaillez sur plusieurs appareils ou exploitez les intégrations, l’abonnement devient beaucoup plus structurel.</p>
<p>Pour replacer ce coût dans le choix d’un appareil, consultez {internal_link('/guides/bloc-notes-numerique-avec-ou-sans-abonnement/', 'le guide avec ou sans abonnement')}.</p>
<h2 id="dependance">Annuler Connect : ce qu’il faut vérifier avant</h2>
<p>Avant de dépendre du service, vérifiez votre méthode d’export et les formats que vous conserverez hors de l’écosystème. L’arrêt de l’abonnement ne supprime pas les fichiers déjà stockés dans le cloud, mais il réduit la synchronisation et l’édition dans les applications. Cette différence est plus importante qu’une simple comparaison « gratuit vs payant ».</p>
<p>Voir aussi {internal_link('/guides/exporter-notes/', 'les méthodes d’export')} et {internal_link('/marques/remarkable/', 'la gamme reMarkable actuelle')}.</p>
<h2 id="produits">Sur quels appareils Connect pèse-t-il dans la décision ?</h2>
<p>Le service est commun à l’écosystème, mais son poids varie selon l’usage. Sur un {internal_link('/marques/remarkable/remarkable-paper-pro/', 'Paper Pro')} utilisé pour de grands documents et un workflow multi-appareils, les fonctions cloud et de recherche peuvent compter davantage que sur un carnet utilisé presque uniquement hors ligne.</p>
<h2 id="sources">Sources consultées</h2>
<p>Fonctions et règles Connect revérifiées le {VERIFIED_DATE}. Les tarifs peuvent évoluer et doivent être contrôlés au moment de l’abonnement.</p>
{_source_list(sources)}
'''


def _remarkable_2_product():
    sources = [
        ('reMarkable 2 — statut, accessoires et mises à jour', 'https://remarkable.com/products/remarkable-2'),
        ('reMarkable — gamme actuelle', 'https://remarkable.com/fr-fr'),
    ]
    return f'''
<p class="article-answer"><strong>En 2026, reMarkable 2 est un produit discontinué, mais pas un appareil abandonné.</strong> reMarkable ne la vend plus comme modèle courant, continue de proposer ses accessoires et annonce toujours des mises à jour logicielles régulières. La question d’achat concerne donc surtout l’occasion ou le reconditionné.</p>
<h2 id="statut">Discontinuée ne veut pas dire privée de support logiciel</h2>
<p>La marque indique explicitement que reMarkable 2 est discontinuée et que les utilisateurs continueront à recevoir des mises à jour, y compris de nouvelles fonctions, des améliorations de performances et des correctifs de stabilité. C’est une distinction importante : le matériel appartient à une ancienne génération, mais l’environnement logiciel continue d’évoluer.</p>
<h2 id="caracteristiques">Les caractéristiques qui comptent encore</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Point</th><th>reMarkable 2</th></tr></thead><tbody>
<tr><td><strong>Écran</strong></td><td>10,3 pouces Canvas, noir et blanc</td></tr>
<tr><td><strong>Éclairage</strong></td><td>aucun éclairage frontal</td></tr>
<tr><td><strong>Documents</strong></td><td>notes, PDF, EPUB importés et conversion manuscrite dans l’écosystème reMarkable</td></tr>
<tr><td><strong>Cloud</strong></td><td>écosystème reMarkable avec intégrations et Connect selon les fonctions utilisées</td></tr>
<tr><td><strong>Stylet</strong></td><td>Marker / Marker Plus de génération reMarkable 2</td></tr>
</tbody></table></div>
<h2 id="compatibilite">Le principal piège reste la génération des accessoires</h2>
<p>Les Markers de reMarkable 2 n’appartiennent pas à la génération Paper actuelle. reMarkable indique toutefois continuer à vendre Markers, Book Folios, Type Folios et mines pour reMarkable 2. Sur le marché de l’occasion, vérifiez donc à la fois l’état de l’accessoire et sa génération.</p>
<h2 id="occasion">Que vérifier en occasion ou reconditionné ?</h2>
<ul>
<li>état de la batterie, de l’écran et du port USB-C ;</li>
<li>présence et état du Marker ;</li>
<li>génération exacte des accessoires fournis ;</li>
<li>écart de prix réel avec un modèle de la gamme actuelle.</li>
</ul>
<p>Le {internal_link('/bons-plans/bloc-notes-numerique-occasion/', 'guide sur l’occasion')} complète cette vérification.</p>
<h2 id="choix">Pour qui reste-t-elle cohérente ?</h2>
<p>Elle garde du sens pour un propriétaire actuel ou pour un achat reconditionné suffisamment décoté si le noir et blanc et l’absence d’éclairage ne sont pas des problèmes. Pour un achat neuf ou à prix proche d’un modèle récent, repartez plutôt de {internal_link('/marques/remarkable/', 'la gamme reMarkable actuelle')}.</p>
<p>Pour le jugement éditorial basé sur des essais indépendants, consultez {internal_link('/marques/remarkable/remarkable-2-avis/', 'notre avis documentaire sur reMarkable 2')} plutôt que de déduire le confort d’usage de cette fiche.</p>
<h2 id="sources">Sources consultées</h2>
<p>Statut commercial, disponibilité des accessoires et maintien logiciel revérifiés le {VERIFIED_DATE}.</p>
{_source_list(sources)}
'''


def _remarkable_2_review():
    official = [
        ('reMarkable 2 — statut, accessoires et mises à jour', 'https://remarkable.com/products/remarkable-2'),
        ('reMarkable — gamme actuelle', 'https://remarkable.com/fr-fr'),
    ]
    independent = [
        ('TechRadar — reMarkable 2 review', 'https://www.techradar.com/reviews/remarkable-2-tablet'),
        ('WIRED — Review: reMarkable 2', 'https://www.wired.com/review/remarkable-2/'),
        ('Tom’s Guide — reMarkable 2 review', 'https://www.tomsguide.com/reviews/remarkable-2-review'),
    ]
    return f'''
<p class="article-answer"><strong>Notre avis en 2026 : reMarkable 2 reste un carnet numérique cohérent pour un propriétaire actuel ou un achat reconditionné bien placé, mais son statut discontinué la sort du rôle de choix neuf par défaut.</strong> Cette conclusion croise la situation actuelle documentée par reMarkable avec des essais indépendants publiés lorsque le produit était au cœur de la gamme ; nous n’avons pas réalisé de test physique.</p>
<h2 id="forces">Pourquoi les qualités historiques restent pertinentes</h2>
<p>TechRadar, WIRED et Tom’s Guide ont notamment évalué son orientation très focalisée vers l’écriture et les documents. Ces observations restent utiles pour comprendre le produit matériel, mais elles ne disent rien à elles seules sur son statut commercial ou son support en 2026.</p>
<h2 id="age">Ce que 2026 change réellement dans le verdict</h2>
<p>reMarkable 2 est officiellement discontinuée, tandis que ses accessoires restent proposés et que reMarkable annonce toujours des mises à jour logicielles régulières. Le produit n’est donc pas « mort », mais un acheteur doit comparer une ancienne génération sans éclairage ni couleur avec les modèles Paper actuels.</p>
<h2 id="limites">Les limites qui pèsent davantage aujourd’hui</h2>
<ul>
<li>absence d’éclairage frontal ;</li>
<li>pas de couleur ;</li>
<li>ancienne génération de Marker et de Folios ;</li>
<li>achat d’occasion ou reconditionné qui ajoute l’état de la batterie et du matériel à l’équation.</li>
</ul>
<p>Pour les caractéristiques, compatibilités et points à contrôler avant un achat d’occasion, voir {internal_link('/marques/remarkable/remarkable-2/', 'la fiche reMarkable 2')}.</p>
<h2 id="pour-qui">À qui la conseiller encore ?</h2>
<p>À un propriétaire actuel, elle reste pleinement défendable si elle couvre encore le besoin. À un acheteur reconditionné, elle peut être rationnelle si l’écart de prix compense clairement les concessions matérielles. Le {internal_link('/bons-plans/bloc-notes-numerique-occasion/', 'guide sur l’occasion')} aide à cadrer cette décision.</p>
<h2 id="verdict">Verdict</h2>
<p><strong>reMarkable 2 doit aujourd’hui être jugée comme une ancienne génération toujours maintenue, pas comme le produit principal de la marque.</strong> Si le prix devient proche d’un appareil actuel, repartez de {internal_link('/marques/remarkable/', 'la gamme reMarkable 2026')}.</p>
<h2 id="methode">Sur quoi repose cet avis ?</h2>
<p>Le statut, les accessoires et le maintien logiciel viennent de reMarkable. Les observations sur l’expérience matérielle viennent des essais indépendants cités ci-dessous. Elles restent attribuées à leurs auteurs et ne sont pas transformées en expérience propre au site.</p>
<h2 id="sources">Sources consultées</h2>
<h3>Sources officielles</h3>{_source_list(official)}
<h3>Essais indépendants</h3>{_source_list(independent)}
'''


def _remarkable_alternatives():
    sources = [
        ('reMarkable — gamme actuelle', 'https://remarkable.com/fr-fr'),
        ('BOOX — gamme actuelle', 'https://shop.boox.com/collections/all-products/reading-tools'),
        ('Supernote — système de notes', 'https://supernote.com/pages/note-system-everything-you-need-to-stay-organized'),
        ('Amazon — connexions Kindle Scribe 2025+', 'https://digprjsurvey.amazon.com/csad/help/node/Tuar1obhcxaS8hVUKd'),
        ('Kobo — Elipsa 2E et gamme actuelle', 'https://www.kobo.com/be/fr/eReaders'),
    ]
    return f'''
<p class="article-answer"><strong>La meilleure alternative à reMarkable dépend de la limite que vous cherchez réellement à corriger.</strong> Davantage d’applications, une organisation de notes plus riche, une bibliothèque Kindle/Kobo ou le refus d’un coût récurrent ne mènent pas vers le même appareil.</p>
<h2 id="android">Si l’absence d’applications tierces est le problème : BOOX</h2>
<p>BOOX est l’alternative la plus directe lorsque Google Play, des applications métier ou plusieurs services tiers sont indispensables. Cette ouverture implique aussi davantage de réglages et une expérience moins volontairement limitée. Voir {internal_link('/comparatifs/remarkable-vs-boox/', 'reMarkable vs BOOX')}.</p>
<h2 id="organisation">Si vous voulez surtout structurer des connaissances : Supernote</h2>
<p>Supernote documente un système de notes fondé sur les titres, mots-clés, étoiles et liens entre notes, documents et pages web. Ce choix est plus pertinent si votre frustration vient de l’organisation du savoir que d’un manque d’applications Android. Voir {internal_link('/comparatifs/remarkable-vs-supernote/', 'reMarkable vs Supernote')} et {internal_link('/marques/supernote/', 'le hub Supernote')}.</p>
<h2 id="lecture">Si la lecture reste le centre du workflow : Kindle ou Kobo</h2>
<p>{internal_link('/marques/kindle-scribe/', 'Kindle Scribe')} est le chemin logique si votre bibliothèque Amazon domine et que l’écriture complète la lecture. Les modèles Scribe sortis à partir de 2025 ajoutent notamment des connexions Google Drive, OneDrive et OneNote.</p>
<p>{internal_link('/marques/kobo-elipsa/', 'Kobo Elipsa 2E')} part du même raisonnement côté Kobo : écran 10,3 pouces, stylet, carnets, annotation et services cloud intégrés.</p>
<h2 id="cout">Si Connect ou le coût total vous gêne</h2>
<p>Ne remplacez pas automatiquement un abonnement par un appareil plus cher. Comparez le coût de la configuration complète — tablette, stylet, protection, clavier éventuel et services — puis vérifiez quelle fonction vous cherchez réellement à éviter. Le {internal_link('/comparatifs/bloc-notes-numerique-sans-abonnement/', 'comparatif sans abonnement')} sert précisément à ce tri.</p>
<h2 id="choix">Le bon critère est celui qui vous fait quitter reMarkable</h2>
<p>Une alternative doit corriger votre blocage sans casser votre tâche principale. Si vous quittez reMarkable uniquement pour une application absente, BOOX a du sens ; si vous voulez surtout un système de notes reliées, Supernote répond à une autre frustration ; si votre bibliothèque de lecture domine, Kindle ou Kobo deviennent plus rationnels.</p>
<h2 id="sources">Sources consultées</h2>
<p>Positionnements et fonctions décisionnelles revérifiés le {VERIFIED_DATE} auprès de chaque fabricant.</p>
{_source_list(sources)}
'''


def _boox_alternatives():
    sources = [
        ('BOOX — gamme actuelle', 'https://shop.boox.com/collections/all-products/reading-tools'),
        ('reMarkable — gamme actuelle', 'https://remarkable.com/fr-fr'),
        ('Supernote — système de notes', 'https://supernote.com/pages/note-system-everything-you-need-to-stay-organized'),
        ('Amazon — connexions Kindle Scribe 2025+', 'https://digprjsurvey.amazon.com/csad/help/node/Tuar1obhcxaS8hVUKd'),
        ('Kobo — Elipsa 2E et gamme actuelle', 'https://www.kobo.com/be/fr/eReaders'),
    ]
    return f'''
<p class="article-answer"><strong>Quitter BOOX n’a de sens que si sa flexibilité Android vous coûte plus qu’elle ne vous apporte.</strong> Si votre problème est la complexité, l’organisation des notes ou une lecture très centrée sur une librairie, plusieurs écosystèmes plus spécialisés peuvent être plus cohérents.</p>
<h2 id="simplicite">Si vous voulez moins de réglages : reMarkable</h2>
<p>reMarkable réduit volontairement le champ des applications et concentre l’expérience sur l’écriture, les documents et son propre environnement. C’est un compromis : moins de liberté logicielle, mais moins de paramètres à gérer. Voir {internal_link('/comparatifs/remarkable-vs-boox/', 'reMarkable vs BOOX')}.</p>
<h2 id="organisation">Si les notes reliées passent avant Android : Supernote</h2>
<p>Supernote met en avant titres, mots-clés, étoiles et liens pour structurer des carnets et relier des informations. Si votre problème BOOX est moins l’absence de fonctions que la surcharge, ce modèle d’organisation mérite d’être comparé. Voir {internal_link('/comparatifs/boox-vs-supernote/', 'BOOX vs Supernote')} et {internal_link('/marques/supernote/', 'le hub Supernote')}.</p>
<h2 id="lecture">Si vous voulez surtout lire : Kindle ou Kobo</h2>
<p>{internal_link('/marques/kindle-scribe/', 'Kindle Scribe')} est plus naturel pour une bibliothèque Amazon, tandis que {internal_link('/marques/kobo-elipsa/', 'Kobo Elipsa 2E')} part de l’écosystème Kobo. Dans les deux cas, la logique de liseuse reste plus centrale que chez BOOX.</p>
<h2 id="garder-boox">Quand rester chez BOOX est plus rationnel</h2>
<p>Si vous utilisez réellement Google Play, plusieurs clouds, les outils PDF de BOOX ou une application métier, changer d’écosystème peut supprimer la fonction même qui justifiait votre achat. Dans ce cas, commencez par {internal_link('/marques/boox/', 'la gamme BOOX')} : un {internal_link('/marques/boox/boox-note-air/', 'Note Air actuel')} ou un autre format peut résoudre le problème sans migration complète.</p>
<h2 id="choix">Choisissez l’alternative qui corrige une friction précise</h2>
<p>Ne comparez pas ces marques sur un nombre total de fonctions. Identifiez la friction — réglages, organisation, bibliothèque, taille ou coût — puis vérifiez que l’alternative améliore ce point sans dégrader votre tâche principale.</p>
<h2 id="sources">Sources consultées</h2>
<p>Les fonctions utilisées pour orienter vers chaque écosystème ont été revérifiées le {VERIFIED_DATE} auprès de leurs sources primaires.</p>
{_source_list(sources)}
'''


def _boox_note_air():
    sources = [
        ('BOOX — Note Air5 C', 'https://shop.boox.com/products/noteair5c'),
        ('BOOX — Note Air4 C', 'https://shop.boox.com/products/noteair4c'),
    ]
    return f'''
<p class="article-answer"><strong>La famille BOOX Note Air est aujourd’hui représentée par le Note Air5 C, un modèle 10,3 pouces couleur sous Android 15.</strong> Sa vraie différence par rapport au Note Air4 C n’est pas un changement de format : c’est surtout une génération logicielle plus récente, un nouveau stylet et une intégration plus poussée de la productivité légère.</p>
<h2 id="modele">Note Air5 C : ce qui reste stable et ce qui change</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Point</th><th>Note Air4 C</th><th>Note Air5 C</th></tr></thead><tbody>
<tr><td><strong>Écran</strong></td><td>10,3 pouces Kaleido 3, 300/150 ppp</td><td>10,3 pouces Kaleido 3, 300/150 ppp</td></tr>
<tr><td><strong>Système</strong></td><td>Android 13</td><td>Android 15</td></tr>
<tr><td><strong>Mémoire</strong></td><td>6 Go / 64 Go</td><td>6 Go / 64 Go</td></tr>
<tr><td><strong>Stockage extensible</strong></td><td>microSD</td><td>microSD, jusqu’à 2 To annoncé</td></tr>
<tr><td><strong>Stylet fourni</strong></td><td>Pen Plus</td><td>Pen3</td></tr>
<tr><td><strong>Clavier</strong></td><td>pas le même positionnement clavier</td><td>keyboard cover magnétique dédié avec pogo pins et recharge traversante</td></tr>
</tbody></table></div>
<p>Si vous possédez déjà un Note Air4 C, le passage au Note Air5 C ne se justifie donc pas par la résolution ou la capacité mémoire. Il faut surtout valoriser Android 15, le clavier dédié et les changements de workflow.</p>
<h2 id="android">Android 15 et EinkWise : la souplesse reste le cœur du produit</h2>
<p>Le Note Air5 C donne accès à Google Play et aux applications tierces. BOOX ajoute EinkWise pour régler le rafraîchissement, la couleur et l’affichage selon l’application. Cette liberté est utile si vous avez des apps précises ; elle ajoute aussi plus de paramètres qu’un carnet spécialisé.</p>
<h2 id="clavier">Le clavier change davantage le rôle du Note Air que la couleur</h2>
<p>Le keyboard cover officiel se connecte par pogo pins et possède un port USB-C pour la recharge traversante. Il vise des tâches courtes de saisie — e-mails, rapports, feuilles de calcul — plutôt qu’un remplacement complet d’ordinateur. Si vous n’écrivez presque jamais au clavier sur E Ink, cet accessoire ne doit pas peser dans le choix.</p>
<h2 id="limites">Ce que la fiche officielle ne permet pas de promettre</h2>
<ul>
<li>toutes les applications Android ne sont pas optimisées pour E Ink ;</li>
<li>Kaleido 3 reste moins saturé qu’un écran LCD/OLED ;</li>
<li>le confort réel du clavier et l’autonomie dépendent de l’usage et ne sont pas déduits ici des specs.</li>
</ul>
<h2 id="choix">Quand choisir Note Air5 C plutôt qu’une autre famille BOOX ?</h2>
<p>Il est cohérent si vous voulez un format 10,3 pouces, de la couleur, Android 15, un slot microSD et la possibilité d’ajouter un clavier dédié. Pour choisir entre les familles BOOX, revenez au {internal_link('/marques/boox/', 'hub BOOX')}. Pour les questions de politique de mises à jour, garantie, retours et confidentialité, consultez {internal_link('/marques/boox/avis/', 'l’avis sur BOOX comme marque')}. Les compatibilités matérielles sont détaillées dans {internal_link('/marques/boox/accessoires/', 'les accessoires BOOX')}.</p>
<h2 id="sources">Sources consultées</h2>
<p>Générations et caractéristiques revérifiées le {VERIFIED_DATE}.</p>
{_source_list(sources)}
'''


def _boox_tab_ultra():
    sources = [
        ('BOOX — Tab Ultra C Pro', 'https://shop.boox.com/products/tabultracpro'),
        ('BOOX — Note Air5 C', 'https://shop.boox.com/products/noteair5c'),
        ('BOOX — Tab X C', 'https://shop.boox.com/products/tabxc'),
    ]
    return f'''
<p class="article-answer"><strong>Le Tab Ultra C Pro reste officiellement documenté et commandable, mais il appartient à une génération plus ancienne que le Note Air5 C.</strong> Son intérêt en 2026 repose sur une combinaison particulière — clavier avec trackpad, caméra, microSD et Android — plutôt que sur le fait d’être le modèle BOOX le plus récent.</p>
<h2 id="positionnement">Une tablette PC E Ink de 10,3 pouces, pas un simple carnet</h2>
<p>La logique Tab Ultra est celle d’un appareil hybride : applications Android, clavier magnétique avec trackpad, caméra arrière 16 MP et stockage extensible. Ces éléments peuvent remplacer certaines tâches d’ordinateur, mais deviennent du poids et de la complexité inutiles si votre besoin se limite aux notes manuscrites et aux PDF.</p>
<h2 id="caracteristiques">Ce qu’il faut réellement comparer en 2026</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Point</th><th>Tab Ultra C Pro</th><th>Alternative interne BOOX</th></tr></thead><tbody>
<tr><td><strong>Format</strong></td><td>10,3 pouces Kaleido 3</td><td>Note Air5 C : 10,3 pouces ; Tab X C : 13,3 pouces</td></tr>
<tr><td><strong>Système</strong></td><td>Android 12</td><td>Note Air5 C : Android 15 ; Tab X C : Android 13</td></tr>
<tr><td><strong>Mémoire</strong></td><td>6 Go / 128 Go</td><td>Note Air5 C : 6/64 Go ; Tab X C : 6/128 Go</td></tr>
<tr><td><strong>Clavier</strong></td><td>cover magnétique avec trackpad</td><td>Note Air5 C et Tab X C ont leurs propres solutions clavier</td></tr>
<tr><td><strong>Caméra</strong></td><td>16 MP arrière</td><td>pas le point central des deux alternatives citées</td></tr>
<tr><td><strong>microSD</strong></td><td>oui</td><td>Note Air5 C : oui ; Tab X C : non listé</td></tr>
</tbody></table></div>
<h2 id="android">Android 12 est un facteur de génération, pas une date d’obsolescence</h2>
<p>Le système est plus ancien que celui des modèles BOOX cités ci-dessus. Cela doit entrer dans une décision qui dépend d’applications tierces, mais aucune date de fin de compatibilité future ne peut être déduite de ce seul numéro de version. La page ne présente donc pas le Tab Ultra C Pro comme « obsolète » tant que BOOX continue à le documenter et le vendre.</p>
<h2 id="choix">Quand le Tab Ultra C Pro garde-t-il du sens ?</h2>
<p>Il reste cohérent si vous voulez précisément un écran couleur 10,3 pouces avec caméra, microSD et clavier à trackpad. Si vous cherchez surtout un Android plus récent sur le même format, {internal_link('/marques/boox/boox-note-air/', 'Note Air5 C')} devient plus logique. Si votre problème est la surface de travail, le Tab X C 13,3 pouces répond à une autre contrainte.</p>
<p>Pour replacer ces modèles dans toute la gamme, voir {internal_link('/marques/boox/', 'le hub BOOX')}. Pour la confiance dans la marque, les mises à jour, la garantie ou les retours, utilisez {internal_link('/marques/boox/avis/', 'l’avis BOOX')}. Si la complexité Android elle-même est le problème, la page {internal_link('/marques/boox/alternatives/', 'alternatives à BOOX')} est la suite logique.</p>
<h2 id="sources">Sources consultées</h2>
<p>Statut et caractéristiques revérifiés le {VERIFIED_DATE}. La disponibilité commerciale peut évoluer selon le pays.</p>
{_source_list(sources)}
'''


LIGHT_BODIES = {
    '/marques/': _directory,
    '/marques/remarkable/abonnement-connect/': _remarkable_connect,
    '/marques/remarkable/remarkable-2/': _remarkable_2_product,
    '/marques/remarkable/remarkable-2-avis/': _remarkable_2_review,
    '/marques/remarkable/alternatives/': _remarkable_alternatives,
    '/marques/boox/alternatives/': _boox_alternatives,
    '/marques/boox/boox-note-air/': _boox_note_air,
    '/marques/boox/boox-tab-ultra/': _boox_tab_ultra,
}


def light_body(url, body):
    renderer = LIGHT_BODIES.get(url)
    return renderer() if renderer else body


def light_metadata(url, title, description):
    if url == '/marques/remarkable/abonnement-connect/':
        description = 'reMarkable Connect en 2026 : ce qui reste gratuit, règle des 50 jours, recherche manuscrite, cloud illimité, apps, intégrations et outils IA.'
    return title, description
