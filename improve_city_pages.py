#!/usr/bin/env python3
"""
Script pour améliorer les pages de villes:
1. Rendre le H2 simulateur plus neutre
2. Corriger le lien simulateur.html vers /
3. Corriger les liens province cassés (prix-m2-antwerpen./ -> ../prix-m2-anvers/)
4. Ajouter liens internes vers hub et province
5. Rendre le texte plus neutre (pas de promesse d'estimation)
"""

import os
import re
import glob

SITE_DIR = "/Users/marc/Desktop/estimation-maison"

# Mapping des noms de provinces
PROVINCE_FIXES = {
    'prix-m2-antwerpen./': '../prix-m2-anvers/',
    'prix-m2-antwerpen.': '../prix-m2-anvers/',
    'prix-m2-brabant-flamand./': '../prix-m2-brabant-flamand/',
    'prix-m2-brabant-wallon./': '../prix-m2-brabant-wallon/',
    'prix-m2-bruxelles./': '../prix-m2-bruxelles/',
    'prix-m2-flandre-occidentale./': '../prix-m2-flandre-occidentale/',
    'prix-m2-flandre-orientale./': '../prix-m2-flandre-orientale/',
    'prix-m2-hainaut./': '../prix-m2-hainaut/',
    'prix-m2-liege./': '../prix-m2-liege/',
    'prix-m2-limbourg./': '../prix-m2-limbourg/',
    'prix-m2-luxembourg./': '../prix-m2-luxembourg/',
    'prix-m2-namur./': '../prix-m2-namur/',
}

def improve_city_page(filepath):
    """Améliore une page de ville"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # 1. Rendre le H2 simulateur plus neutre
        content = content.replace(
            '<h2>Estimez le prix de votre bien grâce à notre simulateur</h2>',
            '<h2>Utiliser un outil pour affiner votre réflexion</h2>'
        )
        
        # 2. Rendre le texte du simulateur plus neutre
        content = re.sub(
            r'Utilisez notre simulateur pour obtenir une estimation précise de votre bien immobilier[^<]*\.',
            'Utilisez les informations de prix au m² ci-dessus comme point de départ pour évaluer votre bien. Ces données constituent une indication basée sur le marché local, mais ne remplacent pas une estimation officielle par un professionnel.',
            content
        )
        
        # 3. Corriger le lien simulateur.html
        content = content.replace('href="../simulateur.html"', 'href="/"')
        content = content.replace("href='../simulateur.html'", "href='/'")
        
        # 4. Rendre le CTA plus neutre
        content = content.replace(
            'ESTIMEZ LE PRIX DE VOTRE MAISON OU APPARTEMENT',
            'CONSULTER LES PRIX PAR PROVINCE'
        )
        
        # 5. Corriger les liens province cassés
        for old, new in PROVINCE_FIXES.items():
            content = content.replace(f'href="{old}"', f'href="{new}"')
            content = content.replace(f"href='{old}'", f"href='{new}'")
        
        # 6. Corriger les doubles points dans les noms de province
        content = re.sub(r'province de ([A-Za-zé]+)\.\.', r'province de \1.', content)
        content = re.sub(r'province d&rsquo;([A-Za-zé]+)\.\.', r"province d'\\1.", content)
        
        # 7. Ajouter lien vers hub après la section communes voisines (si pas déjà présent)
        if 'Voir les prix dans d\'autres villes' not in content and 'autres villes de Belgique' not in content:
            # Trouver la fin de la section communes voisines
            pattern = r'(</ul>\s*</div>\s*<div style="display: flex; align-items: center;)'
            replacement = r'''</ul>
<p style="margin-top: 20px; text-align: center;"><a href="../estimation-par-ville/" style="color: #28a745;">→ Voir les prix dans d'autres villes de Belgique</a></p>
</div>
<div style="display: flex; align-items: center;'''
            content = re.sub(pattern, replacement, content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Erreur {filepath}: {e}")
        return False

def main():
    print("🔧 Amélioration des pages de villes...")
    
    # Trouve toutes les pages de villes
    city_pages = glob.glob(os.path.join(SITE_DIR, "prix-m2-a-*/index.html"))
    
    print(f"   {len(city_pages)} pages de villes à traiter\n")
    
    fixed = 0
    for filepath in city_pages:
        if improve_city_page(filepath):
            fixed += 1
    
    print(f"\n✅ {fixed} pages améliorées")

if __name__ == "__main__":
    main()
