#!/usr/bin/env python3
"""80/20 methodology pilot for /guides/classes-l-m-h/.

Runs after the normal guide generators. It deliberately performs a LIGHT_UPDATE:
retain the useful article, strengthen the decision layer, refresh evidence and
keep the site-specific safety language without turning the page into a new template.
"""
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent
PATH = BASE / "guides" / "classes-l-m-h" / "index.html"
VERIFIED = "09/09/2026"

TITLE = "Classes L, M et H : quelle classe d’aspirateur choisir ?"
DESC = "Classes L, M et H des aspirateurs de chantier : seuils de séparation, différence avec HEPA, exemples de poussières et critères de choix."
ANSWER = (
    "Les classes L, M et H concernent <strong>l’aspirateur complet</strong>, pas seulement son filtre. "
    "L est le niveau le moins contraignant des trois, M ajoute des exigences pour des poussières plus préoccupantes, "
    "et H vise les poussières hautement dangereuses. Le nom du matériau ne suffit toutefois pas à choisir une classe : "
    "l’évaluation du risque, la valeur limite applicable, le procédé et les prescriptions nationales restent prioritaires."
)

BODY = r'''<!-- GUIDE_CONTENT_START -->
<h2 id="norme">Ce que signifient réellement les classes L, M et H</h2>
<p>Les classes L, M et H sont utilisées pour les extracteurs de poussières commerciaux couverts par EN/IEC 60335-2-69. Elles décrivent des exigences qui concernent l’appareil dans son ensemble et sa capacité à gérer certaines poussières dangereuses. Il ne s’agit donc pas d’un simple niveau de finesse du filtre : l’étanchéité du système, le dispositif de collecte, le contrôle du débit et les modalités de vidage peuvent aussi entrer en jeu selon la classe et la conception de la machine.</p>
<p>Les degrés de séparation couramment repris par les fabricants sont supérieurs à 99 % pour L, 99,9 % pour M et 99,995 % pour H. Ces valeurs donnent une échelle utile, mais ne constituent pas à elles seules une règle de sélection. Les valeurs limites d’exposition et les prescriptions nationales restent déterminantes, surtout en environnement professionnel.</p>

<h2 id="lecture-rapide">L, M ou H : le repère rapide avant d’aller plus loin</h2>
<p>Le tableau ci-dessous résume la logique des trois classes sans transformer des exemples de matériaux en règle automatique. Il faut surtout retenir que la classe de l’appareil et la dangerosité réelle de la poussière sont deux informations liées, mais différentes.</p>
<div class="table-wrap"><table><thead><tr><th>Classe</th><th>Degré de séparation du système de filtre</th><th>Exemples couramment cités par les fabricants</th><th>À vérifier avant de choisir</th></tr></thead><tbody>
<tr><td><strong>L</strong></td><td>&gt; 99 %</td><td>Poussières à risque plus faible dans le cadre prévu par le fabricant.</td><td>Que la poussière et l’usage restent bien compatibles avec cette classe.</td></tr>
<tr><td><strong>M</strong></td><td>&gt; 99,9 %</td><td>De nombreuses poussières de bois, d’enduit, de plâtre, ciment ou béton sont citées dans les documentations fabricants.</td><td>Composition du matériau, VLEP, présence éventuelle de silice et prescriptions applicables.</td></tr>
<tr><td><strong>H</strong></td><td>&gt; 99,995 %</td><td>Poussières hautement dangereuses, cancérigènes ou pathogènes selon le risque considéré.</td><td>Exigences spécifiques de confinement, filtre, collecte, maintenance et vidage.</td></tr>
</tbody></table></div>
<p>La conséquence pratique est simple : ne montez pas ou ne descendez pas de classe uniquement parce qu’un matériau apparaît dans une liste générique. Pour un professionnel, l’évaluation des risques, la fiche de données de sécurité lorsqu’elle existe, la VLEP et les règles applicables au procédé doivent guider la décision.</p>

<h2 id="materiaux">Plâtre, bois, béton, silice : pourquoi le nom du matériau ne suffit pas</h2>
<p>Le ponçage du plâtre produit des poussières fines qui colmatent rapidement un filtre ; le bois génère poussières et copeaux, avec des risques qui varient selon les essences et procédés ; le béton ou la pierre peuvent exposer à de la silice cristalline. L’INRS recommande, pour les opérations exposant à la silice, de privilégier le captage à la source et de raccorder les outils aspirants à des systèmes d’aspiration à haute dépression.</p>
<p>Une classe de poussières ne remplace donc pas une stratégie de captage. Si vous travaillez surtout le plâtre, consultez aussi notre guide <a href="/usages/aspirateur-platre/">aspirateur pour plâtre</a>. Pour le bois, la page <a href="/usages/aspirateur-bois-sciure-copeaux/">bois, sciure et copeaux</a> traite du débit et des raccordements. Pour une sélection commerciale ciblée, notre <a href="/comparatifs/aspirateur-classe-m/">comparatif des aspirateurs classe M</a> regroupe les modèles de cette catégorie, sans se substituer à l’évaluation du risque.</p>

<h2 id="hepa">Classe H et filtre HEPA : deux classifications différentes</h2>
<p>HEPA décrit la performance d’un filtre selon une norme de filtration comme EN 1822 ; H13 et H14 sont des classes de filtres mesurées à la taille de particule la plus pénétrante. La classe H d’un aspirateur relève, elle, de la norme de l’appareil complet. Un aspirateur vendu avec un filtre HEPA n’est donc pas automatiquement un aspirateur de classe H.</p>
<p>Cette distinction est particulièrement importante pour l’amiante. L’INRS indique qu’un aspirateur utilisé sur des matériaux ou produits contenant de l’amiante doit être de classe H selon IEC 60335-2-69 et muni de filtres à très haute efficacité, au minimum H13 ou H14 selon NF EN 1822-1, avec d’autres dispositions concernant notamment le préfiltre, le filtre secondaire et la fermeture de l’orifice. Notre guide <a href="/guides/filtre-hepa-aspirateur/">HEPA H13/H14</a> détaille ce que le marquage du filtre dit — et ce qu’il ne dit pas — sur l’appareil.</p>

<h2 id="debit-classe-h">Classe H, colmatage et débit : ne pas sacrifier la filtration pour gagner en confort</h2>
<p>Une communication scientifique de l’INRS publiée en 2026 apporte une nuance utile. Sur deux modèles filaires comparés chacun en versions M et H, les variantes H se sont colmatées plus rapidement avec la poussière d’essai. L’un des deux appareils H a néanmoins conservé un débit de captage correct. Les mesures ont aussi montré une meilleure efficacité de filtration des versions H et moins de relargage de particules pendant le décolmatage.</p>
<p>Cette étude porte sur un nombre limité d’appareils et ne permet pas de généraliser le comportement à toute la classe H. Elle rappelle surtout qu’un débit plus stable ne justifie pas de choisir une classe inférieure à celle requise par le risque. Lorsque le colmatage devient un problème, il faut comparer la conception du filtre, le <a href="/guides/decolmatage-automatique/">système de décolmatage</a> et le débit réellement maintenu, tout en conservant la classe adaptée.</p>

<h2 id="choix">Comment choisir la bonne classe sans surdimensionner</h2>
<p>Pour une collecte de saletés non dangereuses, une classe supérieure n’est pas automatiquement nécessaire. À l’inverse, choisir une classe trop faible pour une poussière réglementée n’est pas compensé par une forte puissance moteur. Le bon choix se fait en reliant la poussière, sa dangerosité, la valeur limite applicable, le mode de captage et la façon dont l’appareil gère le filtre et les déchets collectés.</p>
<p>Une fois la classe déterminée, comparez la <a href="/guides/debit-air-aspirateur/">capacité de débit</a>, le <a href="/guides/decolmatage-automatique/">décolmatage</a>, la <a href="/guides/prise-asservie/">prise asservie</a>, le raccordement à l’outil et le coût des consommables. Cette séquence évite de mettre sur le même plan des machines qui ne répondent pas au même besoin de prévention.</p>

<h2 id="entretien">La classe ne vaut que si le vidage et la maintenance restent maîtrisés</h2>
<p>Une machine correctement classée peut perdre une partie de son intérêt si le filtre est endommagé, si les joints fuient ou si le vidage remet la poussière dans l’air. Les sacs de collecte, obturateurs, systèmes de fermeture et procédures de maintenance ne sont donc pas des détails. Pour certaines poussières dangereuses, la maintenance elle-même doit être réalisée avec des précautions spécifiques.</p>
<p>Respectez la notice du fabricant, remplacez les consommables par des références compatibles et évitez les opérations qui dispersent la poussière, comme souffler un filtre contaminé à l’air comprimé lorsque cette pratique n’est pas explicitement prévue. Pour les règles d’entretien courant, consultez notre <a href="/guides/entretien-aspirateur-chantier/">guide d’entretien</a> et notre page <a href="/guides/sac-ou-sans-sac/">sac ou sans sac</a>.</p>

<h2 id="sources">Sources et références</h2>
<p>Les données normatives et techniques ci-dessus ont été recoupées avec les sources suivantes. Les exigences de prévention peuvent dépendre du matériau, du procédé et de la réglementation applicable à votre situation : en contexte professionnel, la fiche de données de sécurité, l’évaluation des risques et la notice de l’appareil priment sur un guide généraliste.</p>
<ul>
<li><a href="https://webstore.iec.ch/en/publication/64777" target="_blank" rel="noopener noreferrer">IEC 60335-2-69:2021 — exigences applicables aux aspirateurs commerciaux et poussières dangereuses</a></li>
<li><a href="https://www.festool.fr/campagnes/microsites/aspiration" target="_blank" rel="noopener noreferrer">Festool — synthèse des classes L, M et H et degrés de séparation</a></li>
<li><a href="https://www.inrs.fr/risques/amiante/prevention-risque-amiante.html" target="_blank" rel="noopener noreferrer">INRS — prévention du risque amiante et cahier des charges des aspirateurs</a></li>
<li><a href="https://www.inrs.fr/risques/silice-cristalline/ce-qu-il-faut-retenir.html" target="_blank" rel="noopener noreferrer">INRS — prévention des expositions à la silice cristalline</a></li>
<li><a href="https://www.inrs.fr/inrs/recherche/etudes-publications-communications/doc/communication.html?refINRS=NOETUDE%2FC2026-013" target="_blank" rel="noopener noreferrer">INRS 2026 — évolution des performances d’aspirateurs de chantier M et H en cours d’utilisation</a></li>
</ul>
<!-- GUIDE_CONTENT_END -->'''

TOC = '''<!-- GUIDE_TOC_START -->
<a href="#norme">Ce que signifient L, M et H</a>
<a href="#lecture-rapide">L, M ou H : repère rapide</a>
<a href="#materiaux">Matériaux et cas d’usage</a>
<a href="#hepa">Classe H et HEPA</a>
<a href="#debit-classe-h">Classe H, colmatage et débit</a>
<a href="#choix">Comment choisir</a>
<a href="#entretien">Vidage et maintenance</a>
<a href="#sources">Sources</a>
<!-- GUIDE_TOC_END -->'''


def replace_between(html: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pattern.search(html):
        raise RuntimeError(f"markers missing: {start} / {end}")
    return pattern.sub(replacement, html, count=1)


def main() -> None:
    html = PATH.read_text(encoding="utf-8")
    html = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", html, count=1, flags=re.S)
    html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{DESC}">', html, count=1)
    html = re.sub(r'<h1 style="margin-top:10px;">.*?</h1>', f'<h1 style="margin-top:10px;">{TITLE}</h1>', html, count=1, flags=re.S)
    html = re.sub(r'<p class="lead">.*?</p>', f'<p class="lead">{DESC}</p>', html, count=1, flags=re.S)
    html = re.sub(
        r'<div class="answer-box"><div class="article-answer"><p>.*?</p></div></div>',
        f'<div class="answer-box"><div class="article-answer"><p>{ANSWER}</p></div></div>',
        html,
        count=1,
        flags=re.S,
    )
    html = replace_between(html, '<!-- GUIDE_CONTENT_START -->', '<!-- GUIDE_CONTENT_END -->', BODY)
    html = replace_between(html, '<!-- GUIDE_TOC_START -->', '<!-- GUIDE_TOC_END -->', TOC)
    html = re.sub(r'<span class="meta-tag">Vérifié : .*?</span>', f'<span class="meta-tag">Vérifié : {VERIFIED}</span>', html, count=1)
    PATH.write_text('\n'.join(line.rstrip() for line in html.splitlines()) + '\n', encoding="utf-8")
    print("✓ classes-l-m-h LIGHT_UPDATE pilot applied")


if __name__ == "__main__":
    main()
