#!/usr/bin/env python3
"""
Script pour corriger les liens internes du site estimation-maison.be
Remplace les liens cassés par des liens fonctionnels
"""

import os
import re
import glob

SITE_DIR = "/Users/marc/Desktop/estimation-maison"

# Mapping des pages principales
PAGE_MAPPING = {
    'index.html%3Fp=15.html': 'estimation-maison/index.html',
    'index.html%3Fp=27.html': 'estimation-appartement/index.html', 
    'index.html%3Fp=30.html': 'estimation-bien-immobilier/index.html',
    'index.html%3Fp=139.html': 'a-propos/index.html',
    'index.html%3Fp=1516.html': 'prix-m2-par-province/index.html',
    'index.html%3Fp=2805.html': 'estimation-par-ville/index.html',
    'index.html%3Fp=2845.html': 'mentions-legales/index.html',
    'index.html%3Fp=2860.html': 'politique-de-confidentialite/index.html',
    'index.html%3Fp=3.html': 'page-d-exemple/index.html',
}

def build_page_mapping():
    """Construit un mapping complet des pages ?p=XXX vers les vrais chemins"""
    mapping = PAGE_MAPPING.copy()
    
    # Cherche tous les fichiers index.html?p=XXX.html et les mappe
    for f in glob.glob(os.path.join(SITE_DIR, "index.html%3Fp=*.html")):
        basename = os.path.basename(f)
        # On ne peut pas facilement déterminer la destination, on les supprime
        pass
    
    return mapping

def fix_links_in_file(filepath, mapping):
    """Corrige les liens dans un fichier HTML"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Remplace les liens mappés
        for old, new in mapping.items():
            content = content.replace(f'href="{old}"', f'href="{new}"')
            content = content.replace(f"href='{old}'", f"href='{new}'")
        
        # Supprime les liens vers wp-json, feed, comments, xmlrpc
        content = re.sub(r'<link[^>]*href="[^"]*wp-json[^"]*"[^>]*/?>', '', content)
        content = re.sub(r'<link[^>]*href="[^"]*feed/[^"]*"[^>]*/?>', '', content)
        content = re.sub(r'<link[^>]*href="[^"]*comments/[^"]*"[^>]*/?>', '', content)
        content = re.sub(r'<link[^>]*href="[^"]*xmlrpc[^"]*"[^>]*/?>', '', content)
        
        # Remplace les URLs absolues par des relatives
        content = content.replace('https://estimation-maison.be/', '')
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Erreur {filepath}: {e}")
        return False

def main():
    mapping = build_page_mapping()
    
    # Trouve tous les fichiers HTML
    html_files = glob.glob(os.path.join(SITE_DIR, "**/*.html"), recursive=True)
    
    print(f"Correction de {len(html_files)} fichiers HTML...")
    
    fixed = 0
    for filepath in html_files:
        if fix_links_in_file(filepath, mapping):
            fixed += 1
    
    print(f"✅ {fixed} fichiers corrigés")
    
    # Supprime les fichiers inutiles
    print("\nSuppression des fichiers inutiles...")
    for pattern in ["index.html%3Fp=*.html", "xmlrpc.php*", "simulateur.html"]:
        for f in glob.glob(os.path.join(SITE_DIR, pattern)):
            try:
                os.remove(f)
                print(f"  Supprimé: {os.path.basename(f)}")
            except:
                pass

if __name__ == "__main__":
    main()
