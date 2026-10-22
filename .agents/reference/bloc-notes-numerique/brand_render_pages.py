from brand_data import VERIFIED_AT
from brand_render_common import internal_link, sources_html, bullets


def _source_list(items):
    return '<ul class="source-list">' + ''.join(f'<li><a href="{url}" rel="noopener noreferrer">{label}</a></li>' for label, url in items) + '</ul>'


def _paper_pro_product_pilot():
    official_sources = [
        ('reMarkable Paper Pro — caractéristiques', 'https://remarkable.com/products/remarkable-paper/pro/details/features'),
        ('Comparateur officiel reMarkable', 'https://remarkable.com/products/remarkable-paper/pro/details/compare'),
        ('reMarkable Paper Pro — offre et Connect', 'https://remarkable.com/products/remarkable-paper/pro?region_id=000036'),
    ]
    return f'''
<p class="article-answer"><strong>Le reMarkable Paper Pro est le grand modèle couleur de la gamme, avec un écran 11,8 pouces, un éclairage réglable et un Marker inclus.</strong> Il convient surtout aux notes et aux PDF qui profitent d’une grande surface d’affichage. Son intérêt baisse si vous cherchez une tablette polyvalente avec des applications tierces ou si un format 10,3 pouces suffit.</p>
<h2 id="caracteristiques">Ce que vous achetez réellement</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Point</th><th>Paper Pro</th></tr></thead><tbody>
<tr><td><strong>Écran</strong></td><td>Canvas Color 11,8 pouces, 2160 × 1620, 229 ppp, éclairage réglable</td></tr>
<tr><td><strong>Format</strong></td><td>274,1 × 196,6 × 5,1 mm ; environ 525 g</td></tr>
<tr><td><strong>Stockage</strong></td><td>64 Go</td></tr>
<tr><td><strong>Stylet</strong></td><td>Marker ou Marker Plus inclus selon la configuration choisie, avec six mines de remplacement</td></tr>
<tr><td><strong>Documents</strong></td><td>import PDF et EPUB ; export PDF, PNG et SVG</td></tr>
<tr><td><strong>Système</strong></td><td>reMarkable OS, système Linux spécialisé dans le papier numérique</td></tr>
</tbody></table></div>
<p>Le Marker de cette génération se recharge sur la tablette et n’est pas interchangeable avec les anciens Markers de reMarkable 2. Si vous possédez déjà des accessoires reMarkable, la compatibilité mérite donc d’être vérifiée avant l’achat.</p>
<h2 id="ecran">À quoi servent vraiment le grand écran et la couleur ?</h2>
<p>Le format 11,8 pouces laisse davantage de place aux PDF, aux documents en deux colonnes, aux schémas et aux annotations en marge. La couleur ajoute surtout de la hiérarchie visuelle : surlignages, codes couleur et dessins deviennent plus faciles à distinguer qu’en noir et blanc.</p>
<p>Ce gain de surface a une contrepartie simple : avec 525 g et près de 27,5 cm de hauteur, Paper Pro est moins discret dans un sac ou à tenir longtemps qu’un modèle compact. Si vos notes sont courtes et vos PDF simples, le grand format peut être superflu.</p>
<h2 id="connect">Connect, cloud et applications : ce qui change</h2>
<p>Paper Pro fonctionne sans abonnement pour écrire et consulter vos documents. reMarkable indique toutefois que, sans Connect, seuls les fichiers utilisés et synchronisés au cours des 50 derniers jours restent stockés dans le cloud et que la prise de notes dans les applications mobile et desktop n’est pas disponible.</p>
<p>Connect ajoute notamment la recherche dans l’écriture manuscrite, le stockage cloud illimité, la synchronisation, des intégrations et des fonctions supplémentaires dans les applications. Si ces fonctions comptent dans votre usage quotidien, l’abonnement fait partie du coût réel du Paper Pro. Le détail est repris dans {internal_link('/marques/remarkable/abonnement-connect/','notre page sur reMarkable Connect')}.</p>
<h2 id="accessoires">Marker, Folio et Type Folio : quels surcoûts prévoir ?</h2>
<p>Le Marker standard est inclus dans la configuration de base. Le Marker Plus, qui ajoute notamment une gomme à son extrémité, représente un surcoût. Les Folios et le Type Folio sont également optionnels.</p>
<p>Pour un usage principalement manuscrit à domicile ou au bureau, il n’est pas nécessaire d’ajouter tous les accessoires. Le Type Folio a surtout du sens si vous voulez réellement taper de longs passages sur le Paper Pro plutôt que reprendre votre ordinateur. Voir aussi {internal_link('/marques/remarkable/accessoires/','les accessoires reMarkable')}.</p>
<h2 id="limites">Les limites à connaître avant l’achat</h2>
<ul>
<li>reMarkable OS n’offre pas le même catalogue d’applications qu’une tablette Android ;</li>
<li>le grand format augmente l’encombrement et le poids ;</li>
<li>certaines fonctions cloud et applicatives sont liées à Connect ;</li>
<li>les anciens Markers de reMarkable 2 ne sont pas compatibles avec Paper Pro.</li>
</ul>
<p>Si l’ouverture logicielle est indispensable, le {internal_link('/comparatifs/remarkable-vs-boox/','comparatif reMarkable vs BOOX')} est plus utile qu’une comparaison de fiches techniques. Si vous hésitez surtout entre les modèles de la marque, revenez à {internal_link('/marques/remarkable/','la gamme reMarkable')}.</p>
<h2 id="choix">Paper Pro est-il le bon modèle pour vous ?</h2>
<p><strong>Paper Pro mérite surtout d’être retenu si vous annotez souvent de grands documents, utilisez réellement la couleur ou travaillez dans des conditions où l’éclairage intégré est utile.</strong> Pour de la prise de notes simple en noir et blanc, un modèle plus petit peut couvrir le même besoin avec moins d’encombrement.</p>
<p>Si vous cherchez un jugement plus critique sur le confort, la simplicité du logiciel, la couleur et le rapport entre prix et usage, consultez {internal_link('/marques/remarkable/remarkable-paper-pro-avis/','notre avis sur le reMarkable Paper Pro')}.</p>
<h2 id="sources">Sources consultées</h2>
<p>Caractéristiques et services vérifiés le {VERIFIED_AT}. Prix et disponibilité restent à recontrôler au moment de l’achat.</p>{_source_list(official_sources)}
'''


def product_page(title, brand, status, answer, facts, workflow, limitations, choose, avoid, alternatives):
    if title == 'reMarkable Paper Pro':
        return _paper_pro_product_pilot()
    rows = ''.join(f'<tr><td><strong>{k}</strong></td><td>{v}</td></tr>' for k, v in facts)
    table = f'<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Point</th><th>Information vérifiée</th></tr></thead><tbody>{rows}</tbody></table></div>'
    return f'''
<p class="article-answer"><strong>{answer}</strong> Le statut de cette page est <em>{status}</em>. Les informations ci-dessous sont une synthèse documentaire vérifiée le {VERIFIED_AT} ; aucune sensation d’écriture ou performance vécue n’est inventée.</p>
<h2 id="statut">Où se situe {title} dans la gamme actuelle ?</h2><p>{status}. Cette distinction évite de présenter une génération ancienne ou une famille historique comme le choix neuf de référence. Pour replacer le modèle dans son contexte, consultez la {internal_link(f'/marques/{brand}/','page marque')} et le {internal_link('/comparatifs/meilleur-bloc-notes-numerique/','comparatif général')}.</p><p>Le statut produit influence aussi les accessoires, le système et les services disponibles. Avant une commande, vérifiez donc le nom exact, la génération et la région de vente.</p>
<h2 id="caracteristiques">Les caractéristiques qui changent réellement l’usage</h2><p>Nous retenons les éléments qui modifient le workflow plutôt que de recopier toute la fiche constructeur.</p>{table}<p>Une caractéristique n’est pas automatiquement un avantage : un grand écran apporte de la surface mais aussi de l’encombrement ; davantage d’applications apporte de la flexibilité mais aussi plus de réglages.</p>
<h2 id="workflow">Comment le modèle s’intègre dans un workflow</h2>{''.join(f'<p>{p}</p>' for p in workflow)}<p>Testez mentalement un document complet : import, annotation, classement, recherche puis export. Les guides sur {internal_link('/guides/formats-fichiers-compatibles/','les formats compatibles')}, {internal_link('/guides/synchroniser-notes-cloud/','la synchronisation cloud')} et {internal_link('/guides/exporter-notes/','l’export')} permettent de vérifier chaque étape.</p>
<h2 id="limites">Les limites à ne pas masquer</h2>{bullets(limitations)}<p>Une limite structurelle compte plus qu’une petite différence de fiche technique. Si elle touche votre tâche principale, le modèle doit sortir de la shortlist.</p>
<h2 id="pour-qui">Pour qui ce modèle reste cohérent ?</h2><p><strong>À privilégier si :</strong></p>{bullets(choose)}<p><strong>À éviter si :</strong></p>{bullets(avoid)}
<h2 id="alternatives">Quelles alternatives regarder ?</h2><ul>{''.join(f'<li>{internal_link(url,label)}</li>' for label,url in alternatives)}</ul><p>L’alternative utile est celle qui corrige la limite principale sans dégrader une fonction plus importante.</p>
<h2 id="preuve">Ce que la fiche technique ne permet pas de conclure</h2><p>Une fiche constructeur permet de vérifier une diagonale, un format, un système ou une intégration. Elle ne permet pas, à elle seule, d’affirmer qu’un stylet « ressemble au papier », qu’un appareil reste confortable plusieurs heures ou qu’une autonomie annoncée sera reproduite dans votre usage. Ces points nécessitent un test documenté.</p><p>Nous distinguons donc les faits de l’interprétation : présence d’une fonction = fait vérifiable ; pertinence pour un profil = conclusion éditoriale.</p>
<h2 id="checklist">Checklist avant achat</h2><ol><li>Confirmez la génération exacte.</li><li>Vérifiez votre PDF ou format principal.</li><li>Contrôlez cloud et export.</li><li>Ajoutez stylet, protection et abonnement éventuel au coût total.</li><li>Comparez une alternative qui corrige la principale limite.</li></ol><p>Le guide sur {internal_link('/guides/prix-bloc-notes-numerique/','le prix réel')} aide à comparer des configurations équivalentes.</p>
<h2 id="sources">Sources officielles consultées</h2><p>Informations vérifiées le {VERIFIED_AT}. Prix et disponibilité restent à recontrôler au moment de l’achat.</p>{sources_html([brand],5)}
'''


def _paper_pro_review_pilot():
    official_sources = [
        ('reMarkable Paper Pro — caractéristiques', 'https://remarkable.com/products/remarkable-paper/pro/details/features'),
        ('Comparateur officiel reMarkable', 'https://remarkable.com/products/remarkable-paper/pro/details/compare'),
        ('reMarkable Paper Pro — offre et Connect', 'https://remarkable.com/products/remarkable-paper/pro?region_id=000036'),
    ]
    independent_sources = [
        ('TechRadar — reMarkable Paper Pro review', 'https://www.techradar.com/tablets/remarkable-paper-pro-review'),
        ('WIRED — Review: ReMarkable Paper Pro', 'https://www.wired.com/review/remarkable-paper-pro/'),
        ('Tom’s Guide — ReMarkable Paper Pro review', 'https://www.tomsguide.com/tablets/remarkable-paper-pro'),
        ('Forbes Vetted — ReMarkable Paper Pro Review', 'https://www.forbes.com/sites/forbes-personal-shopper/article/remarkable-paper-pro-review/'),
        ('Engadget — reMarkable Paper Pro review', 'https://www.engadget.com/mobile/tablets/remarkable-paper-pro-review-writing-in-color-is-nice-but-itll-cost-you-173024590.html'),
    ]
    return f'''
<p class="article-answer"><strong>Notre avis : le reMarkable Paper Pro est convaincant si vous voulez un grand carnet numérique centré sur l’écriture et l’annotation, avec couleur et éclairage, mais son prix et son logiciel volontairement limité le rendent moins intéressant comme tablette polyvalente.</strong> Il s’agit d’une analyse documentaire : nous croisons la documentation reMarkable avec plusieurs essais indépendants, sans présenter leurs observations comme une expérience réalisée par nos soins.</p>
<h2 id="forces">Pourquoi le Paper Pro convainc</h2>
<p>Le passage à un écran couleur de 11,8 pouces et l’arrivée de l’éclairage changent réellement le produit par rapport aux anciens reMarkable. Les essais de TechRadar, WIRED, Tom’s Guide et Engadget convergent sur un point : la force du Paper Pro reste son environnement d’écriture volontairement simple, désormais plus confortable pour les documents en couleur et les usages en faible lumière.</p>
<p>Le grand écran est particulièrement intéressant pour les PDF, les annotations en marge et les pages qui deviennent vite étroites sur un format 10 pouces. Forbes Vetted, après plusieurs semaines de test, met également en avant l’éclairage et l’organisation des notes comme des améliorations utiles au quotidien.</p>
<h2 id="couleur">La couleur est utile, mais ce n’est pas un écran de tablette classique</h2>
<p>La couleur sert bien aux surlignages, schémas et codes visuels. Elle n’a pas vocation à remplacer un écran LCD ou OLED pour la photo, la vidéo ou une restitution très vive. C’est une différence importante : Paper Pro gagne en lisibilité documentaire sans devenir une tablette multimédia.</p>
<p>Tom’s Guide souligne aussi qu’un certain délai reste perceptible dans l’expérience, malgré les progrès de réactivité. Pour de l’écriture et de l’annotation, cela n’annule pas l’intérêt du produit, mais il faut éviter d’attendre la fluidité d’un iPad.</p>
<h2 id="limites">Ce qui peut faire renoncer</h2>
<p>Le principal compromis est le même dans plusieurs essais indépendants : Paper Pro coûte cher pour un appareil qui choisit délibérément de faire moins de choses qu’une tablette généraliste. WIRED apprécie sa simplicité mais pointe le prix et l’impossibilité de réutiliser l’ancien stylet ; TechRadar juge cette simplicité efficace pour la concentration mais frustrante dès que l’on attend davantage de polyvalence.</p>
<ul>
<li>pas de catalogue d’applications comparable à Android ou iPadOS ;</li>
<li>format 11,8 pouces moins pratique si la mobilité prime ;</li>
<li>anciens Markers reMarkable 2 incompatibles ;</li>
<li>certaines fonctions cloud avancées passent par Connect.</li>
</ul>
<h2 id="connect">Connect change-t-il notre avis ?</h2>
<p>Pas pour l’écriture de base : le Paper Pro reste utilisable sans abonnement. En revanche, Connect devient important si vous comptez sur la recherche manuscrite, le stockage cloud illimité ou la prise de notes depuis les applications reMarkable. Sans Connect, reMarkable limite notamment le stockage cloud aux fichiers utilisés et synchronisés dans les 50 derniers jours.</p>
<p>Pour un usage centré sur le carnet local et l’export ponctuel, ce coût peut rester secondaire. Pour un usage multi-appareils intensif, il doit être intégré dès le départ. Voir {internal_link('/marques/remarkable/abonnement-connect/','reMarkable Connect')}.</p>
<h2 id="pour-qui">À qui le Paper Pro convient le mieux ?</h2>
<ul>
<li>aux personnes qui annotent régulièrement des PDF ou travaillent sur de grands documents ;</li>
<li>à celles qui utilisent la couleur comme code visuel plutôt que pour du contenu multimédia ;</li>
<li>à celles qui veulent réduire les notifications et applications pendant l’écriture.</li>
</ul>
<p>Nous le conseillerions moins si vous avez besoin d’applications Android, si le prix est le critère principal ou si un écran noir et blanc plus compact répond déjà à vos notes quotidiennes.</p>
<h2 id="alternatives">Quelles alternatives regarder avant d’acheter ?</h2>
<p>Le concurrent à examiner dépend surtout de ce qui vous gêne chez reMarkable. Pour davantage d’applications et d’ouverture, commencez par {internal_link('/comparatifs/remarkable-vs-boox/','reMarkable vs BOOX')}. Pour une organisation des notes plus structurée, regardez {internal_link('/comparatifs/remarkable-vs-supernote/','reMarkable vs Supernote')}. Si votre hésitation porte surtout sur la technologie couleur, le {internal_link('/comparatifs/bloc-notes-numerique-couleur/','comparatif des bloc-notes numériques couleur')} est plus pertinent.</p>
<h2 id="verdict">Verdict</h2>
<p><strong>Paper Pro est l’un des choix les plus aboutis pour écrire et annoter sur un grand écran E Ink couleur sans transformer l’appareil en tablette généraliste.</strong> Son intérêt repose précisément sur cette spécialisation. Si vous cherchez davantage d’applications, de navigation web ou de polyvalence, son prix devient difficile à justifier face à des alternatives plus ouvertes.</p>
<h2 id="methode">Sur quoi repose cet avis ?</h2>
<p>Les caractéristiques, compatibilités et fonctions Connect sont vérifiées auprès de reMarkable. Les éléments liés au confort d’écriture, à la réactivité, à la couleur et à l’usage prolongé proviennent d’essais indépendants réalisés par TechRadar, WIRED, Tom’s Guide, Forbes Vetted et Engadget. Nous n’avons pas réalisé de test physique du Paper Pro.</p>
<h2 id="sources">Sources consultées</h2>
<h3>Sources officielles</h3>{_source_list(official_sources)}
<h3>Essais indépendants</h3>{_source_list(independent_sources)}
'''


def review_page(product, brand, verdict, strengths, limitations, evidence_points, who, avoid, alternatives):
    if product == 'reMarkable Paper Pro':
        return _paper_pro_review_pilot()
    rows=''.join(f'<tr><td>{d}</td><td>{claim}</td><td>{level}</td></tr>' for d,claim,level in evidence_points)
    evidence=f'<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Dimension</th><th>Ce que la documentation permet d’affirmer</th><th>Niveau</th></tr></thead><tbody>{rows}</tbody></table></div>'
    return f'''
<p class="article-answer"><strong>{verdict}</strong> Cette page est une <strong>analyse documentaire</strong>, pas le compte rendu d’un test physique. Les caractéristiques vérifiées sont séparées de leur interprétation éditoriale.</p>
<h2 id="preuve">Quel est le niveau de preuve de cet avis ?</h2><p>Nous n’attribuons ni sensation de stylet, ni latence mesurée, ni autonomie réelle sans protocole de test documenté.</p>{evidence}<p>Le fabricant peut documenter une fonction ; conclure qu’elle est préférable pour un profil reste une déduction à expliquer.</p>
<h2 id="forces">Les points forts que l’on peut défendre</h2>{bullets(strengths)}<p>Ces avantages prennent leur sens dans le {internal_link(f'/marques/{brand}/','positionnement global de la marque')} et ne constituent pas une note de laboratoire.</p>
<h2 id="limites">Les limites qui peuvent faire changer de choix</h2>{bullets(limitations)}<p>Le but d’un avis affilié utile est aussi de permettre au lecteur de ne pas acheter le produit.</p>
<h2 id="workflow">Ce que cela implique dans un workflow réel</h2><p>Suivez un fichier représentatif : import, annotation, classement, recherche, export et ouverture sur un autre appareil. Vérifiez aussi les accessoires et services nécessaires à cette chaîne.</p><p>Pour refaire cette analyse, utilisez les guides sur {internal_link('/guides/annoter-pdf-tablette-e-ink/','l’annotation PDF')}, {internal_link('/guides/exporter-notes/','l’export')} et {internal_link('/guides/prix-bloc-notes-numerique/','le coût total')}.</p>
<h2 id="pour-qui">Pour qui {product} est cohérent ?</h2>{bullets(who)}<p><strong>À éviter si :</strong></p>{bullets(avoid)}
<h2 id="alternatives">Alternatives et comparatifs utiles</h2><ul>{''.join(f'<li>{internal_link(url,label)}</li>' for label,url in alternatives)}</ul>
<h2 id="incertitudes">Ce que cette analyse ne prétend pas mesurer</h2><p>Nous ne disposons pas ici d’un protocole physique standardisé pour comparer la latence réelle, le bruit du stylet, la fatigue sur plusieurs heures ou la durée de batterie. Une valeur constructeur est traitée comme une donnée déclarée, pas comme une mesure indépendante.</p><p>Cette séparation évite de transformer une synthèse de sources en faux test, tout en conservant une vraie valeur décisionnelle.</p>
<h2 id="verification">Comment vérifier ce verdict pour votre usage</h2><p>Choisissez votre tâche la plus importante et cherchez le premier point de friction possible. S’il reste incertain, il doit peser davantage que les avantages secondaires. Croisez ensuite avec un comparatif multi-marques pour vérifier que l’alternative corrige réellement le problème.</p>
<h2 id="verdict">Verdict éditorial</h2><p>{verdict} Ce verdict est conditionnel à l’usage et au niveau de preuve disponible ; il ne doit pas être lu comme une note issue d’un laboratoire.</p>
<h2 id="sources">Sources officielles consultées</h2>{sources_html([brand],5)}
'''


def service_page():
    return f'''
<p class="article-answer"><strong>reMarkable Connect n’est pas nécessaire pour écrire sur une tablette reMarkable, mais il devient important si vous voulez certaines fonctions cloud et applicatives avancées.</strong> La frontière entre fonctions de base et service payant a été vérifiée le {VERIFIED_AT}.</p>
<h2 id="definition">Connect, qu’est-ce que c’est ?</h2><p>Connect est l’abonnement de services associé à reMarkable. Les fonctions de base de prise de notes restent sur le matériel ; l’abonnement ajoute surtout une couche cloud et logicielle entre tablette, ordinateur, téléphone et intégrations.</p><p>Il faut donc juger Connect comme un composant du workflow, pas comme une option abstraite ajoutée au panier.</p>
<h2 id="avec-sans">Ce qui change avec ou sans abonnement</h2><p>Stockage, synchronisation et fonctions avancées doivent être séparés.</p><div class="table-wrapper"><table class="comp-table"><thead><tr><th>Besoin</th><th>Sans Connect</th><th>Avec Connect</th></tr></thead><tbody><tr><td>Écrire sur la tablette</td><td>Oui</td><td>Oui</td></tr><tr><td>Cloud</td><td>règles et limites à vérifier</td><td>stockage illimité annoncé</td></tr><tr><td>Recherche manuscrite</td><td>selon offre</td><td>fonction mise en avant</td></tr><tr><td>Apps bureau/mobile</td><td>fonctions de base</td><td>fonctions supplémentaires</td></tr><tr><td>Intégrations</td><td>à vérifier selon fonction</td><td>workflow étendu</td></tr></tbody></table></div><p>Le tableau sert à identifier la fonction réellement payante dans votre cas. Le prix du service doit être revérifié le jour de l’achat.</p>
<h2 id="cout">Comment décider si le coût est justifié</h2><p>Partez de la fonction qui vous manque sans Connect, puis calculez son coût sur la durée pendant laquelle vous pensez garder l’appareil. Le guide {internal_link('/guides/bloc-notes-numerique-avec-ou-sans-abonnement/','avec ou sans abonnement')} fournit une méthode neutre.</p>
<h2 id="donnees">Cloud et dépendance : la vraie question</h2><p>Vérifiez que vous savez toujours récupérer vos notes dans un format exploitable, même si vous arrêtez de payer. Consultez {internal_link('/guides/exporter-notes/','l’export')}, {internal_link('/guides/bloc-notes-numerique-google-drive/','Google Drive')}, {internal_link('/guides/bloc-notes-numerique-onedrive/','OneDrive')} et {internal_link('/guides/bloc-notes-numerique-dropbox/','Dropbox')}.</p>
<h2 id="essentiel">Quelles fonctions doivent rester indépendantes du service ?</h2><p>Pour un outil durable, l’écriture locale, l’accès aux notes et une méthode d’export exploitable doivent peser plus lourd que le confort cloud. Simulez une semaine sans abonnement : si votre travail devient impossible, Connect fait partie du coût structurel ; sinon, il finance surtout du confort.</p>
<h2 id="pour-qui">Pour qui Connect est cohérent ?</h2><p><strong>À privilégier si :</strong></p><ul><li>vous utilisez activement le cloud et les apps reMarkable ;</li><li>la recherche manuscrite vous fait gagner du temps ;</li><li>les intégrations font partie du travail quotidien.</li></ul><p><strong>À éviter ou différer si :</strong></p><ul><li>vous travaillez surtout hors ligne ;</li><li>des exports PDF suffisent ;</li><li>vous refusez tout coût récurrent.</li></ul>
<h2 id="alternatives">Quelles alternatives si vous refusez l’abonnement ?</h2><p>Le {internal_link('/comparatifs/bloc-notes-numerique-sans-abonnement/','comparatif sans abonnement')} est la suite logique. Comparez la fonction équivalente — cloud, OCR, recherche ou export — et pas seulement la présence d’un paiement.</p>
<h2 id="sources">Sources officielles consultées</h2>{sources_html(['remarkable'],5)}
'''


def accessories_page(brand):
    if brand == 'remarkable':
        intro='Les accessoires reMarkable ne sont pas tous interchangeables entre reMarkable 2 et la génération Paper Pure / Paper Pro / Paper Pro Move.'
        rows=[('Marker / Marker Plus','NÉCESSAIRE','écriture','vérifier la génération'),('Mines','À PRÉVOIR','maintenir la pointe','compatibilité générationnelle'),('Folio','RECOMMANDÉ','protection','choisir le modèle exact'),('Type Folio','OPTIONNEL','saisie clavier','utile seulement si vous tapez réellement')]
        links=[('Paper Pro','/marques/remarkable/remarkable-paper-pro/'),('reMarkable 2','/marques/remarkable/remarkable-2/'),('prix total','/guides/prix-bloc-notes-numerique/'),('reMarkable vs BOOX','/comparatifs/remarkable-vs-boox/')]
    else:
        intro='Chez BOOX, la compatibilité des stylets, étuis et claviers dépend fortement du modèle et de sa génération.'
        rows=[('Stylet BOOX','NÉCESSAIRE','écriture','Pen3, Pen Plus ou InkSense selon modèle'),('Étui','RECOMMANDÉ','protection','dimensions spécifiques'),('Clavier','OPTIONNEL','saisie','connectique et modèle à vérifier'),('microSD','OPTIONNEL','stockage','slot à vérifier')]
        links=[('famille Note Air','/marques/boox/boox-note-air/'),('famille Tab Ultra','/marques/boox/boox-tab-ultra/'),('prix total','/guides/prix-bloc-notes-numerique/'),('BOOX vs Supernote','/comparatifs/boox-vs-supernote/')]
    table='<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Accessoire</th><th>Priorité</th><th>Rôle</th><th>Vigilance</th></tr></thead><tbody>'+''.join(f'<tr><td>{a}</td><td>{p}</td><td>{r}</td><td>{v}</td></tr>' for a,p,r,v in rows)+'</tbody></table></div>'
    return f'''
<p class="article-answer"><strong>{intro}</strong> Commencez par les accessoires indispensables à votre usage, puis ajoutez seulement les options qui remplacent une tâche réelle.</p>
<h2 id="priorites">Obligatoire, recommandé ou optionnel ?</h2><p>Un bundle n’est pas automatiquement une meilleure configuration.</p>{table}<p>Cette hiérarchie permet de comparer des paniers équivalents dans le guide sur {internal_link('/guides/prix-bloc-notes-numerique/','le prix réel')}.</p>
<h2 id="compatibilite">La compatibilité est plus importante que le logo</h2><p>Vérifiez génération, diagonale, fixation, technologie du stylet et ports. Un accessoire officiel d’une génération précédente peut être inutilisable sur le produit actuel.</p>
<h2 id="stylet">Le stylet est l’accessoire qui change le plus l’usage</h2><p>Gomme, boutons, recharge, technologie de détection et mines varient selon les gammes. Le guide sur {internal_link('/guides/latence-ecriture/','la latence d’écriture')} rappelle pourquoi le ressenti ne peut pas être déduit du stylet seul.</p>
<h2 id="protection">Étui et protection : utile si l’appareil voyage</h2><p>Comparez poids et épaisseur avec l’étui monté. Une protection devient rationnelle si l’appareil circule chaque jour ; elle est moins prioritaire pour un usage fixe.</p>
<h2 id="clavier">Clavier : ne le payez que s’il remplace une vraie tâche</h2><p>Un clavier a de la valeur si vous tapez suffisamment de texte pour éviter de reprendre l’ordinateur. Sinon, il augmente surtout le prix et le poids.</p>
<h2 id="panier">Comment construire votre panier</h2><ol><li>Choisissez le modèle exact.</li><li>Ajoutez le stylet nécessaire.</li><li>Ajoutez une protection si le transport le justifie.</li><li>Ajoutez clavier ou stockage seulement si une tâche l’exige.</li><li>Comparez le total.</li></ol><p>Pages utiles : {', '.join(internal_link(url,label) for label,url in links)}.</p>
<h2 id="duree">Rapportez le coût à la durée et à la fonction</h2><p>Un accessoire cher peut être rationnel s’il protège chaque jour un appareil coûteux ou remplace réellement une tâche. Pour les consommables, regardez aussi disponibilité et fréquence de remplacement sur plusieurs années.</p>
<h2 id="limites">À éviter</h2><ul><li>acheter un bundle sans comprendre chaque élément ;</li><li>mélanger anciennes et nouvelles générations ;</li><li>présenter un accessoire officiel comme indispensable sans preuve ;</li><li>comparer un appareil nu à un bundle concurrent.</li></ul>
<h2 id="sources">Sources officielles consultées</h2>{sources_html([brand],5)}
'''


def alternatives_page(brand):
    if brand == 'remarkable':
        intro='La meilleure alternative à reMarkable dépend de la raison qui vous fait quitter son écosystème.'
        reasons=[('Applications et ouverture','BOOX','/comparatifs/remarkable-vs-boox/'),('Organisation des connaissances','Supernote','/comparatifs/remarkable-vs-supernote/'),('Lecture Kindle','Kindle Scribe','/comparatifs/kindle-scribe-vs-remarkable/'),('Lecture Kobo','Kobo Elipsa 2E','/comparatifs/kobo-elipsa-vs-remarkable/')]
    else:
        intro='La meilleure alternative à BOOX dépend de ce que l’ouverture Android vous coûte en complexité.'
        reasons=[('Simplicité','reMarkable','/comparatifs/remarkable-vs-boox/'),('Organisation spécialisée','Supernote','/comparatifs/boox-vs-supernote/'),('Lecture Kindle','Kindle Scribe','/marques/kindle-scribe/'),('Lecture Kobo','Kobo Elipsa 2E','/marques/kobo-elipsa/')]
    rows=''.join(f'<tr><td>{r}</td><td>{a}</td><td>{internal_link(url,"Voir le comparatif")}</td></tr>' for r,a,url in reasons)
    return f'''
<p class="article-answer"><strong>{intro}</strong> Nous ne classons pas les alternatives sur un score unique : le critère qui vous fait changer doit déterminer la shortlist.</p>
<h2 id="raison">Commencez par la raison de votre départ</h2><p>Une alternative n’est pertinente que si elle corrige la limite rencontrée.</p><div class="table-wrapper"><table class="comp-table"><thead><tr><th>Pourquoi changer ?</th><th>Alternative</th><th>Suite</th></tr></thead><tbody>{rows}</tbody></table></div><p>Cette méthode évite de recommander le même concurrent à tout le monde.</p>
<h2 id="workflow">Comparez le workflow, pas le nombre de fonctions</h2><p>Suivez un document depuis son import jusqu’à l’export : annotation, recherche, cloud et format de sortie. Le guide sur {internal_link('/guides/ecosysteme-ouvert-ou-ferme/','les écosystèmes')} donne une grille neutre.</p>
<h2 id="cout">Comparez aussi le coût de la configuration</h2><p>Stylet, protection, clavier et services peuvent déplacer le coût final. Voir {internal_link('/guides/prix-bloc-notes-numerique/','prix et budget')}.</p>
<h2 id="rester">Quand rester dans l’écosystème actuel ?</h2><p>Si l’appareil couvre déjà vos tâches centrales et que le problème se résout par un export ou un accessoire raisonnable, migrer peut créer plus de friction que de valeur.</p>
<h2 id="eviter">Quand faut-il réellement envisager une alternative ?</h2><ul><li>application indispensable absente ;</li><li>documents impossibles à exporter dans le bon format ;</li><li>coût récurrent incompatible ;</li><li>taille, couleur ou éclairage inadéquats ;</li><li>organisation des notes devenue un frein.</li></ul>
<h2 id="migration">Le coût caché d’un changement d’écosystème</h2><p>Changer de marque peut exiger l’export d’anciens carnets, la conversion de fichiers ou la reconstruction de dossiers. Avant de migrer, exportez un échantillon représentatif et vérifiez qu’il reste réellement exploitable dans le nouveau système.</p><p>Une alternative plus ouverte sur le papier peut être moins intéressante si elle vous fait perdre la structure de plusieurs années de notes.</p>
<h2 id="shortlist">Construire une shortlist utile</h2><p>Ne gardez que deux ou trois options qui corrigent votre problème principal. Si vous quittez reMarkable pour Android, BOOX mérite plus d’attention que Kobo ; si vous quittez BOOX pour simplifier, reMarkable ou Supernote deviennent plus logiques.</p>
<h2 id="comparatifs">Comparatifs à consulter</h2><p>{internal_link('/comparatifs/meilleur-bloc-notes-numerique/','général')}, {internal_link('/comparatifs/bloc-notes-numerique-professionnel/','professionnels')}, {internal_link('/comparatifs/bloc-notes-numerique-etudiant/','étudiants')} et {internal_link('/comparatifs/bloc-notes-numerique-sans-abonnement/','sans abonnement')}.</p>
<h2 id="sources">Sources officielles consultées</h2>{sources_html(['remarkable','boox','supernote','kindle','kobo'],8)}
'''


def directory_page():
    brands=[('reMarkable','écriture spécialisée et concentration','/marques/remarkable/'),('BOOX','Android, applications et formats','/marques/boox/'),('Kindle Scribe','lecture Kindle + écriture','/marques/kindle-scribe/'),('Kobo Elipsa','lecture Kobo + annotation','/marques/kobo-elipsa/'),('Supernote','organisation de notes et réparabilité','/marques/supernote/')]
    rows=''.join(f'<tr><td>{internal_link(url,name)}</td><td>{focus}</td></tr>' for name,focus,url in brands)
    return f'''
<p class="article-answer"><strong>Les principales marques de bloc-notes numériques ne se distinguent pas seulement par leur écran : chacune organise différemment le matériel, le stylet, les notes, le cloud et les applications.</strong> Ce hub sert à choisir l’écosystème à explorer avant le modèle précis.</p>
<h2 id="marques">Cinq écosystèmes à distinguer</h2><p>Le tableau résume leur centre de gravité ; il ne constitue pas un classement.</p><div class="table-wrapper"><table class="comp-table"><thead><tr><th>Marque</th><th>Centre de gravité</th></tr></thead><tbody>{rows}</tbody></table></div><p>Commencez par la marque dont le workflow correspond le mieux à vos outils existants.</p>
<h2 id="remarkable">reMarkable : spécialisation et concentration</h2><p>{internal_link('/marques/remarkable/','reMarkable')} privilégie le papier numérique spécialisé. Sa gamme actuelle est structurée autour de Paper Pure, Paper Pro Move et Paper Pro ; reMarkable 2 est désormais une génération arrêtée.</p>
<h2 id="boox">BOOX : Android et ouverture</h2><p>{internal_link('/marques/boox/','BOOX')} couvre un spectre large, du Go 10.3 au Note Air5 C, Note Max ou Tab X C. Applications Android, PDF et clouds tiers sont ses différences majeures.</p>
<h2 id="kindle-kobo">Kindle Scribe et Kobo Elipsa : la lecture comme point de départ</h2><p>{internal_link('/marques/kindle-scribe/','Kindle Scribe')} part de l’écosystème Amazon et ajoute carnets, Workspace et connexions cloud sur les générations récentes. {internal_link('/marques/kobo-elipsa/','Kobo Elipsa 2E')} part de la lecture Kobo et ajoute carnets, stylet, Drive et Dropbox.</p>
<h2 id="supernote">Supernote : organiser des connaissances</h2><p>{internal_link('/marques/supernote/','Supernote')} structure sa gamme autour de Manta et Nomad, avec liens entre notes, reconnaissance manuscrite et une logique de réparabilité.</p>
<h2 id="choisir">Comment choisir une marque avant le modèle ?</h2><ol><li>Listez trois tâches.</li><li>Notez clouds et applications indispensables.</li><li>Vérifiez un PDF et un carnet.</li><li>Éliminez les écosystèmes bloquants.</li><li>Comparez les modèles restants.</li></ol><p>Suivez le {internal_link('/guides/choisir-bloc-notes-numerique/','guide de choix')} ou le {internal_link('/comparatifs/meilleur-bloc-notes-numerique/','comparatif')}.</p>
<h2 id="workflow">Comparer les marques sur un workflow complet</h2><p>Prenez un document réel : où arrive-t-il, peut-on l’annoter, le retrouver et le ressortir dans un format utilisable ailleurs ? Cette chaîne révèle davantage que le nombre de fonctions affichées.</p><p>Les différences sont fortes sur le cloud : Kindle travaille par copies avec Drive/OneDrive sur les modèles récents ; Kobo dépend du type de contenu et des DRM ; BOOX mise sur Android et plusieurs clouds ; reMarkable concentre le workflow dans son propre environnement ; Supernote mise davantage sur la structure des notes.</p>
<h2 id="limites">Pourquoi ne pas choisir uniquement sur la marque ?</h2><p>Une même marque propose plusieurs générations, formats et technologies. La marque donne le cadre ; le modèle doit encore correspondre à vos documents, votre mobilité et votre budget.</p>
<h2 id="sources">Sources officielles consultées</h2>{sources_html(['remarkable','boox','kindle','kobo','supernote'],10)}
'''