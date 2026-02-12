#!/usr/bin/env python3
"""
Script pour corriger TOUS les liens internes du site estimation-maison.be
"""

import os
import re
import glob

SITE_DIR = "/Users/marc/Desktop/estimation-maison"

# Mapping complet des pages ?p=XXX vers les vrais chemins
PAGE_MAPPING = {
    'index.html%3Fp=15.html': 'estimation-maison/index.html',
    'index.html%3Fp=27.html': 'estimation-appartement/index.html', 
    'index.html%3Fp=30.html': 'estimation-bien-immobilier/index.html',
    'index.html%3Fp=139.html': 'a-propos/index.html',
    'index.html%3Fp=1516.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2805.html': 'estimation-par-ville/index.html',
    'index.html%3Fp=2845.html': 'mentions-legales/index.html',
    'index.html%3Fp=2860.html': 'politique-de-confidentialite/index.html',
    'index.html%3Fp=3.html': 'index.html',
    # Provinces
    'index.html%3Fp=2741.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2739.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2757.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2751.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2759.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2743.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2753.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2749.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2755.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2747.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2745.html': 'prix-m2-par-province/index.html',
}

def fix_links_in_file(filepath):
    """Corrige les liens dans un fichier HTML"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Calcule la profondeur du fichier pour les chemins relatifs
        rel_path = os.path.relpath(filepath, SITE_DIR)
        depth = rel_path.count(os.sep)
        prefix = "../" * depth if depth > 0 else ""
        
        # Remplace les liens mappés (avec et sans ../)
        for old, new in PAGE_MAPPING.items():
            # Version avec ../
            content = content.replace(f'href="../{old}"', f'href="{prefix}{new}"')
            # Version sans ../
            content = content.replace(f'href="{old}"', f'href="{prefix}{new}"')
        
        # Corrige les liens vers les pages de provinces
        province_mapping = {
            'prix-m2-brabant-flamand.html': 'prix-m2-brabant-flamand/index.html',
            'prix-m2-brabant-wallon.html': 'prix-m2-brabant-wallon/index.html', 
            'prix-m2-bruxelles.html': 'prix-m2-bruxelles/index.html',
            'prix-m2-flandre-occidentale.html': 'prix-m2-flandre-occidentale/index.html',
            'prix-m2-flandre-orientale.html': 'prix-m2-flandre-orientale/index.html',
            'prix-m2-hainaut.html': 'prix-m2-hainaut/index.html',
            'prix-m2-limbourg.html': 'prix-m2-limbourg/index.html',
            'prix-m2-liege.html': 'prix-m2-liege/index.html',
            'prix-m2-luxembourg.html': 'prix-m2-luxembourg/index.html',
            'prix-m2-namur.html': 'prix-m2-namur/index.html',
            'prix-m2-anvers.html': 'prix-m2-anvers/index.html',
        }
        for old_page, new_page in province_mapping.items():
            content = content.replace(f'href="../{old_page}"', f'href="{prefix}{new_page}"')
            content = content.replace(f'href="{old_page}"', f'href="{prefix}{new_page}"')
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Erreur {filepath}: {e}")
        return False

def main():
    # Trouve tous les fichiers HTML
    html_files = glob.glob(os.path.join(SITE_DIR, "**/*.html"), recursive=True)
    
    print(f"Correction de {len(html_files)} fichiers HTML...")
    
    fixed = 0
    for filepath in html_files:
        if fix_links_in_file(filepath):
            fixed += 1
            print(f"  ✅ {os.path.relpath(filepath, SITE_DIR)}")
    
    print(f"\n✅ {fixed} fichiers corrigés")

if __name__ == "__main__":
    main()
