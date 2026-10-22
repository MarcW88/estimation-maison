#!/usr/bin/env python3
"""Generate the eight brand hubs from explicit current-range and ecosystem data.

Desk research only. This script post-processes existing /marques/<slug>/index.html shells
and deliberately preserves their robots directive and global layout.
"""
from pathlib import Path
from html import escape
import json
import re

BASE = Path(__file__).resolve().parent
UPDATED = "08/09/2026"

BRANDS = {
"karcher": {
 "name":"Kärcher","title":"Kärcher — Aspirateurs de chantier WD et NT : gamme 2026","desc":"Gamme Kärcher 2026 : aspirateurs eau et poussière WD, aspirateurs professionnels NT, classes L/M/H, Tact, ACD, forces et limites.",
 "quick":"Kärcher est l'une des marques les plus larges de ce marché : la famille <strong>WD</strong> vise surtout le nettoyage eau/poussière, le garage et la rénovation, tandis que la gamme professionnelle <strong>NT</strong> couvre les chantiers exigeants et des aspirateurs de sécurité L, M ou H. Le bon choix dépend donc davantage de la famille que du logo Kärcher lui-même.",
 "distinct":[
  "Kärcher sépare assez nettement deux univers. Les WD Home & Garden sont pensés comme des aspirateurs eau et poussière polyvalents : liquide, gravats, garage, véhicule, atelier et bricolage. Les NT Professional ajoutent, selon les références, surveillance du débit, système antistatique, prise asservie, décolmatage Tact et classifications de poussières adaptées aux usages professionnels.",
  "Cette largeur est un avantage, mais crée aussi un piège de lecture : un WD très performant sur le papier ne devient pas un aspirateur de sécurité. Le WD 7 Control annonce par exemple 80 l/s et 290 mbar, alors qu'un NT 30/1 Tact Te M ACD est choisi d'abord pour sa classe M, son contrôle du débit et son système Tact. Les chiffres d'aspiration ne remplacent jamais l'évaluation du risque poussière.",
 ],
 "range":[
  ["WD 3 / WD 4 / WD 5 / WD 6", "CURRENT", "Bricolage et nettoyage eau/poussière", "Famille Home & Garden, du format simple au modèle plus équipé."],
  ["WD 7 Control", "CURRENT", "Rénovation et atelier polyvalents", "30 L, 80 l/s et 290 mbar annoncés, prise outil et télécommande 2-en-1."],
  ["NT 30/1 Tact Te M ACD", "CURRENT", "Poussières fines et chantier pro", "Classe M, 30 L, Tact automatique commandé par capteur et certification ACD."],
  ["NT 50/1 Tact Te M ACD", "CURRENT", "Gros volumes en classe M", "Cuve 50 L, Tact, surveillance du débit, prise asservie."],
  ["NT Tact Te H / H ACD", "CURRENT", "Poussières relevant de la classe H", "Références dédiées ; le choix doit suivre le risque et les prescriptions applicables."],
  ["WD 2 Plus et anciennes variantes WD", "PREVIOUS_GENERATION", "Occasion / anciens catalogues", "Ne pas les confondre avec la gamme actuellement mise en avant en France."],
 ],
 "ecosystem":[
  "L'écosystème Kärcher repose moins sur une plateforme batterie d'outillage que sur la continuité entre accessoires, flexibles, filtres, sacs et familles de machines. Sur les WD, l'intérêt vient de la polyvalence et de fonctions de confort : filtre plissé, soufflerie, vidange, prise outil ou nettoyage de filtre selon le modèle. Sur les NT, l'écosystème devient plus technique avec flexibles conducteurs, antistatique, sacs d'élimination et surveillance du débit.",
  "Le système Tact est le marqueur le plus important côté professionnel. Sur les versions récentes, Kärcher pilote le décolmatage en fonction du besoin afin de maintenir le filtre disponible pendant l'aspiration de grandes quantités de poussières fines. La mention ACD concerne la collecte de poussières combustibles selon le cadre indiqué par le fabricant ; elle ne doit pas être interprétée comme une compatibilité universelle avec toute atmosphère explosive.",
 ],
 "strengths":["Une gamme très large, du petit nettoyage eau/poussière jusqu'aux aspirateurs de sécurité professionnels.","Des options professionnelles M et H clairement documentées.","Le système Tact, la prise asservie et l'antistatique sur les NT concernés.","Une forte disponibilité d'accessoires, consommables et pièces dans l'écosystème Kärcher."],
 "limits":["La proximité des noms WD et NT peut masquer des différences de certification beaucoup plus importantes que la puissance annoncée.","Les WD ne doivent pas être présentés comme des aspirateurs de sécurité simplement parce qu'ils aspirent fort.","Les références professionnelles deviennent lourdes et coûteuses ; le NT 50 est disproportionné pour un petit atelier domestique.","La gamme évolue : certaines anciennes variantes WD restent visibles chez des revendeurs alors qu'elles ne représentent plus le meilleur point de comparaison 2026."],
 "choose":["Vous cherchez avant tout un aspirateur eau/poussière robuste pour garage, rénovation ou gravats : regardez les WD 5 à WD 7.","Vous travaillez avec des poussières fines et avez besoin d'une classe M documentée : partez sur les NT M, puis vérifiez le risque exact.","Vous voulez une grosse cuve et un décolmatage automatique pour un chantier intensif : les NT Tact sont plus cohérents que les WD."],
 "avoid":["Évitez de choisir un WD pour une poussière exigeant une classe M ou H uniquement sur la base de son débit ou de sa dépression.","Kärcher convient moins si votre priorité est une intégration poussée avec une plateforme batterie d'outillage déjà possédée.","Pour du ponçage ultra-mobile en environnement premium, Festool ou Mirka peuvent offrir un workflow plus intégré autour de l'outil."],
 "links":[["comparatif général","/comparatifs/meilleur-aspirateur-de-chantier/"],["eau et poussière","/comparatifs/aspirateur-eau-poussiere/"],["classe M","/comparatifs/aspirateur-classe-m/"],["professionnel","/comparatifs/aspirateur-professionnel/"],["guide classes L/M/H","/guides/classes-l-m-h/"],["décolmatage automatique","/guides/decolmatage-automatique/"],["gravats","/usages/aspirateur-gravats/"],["Kärcher WD6","/modeles/karcher-wd6/"],["Kärcher NT 30/1 Tact","/modeles/karcher-nt-30-1-tact/"]],
 "sources":[
  ["Kärcher WD 7 Control — fiche officielle","https://www.kaercher.com/fr/home-garden/aspirateurs-eau-et-poussieres/wd-7-control-p-s-30-6-35-t-eu-iii-16283860.html"],
  ["Kärcher NT 30/1 Tact Te M ACD — fiche officielle","https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres/aspirateurs-de-securite/nt-30-1-tact-te-m-acd-11482350.html"],
  ["Kärcher NT 50/1 Tact Te M ACD — fiche officielle","https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres/aspirateurs-de-securite/nt-50-1-tact-te-m-acd-11484350.html"],
  ["Kärcher — gamme aspirateurs de sécurité","https://www.kaercher.com/fr/professional/aspirateurs-eau-et-poussieres/aspirateurs-de-securite.html"],
 ]
},
"bosch": {
 "name":"Bosch","title":"Bosch — Aspirateurs de chantier GAS et AdvancedVac : gamme 2026","desc":"Bosch 2026 : différence entre AdvancedVac DIY et GAS Professional, classe M, Click & Clean, 18 V, L-BOXX, modèles et usages.",
 "quick":"Chez Bosch, il faut d'abord distinguer les aspirateurs <strong>DIY</strong> verts — dont l'AdvancedVac 20 — et les aspirateurs <strong>Professional GAS</strong> bleus. Les premiers répondent au bricolage eau/poussière ; les seconds structurent l'offre chantier, avec notamment des modèles classe M, le système Click & Clean et des formats sur batterie.",
 "distinct":[
  "Bosch a une architecture de gamme plus segmentée qu'elle n'en a l'air. La gamme DIY comprend plusieurs aspirateurs eau et poussière, dont l'AdvancedVac 20, le PAS30-240PRS ou l'AdvancedVac 18V-8. La gamme Professional utilise le préfixe GAS et cible l'usage avec outils électroportatifs, le transport L-BOXX, la filtration de chantier et les besoins de classe L ou M selon la référence.",
  "Le GAS 35 M AFC et le GAS 55 M AFC illustrent le haut de cette logique : tous deux sont certifiés classe M, annoncent 74 l/s et 254 mbar à la turbine et disposent du nettoyage automatique AFC. La différence se joue notamment sur le volume : 35 L brut pour le premier, 55 L pour le second. À l'inverse, l'AdvancedVac 20 est un excellent aspirateur eau/poussière de bricolage, mais son rôle n'est pas celui d'un aspirateur de sécurité M.",
 ],
 "range":[
  ["AdvancedVac 18V-8", "CURRENT", "Bricolage mobile", "8 L, plateforme Power for All 18 V, format compact."],
  ["AdvancedVac 20", "CURRENT", "Atelier DIY eau/poussière", "20 L, 70 l/s, 260 mbar, démarrage automatique avec outil."],
  ["GAS 18V-10 L", "CURRENT", "Interventions sans fil", "Classe L, 10 L brut, plateforme Professional 18 V."],
  ["GAS 35 M AFC", "CURRENT", "Chantier classe M polyvalent", "35 L brut, 74 l/s, 254 mbar, nettoyage automatique AFC."],
  ["GAS 55 M AFC", "CURRENT", "Classe M et gros volume", "55 L brut / 43 L net, même logique AFC et Click & Clean."],
  ["GAS 35 L AFC et références L antérieures", "CURRENT_OR_LEGACY_BY_MARKET", "Classe L / parc existant", "Toujours pertinentes selon marché, mais à distinguer des besoins imposant M."],
 ],
 "ecosystem":[
  "Côté Professional, Bosch s'appuie sur Click & Clean pour raccorder l'aspiration aux outils et sur la compatibilité L-BOXX pour le transport. C'est un avantage concret si l'atelier ou le parc de chantier est déjà largement Bosch : l'aspirateur devient un élément du workflow plutôt qu'un appareil isolé. La plateforme batterie Professional 18 V renforce cette logique sur les références sans fil.",
  "Il existe toutefois deux écosystèmes Bosch distincts. Power for All 18 V concerne l'univers DIY, tandis que Professional 18 V concerne les outils bleus. Il ne faut donc pas écrire qu'un aspirateur Bosch 18 V partage automatiquement ses batteries avec n'importe quel outil Bosch. Cette distinction est importante dans le coût total d'une solution sans fil.",
 ],
 "strengths":["Une séparation utile entre bricolage et gamme Professional.","Des références classe M très documentées avec AFC.","Click & Clean et L-BOXX rendent l'ensemble cohérent pour un parc Bosch Professional.","Un choix filaire et sans fil qui couvre atelier, chantier et interventions mobiles."],
 "limits":["Deux plateformes 18 V Bosch coexistent : DIY et Professional ne sont pas un seul écosystème batterie.","L'AdvancedVac peut être très performant en nettoyage sans répondre au rôle réglementaire d'un GAS classe M.","Les GAS 35/55 M sont lourds et chers pour de simples travaux domestiques.","Les chiffres publiés à la turbine doivent être comparés avec le même point de mesure."],
 "choose":["Choisissez Bosch si vous avez déjà un parc Professional et souhaitez raccorder outils, L-BOXX et aspiration.","Le GAS 35 M AFC convient si la classe M est adaptée au risque et que vous voulez un volume encore mobile.","L'AdvancedVac 20 est à privilégier pour un atelier DIY eau/poussière sans besoin de classe M."],
 "avoid":["Évitez l'AdvancedVac pour remplacer un aspirateur de sécurité requis par votre poussière.","Bosch convient moins si votre workflow est centré sur Systainer/Festool ou sur le ponçage Mirka.","Ne choisissez pas le GAS 55 simplement parce qu'il est plus gros : son volume pénalise les déplacements fréquents."],
 "links":[["Bosch GAS 35 M AFC","/modeles/bosch-gas-35-m-afc/"],["Bosch GAS 18V-10 L","/modeles/bosch-gas-18v-10-l/"],["Bosch AdvancedVac 20","/modeles/bosch-advancedvac-20/"],["classe M","/comparatifs/aspirateur-classe-m/"],["sans fil","/comparatifs/aspirateur-chantier-sans-fil/"],["professionnel","/comparatifs/aspirateur-professionnel/"],["prise asservie","/guides/prise-asservie/"],["classes L/M/H","/guides/classes-l-m-h/"],["ponceuse","/usages/aspirateur-ponceuse/"]],
 "sources":[
  ["Bosch Professional GAS 35 M AFC","https://www.bosch-professional.com/fr/fr/products/gas-35-m-afc-06019C31W0"],
  ["Bosch Professional GAS 55 M AFC","https://www.bosch-professional.com/fr/fr/products/gas-55-m-afc-06019C33W0"],
  ["Bosch DIY AdvancedVac 20","https://www.bosch-diy.com/fr/fr/p/advancedvac-20-06033d12w0"],
  ["Bosch DIY — gamme aspirateurs eau et poussière","https://www.bosch-diy.com/fr/fr/outils-de-nettoyage/aspirateurs-eau-et-poussiere"],
 ]
},
"makita": {
 "name":"Makita","title":"Makita — Aspirateurs de chantier VC, LXT et XGT : gamme 2026","desc":"Makita 2026 : aspirateurs VC filaires et sans fil, classes L/M/H, XGT 40 V, AWS, Makpac, modèles actuels, forces et limites.",
 "quick":"Makita a l'une des gammes les plus étendues pour qui possède déjà ses outils : aspirateurs filaires VC, modèles sur batterie LXT/XGT, classes L et M selon références, compatibilité <strong>Makpac</strong> et démarrage sans fil <strong>AWS</strong> sur certaines configurations. La contrepartie est une nomenclature dense qu'il faut lire référence par référence.",
 "distinct":[
  "L'offre Makita ne se résume pas aux VC2512L et VC4210. Le fabricant conserve des modèles filaires simples, des aspirateurs à décolmatage automatique et une gamme croissante sur batterie. Les documents français listent aussi des références XGT 40 V comme les VC001G, VC002G, VC003G, VC004G, VC006G et VC007G, auxquelles s'ajoutent des modèles filaires L, M ou H.",
  "Le VC2512L reste une bonne illustration du segment accessible : classe L, eau/poussière, 25 L brut, 3,6 m³/min et 210 mbar, avec nettoyage manuel Push & Clean et prise asservie. Plus haut dans la gamme, le VC4210M est la variante classe M de la plateforme 42 L et s'accompagne d'un décolmatage automatique InfiniClean sur la génération concernée. Le suffixe commercial peut varier selon les kits : il faut vérifier la fiche exacte plutôt que déduire la classe de la seule racine VC4210.",
 ],
 "range":[
  ["VC2512L", "CURRENT", "Filaire classe L accessible", "25 L brut, 21 L poussière, 18 L liquide, Push & Clean manuel."],
  ["VC4210L / VC4210M", "CURRENT", "Grand volume filaire", "42 L brut ; variantes L ou M, décolmatage automatique sur la famille."],
  ["VC3211M / VC2211M", "CURRENT_OR_CATALOG", "Classe M filaire", "Références professionnelles présentes dans les catalogues Makita."],
  ["VC001G à VC007G", "CURRENT", "Aspiration XGT 40 V", "Famille sans fil, avec variantes L/M selon référence et configuration."],
  ["DVC / 18Vx2 LXT", "CURRENT_OR_CATALOG", "Parc batterie LXT", "Solutions mobiles pour utilisateurs déjà équipés Makita."],
  ["Anciennes références et suffixes kit X/X1", "REGION_SPECIFIC", "Parc existant", "Le suffixe peut désigner une fourniture ou une variante de marché ; vérifier la classe exacte."],
 ],
 "ecosystem":[
  "Makita est particulièrement intéressante lorsqu'on raisonne en parc d'outillage. Makpac permet d'empiler et transporter des coffrets, tandis qu'AWS peut déclencher l'aspiration sans câble de commande avec des outils compatibles. Sur les modèles batterie, le choix entre LXT 18 V, 18Vx2 et XGT 40 V pèse directement sur le coût total si l'utilisateur possède déjà batteries et chargeurs.",
  "Cet écosystème impose cependant de vérifier les compatibilités au niveau de la référence. Un aspirateur filaire peut recevoir un adaptateur AWS sans devenir pour autant un aspirateur sur batterie ; une machine XGT n'utilise pas les mêmes batteries qu'une LXT. Makita offre de nombreuses combinaisons, mais cette largeur rend les raccourcis éditoriaux dangereux.",
 ],
 "strengths":["Très grande profondeur de gamme filaire et sans fil.","Intégration Makpac et AWS intéressante avec les outils Makita.","Présence de références L, M et H dans le catalogue professionnel.","Choix pertinent pour les utilisateurs déjà investis dans LXT ou XGT."],
 "limits":["Nomenclature complexe : un suffixe peut changer la fourniture, la classe ou le marché.","La batterie LXT et la batterie XGT ne sont pas une même plateforme.","Les petits modèles Push & Clean demandent plus d'intervention qu'un vrai décolmatage automatique en poussière fine continue.","Certaines pages revendeurs continuent d'utiliser des noms abrégés qui peuvent masquer la classe exacte."],
 "choose":["Choisissez Makita si vos outils, batteries et coffrets sont déjà majoritairement Makita.","Le VC2512L convient aux besoins eau/poussière de classe L avec prise outil, sans usage intensif de poussière fine.","Une variante VC4210M ou un modèle M sans fil devient plus cohérent lorsque la classe M et l'endurance de filtre font partie du cahier des charges."],
 "avoid":["Évitez d'acheter sur la seule mention VC4210 sans vérifier L ou M et le suffixe exact.","Makita convient moins si vous ne possédez aucune batterie de la plateforme visée et cherchez uniquement le coût initial le plus bas.","Pour une intégration de ponçage très spécialisée, Mirka ou Festool peuvent offrir une chaîne outil-flexible-aspirateur plus lisible."],
 "links":[["Makita VC2512L","/modeles/makita-vc2512l/"],["Makita VC4210MX","/modeles/makita-vc4210mx/"],["sans fil","/comparatifs/aspirateur-chantier-sans-fil/"],["classe M","/comparatifs/aspirateur-classe-m/"],["professionnel","/comparatifs/aspirateur-professionnel/"],["décolmatage automatique","/guides/decolmatage-automatique/"],["prise asservie","/guides/prise-asservie/"],["atelier","/usages/aspirateur-atelier/"],["bois et sciure","/usages/aspirateur-bois-sciure-copeaux/"]],
 "sources":[
  ["Makita VC2512L — fiche produit officielle","https://www.makita.fr/data/sr/productinfo/generated/vc2512l_fiche_produit.pdf"],
  ["Makita — brochure gamme aspiration","https://www.makita.fr/data/pam/public/Content-Pages/Media/CatalogsAndBrochures/2023_leaflet_aspi_web.pdf"],
  ["Makita — références sous garantie commerciale","https://www.makita.fr/data/pam/public/Content-Pages/Media/CatalogsAndBrochures/GARANTY/21032025_-_refs_sous_garantie_%28web%29.pdf"],
 ]
},
"festool": {
 "name":"Festool","title":"Festool — Aspirateurs CTL, CTM, CTH et CTC : gamme 2026","desc":"Festool 2026 : aspirateurs CLEANTEC CTL/CTM/CTH, AUTOCLEAN, Bluetooth, Systainer, modèles filaires et sans fil, forces et limites.",
 "quick":"Festool est surtout pertinent quand l'aspirateur fait partie d'un <strong>système de travail</strong> : ponceuse, flexible CLEANTEC, Systainer, Bluetooth et application. La gamme 2026 distingue clairement les classes L, M et H via les familles CTL, CTM et CTH, avec des versions AUTOCLEAN et des solutions sans fil CTC/CTMC.",
 "distinct":[
  "La force de Festool n'est pas d'afficher la plus grande cuve ou la plus grosse puissance électrique. La marque cherche plutôt à réduire les frictions entre l'outil et l'aspirateur : tuyau antistatique lisse, raccord CLEANTEC, démarrage Bluetooth par batterie ou télécommande, fixation T-LOC/SYS-DOCK et rangement du flexible. Pour le ponçage et le montage, cette ergonomie systémique est souvent plus décisive qu'un chiffre isolé.",
  "La nomenclature donne aussi une information utile. CTL correspond à la classe L, CTM à la classe M et CTH à la classe H sur les références concernées. L'ajout AC signale AUTOCLEAN. Le CTM MIDI I AC, par exemple, combine classe M, 15 L, 3 700 l/min, 24 000 Pa, prise 2 400 W, Bluetooth et nettoyage automatique du filtre. Le CTH MIDI I AC reprend le format compact avec la catégorie H pour les usages concernés.",
 ],
 "range":[
  ["CTL MIDI I / CTL MIDI I AC", "CURRENT", "Compact classe L", "Format mobile ; version AC avec AUTOCLEAN."],
  ["CTM MIDI I / CTM MIDI I AC", "CURRENT", "Compact classe M", "15 L, Bluetooth ; AC pour poussières colmatantes et cycles de nettoyage auto."],
  ["CTH MIDI I AC", "CURRENT", "Compact classe H", "Filtration et sécurité adaptées aux poussières relevant de H selon les prescriptions."],
  ["CTM 26 EI / CTM 26 EI AC", "CURRENT", "Volume intermédiaire classe M", "Cuve plus grande, intégration système et version AUTOCLEAN."],
  ["CTC / CTMC MIDI I", "CURRENT", "Aspiration sans fil", "Deux batteries 18 V sur les configurations sans fil ; classe selon variante."],
  ["Anciennes CT MINI/MIDI générations", "PREVIOUS_GENERATION", "Occasion / parc existant", "Toujours répandues mais à distinguer de la génération I/AC actuelle."],
 ],
 "ecosystem":[
  "CLEANTEC est le cœur du raccordement : le manchon à baïonnette verrouille le flexible sur l'outil et limite les déconnexions. Le tuyau lisse est conçu pour moins accrocher les arêtes. À cela s'ajoutent Systainer/T-LOC pour le transport et Bluetooth pour le démarrage automatique avec une batterie compatible ou une télécommande. Sur les générations récentes, l'application Festool peut aussi fournir des informations d'usage ou aider au réglage.",
  "Cette intégration crée un vrai avantage si vos ponceuses, scies et coffrets sont déjà Festool. Elle peut en revanche devenir un surcoût si vous n'utilisez qu'un aspirateur de façon isolée : le prix premium rémunère autant l'écosystème que la simple capacité à aspirer. C'est pourquoi il faut comparer le workflow complet, pas uniquement le prix de la cuve."],
 "strengths":["Intégration outil-flexible-aspirateur particulièrement poussée.","Nomenclature L/M/H plus lisible que chez beaucoup de concurrents.","AUTOCLEAN disponible sur des formats compacts récents.","Bluetooth, Systainer et Festool App réduisent les manipulations dans un parc Festool."],
 "limits":["Positionnement premium et consommables/accessoires parfois coûteux.","Les cuves MIDI restent compactes : un gros volume de déchets peut justifier un modèle plus grand ou une autre marque.","L'intérêt du système diminue si vos outils et coffrets appartiennent à d'autres écosystèmes.","Il faut toujours choisir la classe selon le risque ; le logo Festool ne rend pas une version CTL équivalente à une CTM ou CTH."],
 "choose":["Choisissez Festool si votre activité tourne autour du ponçage, montage ou sciage avec des outils Festool.","Le CTM MIDI I AC est à privilégier si vous voulez classe M, AUTOCLEAN et compacité.","Une CTH est à étudier lorsque le risque et les règles applicables exigent réellement la classe H."],
 "avoid":["Évitez de payer l'écosystème si vous cherchez seulement un aspirateur eau/poussière économique pour garage.","Festool convient moins aux gros gravats et très gros volumes avec une petite cuve MIDI.","Ne choisissez pas CTL à la place de CTM/CTH lorsque la classe supérieure est requise par l'application."],
 "links":[["Festool CTL Midi","/modeles/festool-ctl-midi/"],["ponceuse","/usages/aspirateur-ponceuse/"],["classe M","/comparatifs/aspirateur-classe-m/"],["professionnel","/comparatifs/aspirateur-professionnel/"],["sans fil","/comparatifs/aspirateur-chantier-sans-fil/"],["classes L/M/H","/guides/classes-l-m-h/"],["décolmatage automatique","/guides/decolmatage-automatique/"],["prise asservie","/guides/prise-asservie/"],["Mirka","/marques/mirka/"]],
 "sources":[
  ["Festool CTM MIDI I AC","https://www.festool.fr/produits/aspirateurs/aspirateurs-compact/578552---ctm-midi-i-ac"],
  ["Festool CTH MIDI I AC","https://www.festool.fr/produits/aspirateurs/aspirateurs-pour-amiante/578558---cth-midi-i-ac"],
  ["Festool — gamme aspiration et classes de poussière","https://www.festool.fr/produits/aspirateurs"],
 ]
},
"dewalt": {
 "name":"DeWalt","title":"DeWalt — Aspirateurs et extracteurs XR FLEXVOLT : gamme 2026","desc":"DeWalt 2026 : DCV586M classe M, DCV584L hybride, XR FLEXVOLT, TSTAK, AIRLOCK, Perform & Protect, usages, forces et limites.",
 "quick":"DeWalt est surtout intéressant pour un chantier déjà équipé en <strong>XR / FLEXVOLT</strong>. La pièce maîtresse actuelle est le DCV586M, extracteur sans fil 54 V classe M compatible TSTAK. La marque complète ce système avec AIRLOCK et des solutions d'extraction directement reliées aux outils, plutôt qu'avec une immense famille d'aspirateurs traîneaux.",
 "distinct":[
  "L'offre française actuelle est plus étroite que ne le suggèrent certains anciens catalogues ou pages revendeurs. Le cœur professionnel est le DCV586M : classe M, moteur brushless, deux filtres HEPA avec nettoyage automatique, télécommande et intégration TSTAK. Il vise clairement le chantier mobile sans sacrifier la logique de contrôle des poussières.",
  "Le DCV584L occupe un rôle différent. Il peut fonctionner sur secteur ou avec des batteries XR/FLEXVOLT et aspire eau ou poussière, mais il est classe L. C'est un bon exemple de l'importance de lire la classe plutôt que la marque : sa polyvalence hybride ne le rend pas équivalent au DCV586M pour un besoin M. AIRLOCK complète l'ensemble avec une connexion rapide entre outil et aspiration."],
 "range":[
  ["DCV586M / DCV586MN", "CURRENT", "Sans fil classe M", "XR FLEXVOLT 54 V, brushless, nettoyage automatique, télécommande, TSTAK."],
  ["DCV584L", "CURRENT", "Hybride secteur/batterie classe L", "Wet & dry, XR/FLEXVOLT, compact pour chantier mobile."],
  ["DWH161 et extracteurs embarqués", "CURRENT", "Extraction à la source", "Solutions dédiées au perçage et aux outils plutôt qu'au nettoyage général."],
  ["AIRLOCK accessoires et forets aspirants", "CURRENT", "Connexion outil-aspirateur", "Raccords rapides et extraction à la source."],
  ["DWV900L / DWV901L / DWV902M", "PREVIOUS_GENERATION", "Parc filaire existant", "Encore présents dans la documentation/accessoires, mais ne structurent plus seuls la gamme actuelle."],
 ],
 "ecosystem":[
  "L'écosystème DeWalt relie trois briques. XR/FLEXVOLT fournit l'énergie sans fil, TSTAK structure le transport, et AIRLOCK standardise la connexion entre les outils et l'extracteur. Pour un artisan déjà équipé en batteries 54 V et coffrets TSTAK, le DCV586M peut donc éviter d'ajouter un second univers de batteries ou de rangement.",
  "Perform & Protect élargit la logique au contrôle des poussières à la source. DeWalt propose des forets et accessoires aspirants qui se raccordent via AIRLOCK. Cela ne dispense pas d'évaluer la poussière et la classe de l'aspirateur, mais explique pourquoi la marque est plus convaincante comme système chantier que comme simple achat d'un aspirateur isolé."],
 "strengths":["DCV586M : véritable option sans fil classe M dans l'écosystème FLEXVOLT.","AIRLOCK facilite le raccordement direct aux outils.","TSTAK simplifie le transport avec les coffrets DeWalt.","Le DCV584L offre une flexibilité secteur/batterie utile en classe L."],
 "limits":["Gamme d'aspirateurs complets moins profonde que Kärcher, Bosch ou Makita.","Le coût d'un système 54 V est élevé si vous ne possédez pas déjà les batteries FLEXVOLT.","Le DCV584L reste classe L malgré son filtre HEPA et sa polyvalence.","Les anciennes références DWV sont encore très visibles en ligne et peuvent brouiller la perception de la gamme actuelle."],
 "choose":["Choisissez DeWalt si votre parc chantier est déjà XR/FLEXVOLT et TSTAK.","Le DCV586M est à privilégier pour un besoin mobile classe M compatible avec votre analyse de risque.","Le DCV584L convient si la classe L suffit et que l'hybride secteur/batterie est plus important que la classe M."],
 "avoid":["Évitez de choisir le DCV584L comme substitut à un aspirateur M uniquement parce qu'il possède un filtre HEPA.","DeWalt convient moins si vous cherchez une grande diversité de cuves 30 à 50 L filaires.","Si vous ne possédez aucune batterie FLEXVOLT, comparez le coût complet avec Bosch, Makita ou Festool avant d'acheter."],
 "links":[["sans fil","/comparatifs/aspirateur-chantier-sans-fil/"],["classe M","/comparatifs/aspirateur-classe-m/"],["professionnel","/comparatifs/aspirateur-professionnel/"],["guide classes L/M/H","/guides/classes-l-m-h/"],["adaptateurs outils","/accessoires/adaptateur-outil-electroportatif/"],["prise asservie","/guides/prise-asservie/"],["ponceuse","/usages/aspirateur-ponceuse/"],["Bosch","/marques/bosch/"],["Makita","/marques/makita/"]],
 "sources":[
  ["DeWalt DCV586MN — fiche officielle","https://www.dewalt.fr/fr-fr/produit/dcv586mn-xj/aspirateur-tstak-xr-flexvolt-54v-brushless-eau-et-poussieres-classe-m"],
  ["DeWalt DCV584L — fiche officielle","https://www.dewalt.fr/fr-fr/produit/dcv584l-qw/aspirateur-sur-secteur-ou-batterie-xr-et-xr-flexvolt-1854v-classe-l-sans"],
  ["DeWalt Perform & Protect / AIRLOCK","https://prod.dewalt.fr/fr-fr/solutions-chantier/perform-protect"],
 ]
},
"parkside": {
 "name":"Parkside","title":"Parkside — Aspirateurs eau et poussière PWD : gamme 2026","desc":"Parkside 2026 : PWD 12, PWD 20, PWD 25 et PWD 30, prix, disponibilité Lidl, prise outil, limites face aux aspirateurs de sécurité.",
 "quick":"Parkside se positionne d'abord sur le <strong>rapport équipement/prix</strong>. En 2026, les références PWD 12, 20, 25 et 30 apparaissent sur Lidl France selon les stocks. Elles couvrent le nettoyage eau/poussière, le garage et le bricolage, mais ne doivent pas être assimilées à une gamme professionnelle de sécurité L/M/H sans certification explicite.",
 "distinct":[
  "La gamme Parkside évolue davantage par lots, générations et disponibilité que les gammes professionnelles classiques. Un PWD 30 C1 peut être disponible à un moment puis marqué épuisé, tandis qu'une autre référence ou une nouvelle révision apparaît. Pour une page marque, le statut de stock fait donc partie de l'information : il faut parler de gamme observée et non promettre une disponibilité permanente.",
  "Le PWD 30 C1 illustre le positionnement : environ 30 L brut, 1 500 W, 260 Airwatts annoncés, prise pour outil avec marche/arrêt automatique, nettoyage du filtre par bouton et accessoires nombreux. Le PWD 20 C3 descend à 19,8 L et 1 300 W. Ces chiffres sont utiles pour le bricolage, mais ils ne donnent pas une classe de poussière de sécurité."],
 "range":[
  ["PWD 12 B1", "CURRENT", "Petit nettoyage eau/poussière", "12 L brut, 1 200 W, format compact."],
  ["PWD 20 C3", "CURRENT", "Garage et bricolage polyvalent", "19,8 L, 1 300 W, 200 Airwatts annoncés."],
  ["PWD 25 C4", "CURRENT", "Rénovation domestique", "25 L, 1 400 W, 240 Airwatts annoncés."],
  ["PWD 30 C1", "CURRENT_STOCK_DEPENDENT", "Grand format DIY", "30 L brut, prise outil, nettoyage filtre par bouton, disponibilité fluctuante."],
  ["PNTS 1250 / 1300 et anciennes séries", "PREVIOUS_GENERATION", "Parc existant / consommables", "Encore citées pour la compatibilité des sacs et filtres, mais ne résument plus la gamme actuelle."],
 ],
 "ecosystem":[
  "Parkside fonctionne moins comme un écosystème fermé d'aspiration que comme une gamme d'équipement Lidl à prix serré. Les consommables et accessoires sont proposés pour plusieurs générations, avec des raccords souvent simples et des kits fournis généreux. Sur le PWD 30, la prise outil et l'adaptateur permettent une aspiration directe lors de certains travaux de sciage ou ponçage.",
  "La principale variable est la disponibilité. Les références, révisions et promotions changent plus souvent qu'un catalogue professionnel stable. Il faut donc vérifier la fiche Lidl du moment, le contenu du carton et la compatibilité des filtres avant achat. Une bonne affaire n'est bonne que si les consommables utiles restent accessibles."],
 "strengths":["Prix d'entrée très compétitif pour eau/poussière et garage.","Équipement généreux sur les PWD 20/25/30.","Prise outil et nettoyage de filtre sur certaines grandes références.","Formats de 12 à 30 L qui couvrent de nombreux besoins domestiques."],
 "limits":["Disponibilité et révisions de modèles fluctuantes chez Lidl.","Pas de raison de déduire une classe M ou H à partir de la puissance ou d'un filtre plissé.","Le décolmatage par bouton n'est pas équivalent à un système automatique Tact/AFC/InfiniClean en poussière fine continue.","Pour un usage professionnel quotidien, SAV, consommables et robustesse du workflow peuvent peser plus que le prix initial."],
 "choose":["Choisissez Parkside pour du bricolage occasionnel, un garage ou de l'eau/poussière avec budget serré.","Le PWD 20 ou 25 est souvent un meilleur compromis si vous n'avez pas besoin d'une cuve 30 L.","Le PWD 30 est à privilégier lorsque la prise outil et le volume comptent réellement et que la référence est disponible."],
 "avoid":["Évitez Parkside pour remplacer un aspirateur de sécurité M/H requis par la poussière sans certification explicite du modèle.","La marque convient moins à une utilisation intensive où le décolmatage automatique et la surveillance de débit sont critiques.","Évitez de commander des sacs ou filtres uniquement sur le nom Parkside : vérifiez la génération PWD/PNTS exacte."],
 "links":[["petit aspirateur","/comparatifs/petit-aspirateur-de-chantier/"],["eau et poussière","/comparatifs/aspirateur-eau-poussiere/"],["bricolage et rénovation","/usages/aspirateur-bricolage-renovation/"],["gravats","/usages/aspirateur-gravats/"],["classes L/M/H","/guides/classes-l-m-h/"],["prise asservie","/guides/prise-asservie/"],["sacs","/accessoires/sacs-aspirateur-chantier/"],["filtres","/accessoires/filtres-aspirateur-chantier/"],["Kärcher","/marques/karcher/"]],
 "sources":[
  ["Lidl / Parkside PWD 30 C1","https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-30-c1/p100407117"],
  ["Lidl / Parkside PWD 20 C3","https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-20-c3-19-8-l-1300-w/p100397254"],
  ["Lidl / Parkside PWD 25 C4","https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-25-c4-25-l-1400-w/p100395330"],
  ["Lidl / Parkside PWD 12 B1","https://www.lidl.fr/p/parkside-aspirateur-eau-et-poussiere-pwd-12-b1/p100406420"],
 ]
},
"nilfisk": {
 "name":"Nilfisk","title":"Nilfisk — Aspirateurs Multi, Buddy et ATTIX : gamme 2026","desc":"Nilfisk 2026 : Buddy et Multi pour eau/poussière, ATTIX professionnel, classe M, InfiniClean, FlowSensor, forces et limites.",
 "quick":"Nilfisk couvre deux besoins très différents : <strong>Buddy/Multi</strong> pour le nettoyage eau/poussière grand public et <strong>ATTIX</strong> pour l'aspiration professionnelle, avec des variantes de sécurité et le système de décolmatage InfiniClean. Cette séparation est plus utile que de chercher un unique “meilleur Nilfisk”.",
 "distinct":[
  "Les familles Buddy II et Multi II répondent aux garages, ateliers domestiques et travaux de nettoyage. Le Multi II 30 T Inox VSC, par exemple, combine une cuve 30 L et 1 400 W dans un format eau/poussière. La gamme ATTIX change de registre : cuves plus robustes, antistatique, démarrage outil, classes de poussière selon variante et maintenance automatique du filtre.",
  "Sur l'ATTIX 44-2M IC, Nilfisk documente une classe M, un filtre PTFE et le système FlowSensor. InfiniClean nettoie brièvement le filtre toutes les 15 secondes afin de maintenir l'aspiration sans arrêt manuel. C'est précisément le type de fonction qui devient décisif avec des poussières colmatantes et qui n'a pas d'équivalent direct sur un simple Multi."],
 "range":[
  ["Buddy II 12 / 18", "CURRENT", "Nettoyage occasionnel", "Petits aspirateurs eau/poussière simples et accessibles."],
  ["Multi II 22 / 30 T", "CURRENT", "Garage, atelier, eau/poussière", "Famille 22 à 30 L avec variantes Inox et prise outil selon version."],
  ["ATTIX 33 IC", "CURRENT", "Professionnel compact", "Famille pro avec InfiniClean selon variante et classes L/M."],
  ["ATTIX 44-2M IC", "CURRENT", "Classe M / poussière fine", "42 L, InfiniClean, FlowSensor, antistatique et alarme débit."],
  ["ATTIX H / variantes spécifiques", "CURRENT_BY_MARKET", "Risques supérieurs", "Choisir sur la certification exacte et les prescriptions applicables."],
 ],
 "ecosystem":[
  "Nilfisk n'est pas un fabricant d'outillage électroportatif au sens de Bosch ou Makita : son écosystème se concentre sur le nettoyage, les accessoires et la gestion des poussières. C'est un avantage si l'aspiration est le centre du besoin, moins si vous cherchez à partager batteries et coffrets avec un parc d'outils.",
  "Dans la gamme ATTIX, les éléments à regarder sont InfiniClean, le diamètre du flexible, l'antistatique, la prise outil et la surveillance du débit. Certains modèles acceptent aussi des adaptateurs de rangement ou de coffrets. Le vrai différenciateur est la maîtrise de l'aspiration professionnelle, pas l'appartenance à une plateforme d'outils."],
 "strengths":["Spécialiste historique du nettoyage avec une gamme grand public et professionnelle distincte.","InfiniClean est pertinent pour les poussières colmatantes en usage continu.","ATTIX propose des variantes classe M avec FlowSensor et antistatique.","Multi II offre une alternative eau/poussière robuste sans payer une architecture de sécurité inutile."],
 "limits":["Moins d'intégration avec une plateforme de batteries ou d'outillage qu'un Bosch, Makita ou DeWalt.","Les noms ATTIX couvrent plusieurs classes : il faut vérifier la variante complète.","Un Multi II ne remplace pas un ATTIX M lorsqu'une classe M est requise.","Les accessoires professionnels peuvent être spécifiques au système Nilfisk."],
 "choose":["Choisissez Nilfisk si l'aspiration et le nettoyage sont le centre du cahier des charges plutôt que l'écosystème d'outillage.","Le Multi II convient au garage et aux liquides ; l'ATTIX M convient mieux à la poussière fine professionnelle lorsque cette classe est adaptée.","InfiniClean est à privilégier lorsque le filtre se colmate vite et que les interruptions coûtent du temps."],
 "avoid":["Évitez un Multi grand public pour une poussière qui nécessite une certification de sécurité supérieure.","Nilfisk convient moins si votre priorité est de mutualiser batteries et coffrets avec vos outils électroportatifs.","N'achetez pas un ATTIX uniquement sur la taille de cuve : la classe et le système de filtre priment."],
 "links":[["Nilfisk Multi II 30 T","/modeles/nilfisk-multi-ii-30-t/"],["industriel","/comparatifs/aspirateur-industriel/"],["classe M","/comparatifs/aspirateur-classe-m/"],["eau et poussière","/comparatifs/aspirateur-eau-poussiere/"],["professionnel","/comparatifs/aspirateur-professionnel/"],["décolmatage automatique","/guides/decolmatage-automatique/"],["classes L/M/H","/guides/classes-l-m-h/"],["atelier","/usages/aspirateur-atelier/"],["gravats","/usages/aspirateur-gravats/"]],
 "sources":[
  ["Nilfisk Multi II 30 T Inox VSC","https://shop.nilfisk.com/fr-fr/products/multi-ii-30-t-aspirateur-eau-et-poussiere-2"],
  ["Nilfisk ATTIX 44-2M IC","https://www.nilfisk.com/fr-fr/professionnel/produits/aspirateurs-industriels/poussiere-dangereuse/monophase/attix-44-2m-ic%2B107412182/"],
  ["Nilfisk — aspirateurs professionnels","https://www.nilfisk.com/fr-fr/professionnel/produits/aspirateurs-industriels/"],
 ]
},
"mirka": {
 "name":"Mirka","title":"Mirka — Aspirateurs DEXOS pour ponçage : gamme 2026","desc":"Mirka 2026 : DEXOS 1217 M AFC et DEXOS 1230 M AFC, myMirka, ponceuses DEROS/DEOS, classe M, forces et limites.",
 "quick":"Mirka n'est pas d'abord une marque d'aspirateurs généralistes : son intérêt vient du <strong>ponçage sans poussière</strong>. La génération DEXOS 1217 M AFC et DEXOS 1230 M AFC place désormais la classe M, le nettoyage automatique du filtre, le Bluetooth et l'application myMirka au cœur de cet écosystème.",
 "distinct":[
  "Mirka raisonne de la surface à la poussière : abrasifs, ponceuses DEROS/DEOS, flexible, extracteur et contrôle connecté. C'est une approche différente d'un aspirateur conçu d'abord pour le garage ou les gravats. Elle prend tout son sens dans la carrosserie, le bois, la finition et les travaux où l'outil génère une poussière fine en continu.",
  "Le DEXOS 1217 M AFC est le format compact de 17 L. Mirka le documente comme un extracteur classe M sec/humide avec moteur brushless, AFC, rangement intégré, deux prises avec démarrage automatique et Bluetooth. Le DEXOS 1230 M AFC monte à 30 L pour le travail continu et les volumes plus élevés, tout en conservant la logique AFC et myMirka."],
 "range":[
  ["DEXOS 1217 M AFC", "CURRENT", "Ponçage mobile classe M", "17 L, moteur brushless, AFC, Bluetooth/myMirka, sec/humide."],
  ["DEXOS 1230 M AFC", "CURRENT", "Ponçage continu / gros volume", "30 L, classe M, AFC, deux prises auto, workstation disponible."],
  ["DE 1230 / 1242 et anciennes générations", "PREVIOUS_GENERATION_OR_LEGACY", "Parc existant", "Encore supportées et visibles ; DEXOS structure la nouvelle génération."],
  ["DEROS II / DEOS II / DEROS RS", "CURRENT_RELATED", "Outils de ponçage", "Ponceuses qui donnent son sens au système d'aspiration Mirka."],
  ["Workstation et télécommande DEXOS", "CURRENT_ACCESSORY", "Organisation du poste", "Accessoires dédiés au contrôle et au rangement."],
 ],
 "ecosystem":[
  "L'écosystème Mirka est particulièrement cohérent autour des ponceuses. Les abrasifs maillés, les plateaux, les flexibles et les extracteurs sont pensés ensemble pour capter la poussière à la source. Le Bluetooth relie les DEXOS à myMirka et la télécommande peut piloter l'extracteur selon le workflow. Sur le DEXOS 1230, une workstation transforme l'appareil en poste mobile pour outils et abrasifs.",
  "Ce positionnement spécialisé explique à la fois l'intérêt et la limite de la marque. Pour un atelier de finition, l'intégration peut être plus importante qu'une cuve géante. Pour des gravats, un sous-sol inondé ou un nettoyage généraliste bon marché, la valeur du système Mirka est moins évidente."],
 "strengths":["Écosystème de ponçage et extraction très cohérent.","DEXOS 1217 et 1230 sont classe M avec AFC.","Bluetooth, myMirka et télécommande facilitent le contrôle du workflow.","Le DEXOS 1230 apporte désormais un vrai volume 30 L au système."],
 "limits":["Positionnement professionnel premium, peu justifié pour du simple nettoyage de garage.","Gamme d'aspirateurs moins large que Kärcher ou Nilfisk hors ponçage.","Les anciennes références DE 1230/1242 restent visibles et peuvent être confondues avec DEXOS.","Classe M ne signifie pas adapté à toutes les poussières dangereuses : le risque doit toujours être vérifié."],
 "choose":["Choisissez Mirka si votre travail est dominé par le ponçage, la finition ou la carrosserie.","Le DEXOS 1217 est à privilégier pour la mobilité ; le 1230 si la capacité et le fonctionnement continu comptent davantage.","La marque est particulièrement logique si vous utilisez déjà DEROS/DEOS, abrasifs Mirka et myMirka."],
 "avoid":["Évitez de payer le système Mirka pour un besoin essentiellement gravats ou eau/poussière domestique.","Mirka convient moins si vous cherchez une très grande diversité de classes, de tailles et de budgets.","N'assimilez pas DEXOS M à une classe H : vérifiez le matériau et les règles applicables."],
 "links":[["ponceuse","/usages/aspirateur-ponceuse/"],["classe M","/comparatifs/aspirateur-classe-m/"],["professionnel","/comparatifs/aspirateur-professionnel/"],["décolmatage automatique","/guides/decolmatage-automatique/"],["classes L/M/H","/guides/classes-l-m-h/"],["adaptateurs outil","/accessoires/adaptateur-outil-electroportatif/"],["Festool","/marques/festool/"],["bois et sciure","/usages/aspirateur-bois-sciure-copeaux/"],["guide débit d'air","/guides/debit-air-aspirateur/"]],
 "sources":[
  ["Mirka DEXOS 1217 M AFC","https://www.mirka.com/fr-fr/produits/top-brands/extracteur-de-poussiere-mirka-dexos/"],
  ["Mirka DEXOS 1230 M AFC — fiche officielle","https://www.mirka.com/fr-fr/p/Mirka-DEXOS-1230-M-AFC-M/"],
  ["Mirka — lancement DEXOS 1230 M AFC","https://www.mirka.com/fr-fr/entreprise/actualites/mirka-dexos-1230-m-afc--concu-pour-lextraction-efficace-de-la-poussiere/"],
 ]
}
}


def lis(items):
    return "".join(f"<li>{x}</li>" for x in items)

def link_list(items):
    return ", ".join(f'<a href="{escape(url)}">{escape(label)}</a>' for label,url in items)

def range_table(items):
    rows=[]
    for name,status,role,facts in items:
        rows.append(f"<tr><td><strong>{escape(name)}</strong></td><td><code>{escape(status)}</code></td><td>{escape(role)}</td><td>{escape(facts)}</td></tr>")
    return '<div class="table-wrap"><table><thead><tr><th>Famille / modèle</th><th>Statut 2026</th><th>Rôle</th><th>À retenir</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>'

def article(slug,b):
    name=escape(b['name'])
    sources=''.join(f'<li><a href="{escape(url)}" rel="nofollow noopener">{escape(label)}</a></li>' for label,url in b['sources'])
    return f'''<!-- BRAND_CONTENT_START -->
<div class="answer-box"><p>{b['quick']}</p></div>

<h2 id="distinction">Ce qui distingue {name} sur les aspirateurs de chantier</h2>
<p>{b['distinct'][0]}</p>
<p>{b['distinct'][1]}</p>
<p>Notre lecture de la marque repose sur les gammes et documents officiels disponibles au {UPDATED}. Elle ne repose pas sur un essai physique réalisé par notre rédaction. Les performances annoncées restent celles des fabricants ; notre rôle consiste à les remettre dans le contexte d'usage et à signaler lorsqu'une fonction, une classe ou un statut de modèle change la décision.</p>

<h2 id="gamme">Gamme {name} actuelle et modèles à connaître en 2026</h2>
<p>Plutôt que d'aligner toutes les références historiques, nous retenons les familles qui aident réellement à comprendre le catalogue actuel. Le statut <code>CURRENT</code> signifie que la référence ou la famille est encore documentée dans l'offre actuelle consultée ; <code>PREVIOUS_GENERATION</code> signale un modèle surtout pertinent pour l'occasion ou le parc existant. Les mentions liées au marché rappellent qu'une variante peut différer selon le pays ou la fourniture.</p>
{range_table(b['range'])}
<p>Ce tableau sert à orienter la recherche, pas à remplacer la fiche technique exacte. Une même famille peut exister avec plusieurs volumes, classes de poussière, prises, batteries ou kits. Avant l'achat, vérifiez toujours la référence complète et, pour une poussière potentiellement dangereuse, la classe d'aspirateur requise.</p>

<h2 id="ecosysteme">Comment fonctionne l'écosystème {name}</h2>
<p>{b['ecosystem'][0]}</p>
<p>{b['ecosystem'][1]}</p>
<p>Pour comparer ce système à d'autres marques, il faut donc regarder le coût total de la solution : aspirateur, sacs, filtres, flexible, raccords, batteries éventuelles, coffrets et accessoires. Un produit nu moins cher peut revenir plus cher s'il impose une nouvelle plateforme ou des consommables difficiles à trouver.</p>

<h2 id="forces">Les forces de {name}</h2>
<ul>{lis(b['strengths'])}</ul>
<p>Ces points forts n'ont pas tous le même poids selon l'usage. Pour une <a href="/usages/aspirateur-ponceuse/">ponceuse</a>, le raccord, le démarrage automatique et le maintien du débit peuvent passer avant la capacité de cuve. Pour des <a href="/usages/aspirateur-gravats/">gravats</a>, robustesse, diamètre du flexible et volume deviennent plus importants. Le bon produit est celui dont les avantages correspondent au travail réel.</p>

<h2 id="limites">Limites et points de vigilance</h2>
<ul>{lis(b['limits'])}</ul>
<p>Un autre point mérite d'être répété : filtre HEPA, puissance électrique, Airwatts, débit et classe de poussière ne sont pas synonymes. Consultez notre <a href="/guides/classes-l-m-h/">guide des classes L, M et H</a> et notre explication du <a href="/guides/debit-air-aspirateur/">débit d'air</a> avant de transformer un chiffre marketing en critère de sécurité.</p>

<h2 id="choisir">Pour qui choisir {name} ?</h2>
<ul>{lis(b['choose'])}</ul>
<p>Si vous hésitez entre plusieurs familles, partez du job-to-be-done : liquide et déchets mixtes, aspiration à la source avec outil, poussière fine continue, mobilité sur batterie ou gros volume. Cette méthode évite de payer une fonctionnalité inutile ou, inversement, d'économiser sur un élément qui conditionne la sécurité et l'endurance.</p>

<h2 id="eviter">Quand éviter {name} ou regarder une autre marque ?</h2>
<ul>{lis(b['avoid'])}</ul>
<p>« À éviter » ne signifie pas que la marque est mauvaise. Cela signifie que son avantage principal ne correspond pas forcément au besoin. Les marques de ce marché se différencient beaucoup par leur écosystème : certains fabricants excellent en eau/poussière, d'autres en ponçage, en outils sur batterie ou en aspiration professionnelle certifiée.</p>

<h2 id="alternatives">Alternatives, comparatifs et guides utiles</h2>
<p>Pour aller plus loin : {link_list(b['links'])}.</p>
<p>Nos pages comparatives utilisent des critères définis avant le classement et séparent les faits fabricants de l'interprétation éditoriale. Commencez par le <a href="/comparatifs/meilleur-aspirateur-de-chantier/">comparatif général</a> si votre besoin est encore flou, ou par le <a href="/comparatifs/aspirateur-classe-m/">comparatif classe M</a> si la filtration professionnelle est déjà un critère central.</p>

<h2 id="sources">Sources consultées</h2>
<p>Nous privilégions les pages fabricants et catalogues officiels pour le statut des modèles, les classes et les caractéristiques. Sources principales de cette mise à jour :</p>
<ul>{sources}</ul>
<p><small>Mise à jour : {UPDATED}. Page réalisée par recherche documentaire, sans prétention de test physique. Les liens affiliés éventuels n'influencent ni le statut des modèles, ni les forces et limites présentées.</small></p>
<!-- BRAND_CONTENT_END -->'''

def data_record(slug,b):
    return {
      "slug":slug,"brand":b['name'],"page_type":"BRAND_HUB","updated_at":"2026-09-08",
      "entity_map":{"brand":b['name'],"products":[r[0] for r in b['range']],"use_cases":[x[0] for x in b['links'] if x[1].startswith('/usages/')],"technologies":[],"competitors":["Kärcher","Bosch","Makita","Festool","DeWalt","Parkside","Nilfisk","Mirka"]},
      "brand_positioning":{"summary":re.sub('<[^>]+>','',b['quick']),"strengths":b['strengths'],"limitations":b['limits']},
      "product_range":[{"name":n,"status":s,"role":r,"evidence":f} for n,s,r,f in b['range']],
      "ecosystem":{"summary":b['ecosystem'],"choose":b['choose'],"avoid":b['avoid']},
      "evidence":[{"claim":label,"status":"VERIFIED","source":url,"source_type":"primary"} for label,url in b['sources']],
      "internal_links":[{"label":l,"url":u} for l,u in b['links']],
      "editorial":{"desk_research_only":True,"affiliate_influence":False,"human_validation_required":True}
    }

def replace_between(html, start, end, replacement):
    if start in html and end in html:
        return re.sub(re.escape(start)+r'.*?'+re.escape(end), replacement, html, flags=re.S)
    return html

def build_page(path,slug,b):
    html=path.read_text(encoding='utf-8')
    body=article(slug,b)
    if '<!-- BRAND_CONTENT_START -->' in html:
        html=replace_between(html,'<!-- BRAND_CONTENT_START -->','<!-- BRAND_CONTENT_END -->',body)
    elif '<!-- Contenu à rédiger -->' in html:
        html=html.replace('<!-- Contenu à rédiger -->',body)
    else:
        raise RuntimeError(f'No brand insertion marker in {path}')
    html=re.sub(r'<title>.*?</title>',f"<title>{escape(b['title'])}</title>",html,count=1,flags=re.S)
    html=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{escape(b["desc"], quote=True)}">',html,count=1)
    html=re.sub(r'<h1 style="margin-top:10px;">.*?</h1>',f'<h1 style="margin-top:10px;">{escape(b["title"])}</h1>',html,count=1,flags=re.S)
    html=re.sub(r'<p class="lead">.*?</p>',f'<p class="lead">{escape(b["desc"])}</p>',html,count=1,flags=re.S)
    html=html.replace('Vérifié : MM/AAAA',f'Verifié : {UPDATED}')
    toc=''.join(f'<a href="#{a}">{escape(l)}</a>' for a,l in [('distinction','Positionnement'),('gamme','Gamme 2026'),('ecosysteme','Écosystème'),('forces','Forces'),('limites','Limites'),('choisir','Pour qui ?'),('eviter','À éviter'),('sources','Sources')])
    html=html.replace('<!-- TOC générée -->',toc)
    return '\n'.join(line.rstrip() for line in html.splitlines())+'\n'

def main():
    out=BASE/'.content'/'brands'; out.mkdir(parents=True,exist_ok=True)
    for slug,b in BRANDS.items():
        p=BASE/'marques'/slug/'index.html'
        p.write_text(build_page(p,slug,b),encoding='utf-8')
        # JSON is valid YAML 1.2 and keeps the file dependency-free and machine-auditable.
        (out/f'{slug}.yaml').write_text(json.dumps(data_record(slug,b),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(f'✓ {slug}')
    print(f'Generated {len(BRANDS)} brand hubs and brand data files.')

if __name__=='__main__':
    main()
