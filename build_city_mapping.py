#!/usr/bin/env python3
"""
Script pour construire le mapping des IDs WordPress vers les URLs des pages de villes
et corriger tous les liens dans le site.
"""

import os
import re
import glob

SITE_DIR = "/Users/marc/Desktop/estimation-maison"

def extract_wp_id_from_page(filepath):
    """Extrait l'ID WordPress d'une page depuis son contenu"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Cherche le pattern ?p=XXX dans le canonical ou autres liens
        match = re.search(r'\?p=(\d+)', content)
        if match:
            return match.group(1)
        
        # Cherche dans wp-json/wp/v2/pages/XXX
        match = re.search(r'wp/v2/pages/(\d+)', content)
        if match:
            return match.group(1)
            
        return None
    except:
        return None

def build_mapping():
    """Construit le mapping complet ID -> URL"""
    mapping = {}
    
    # Parcourt toutes les pages prix-m2-a-*
    for folder in glob.glob(os.path.join(SITE_DIR, "prix-m2-a-*")):
        if os.path.isdir(folder):
            index_file = os.path.join(folder, "index.html")
            if os.path.exists(index_file):
                wp_id = extract_wp_id_from_page(index_file)
                if wp_id:
                    folder_name = os.path.basename(folder)
                    mapping[wp_id] = f"{folder_name}/index.html"
    
    # Ajoute les pages principales
    main_pages = {
        'estimation-maison': 'estimation-maison/index.html',
        'estimation-appartement': 'estimation-appartement/index.html',
        'estimation-bien-immobilier': 'estimation-bien-immobilier/index.html',
        'estimation-par-ville': 'estimation-par-ville/index.html',
        'prix-m2-par-province': 'prix-m2-par-province/index.html',
        'a-propos': 'a-propos/index.html',
        'mentions-legales': 'mentions-legales/index.html',
        'politique-de-confidentialite': 'politique-de-confidentialite/index.html',
    }
    
    for folder, url in main_pages.items():
        index_file = os.path.join(SITE_DIR, folder, "index.html")
        if os.path.exists(index_file):
            wp_id = extract_wp_id_from_page(index_file)
            if wp_id:
                mapping[wp_id] = url
    
    return mapping

def fix_links_with_mapping(mapping):
    """Corrige tous les liens dans tous les fichiers HTML"""
    html_files = glob.glob(os.path.join(SITE_DIR, "**/*.html"), recursive=True)
    
    fixed_count = 0
    
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            # Calcule le préfixe relatif
            rel_path = os.path.relpath(filepath, SITE_DIR)
            depth = rel_path.count(os.sep)
            prefix = "../" * depth if depth > 0 else ""
            
            # Remplace tous les liens index.html%3Fp=XXX.html
            for wp_id, url in mapping.items():
                old_patterns = [
                    f'href="../index.html%3Fp={wp_id}.html"',
                    f"href='../index.html%3Fp={wp_id}.html'",
                    f'href="index.html%3Fp={wp_id}.html"',
                    f"href='index.html%3Fp={wp_id}.html'",
                ]
                for old in old_patterns:
                    if old in content:
                        content = content.replace(old, f'href="{prefix}{url}"')
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed_count += 1
                print(f"  ✅ {rel_path}")
                
        except Exception as e:
            print(f"  ❌ {filepath}: {e}")
    
    return fixed_count

def main():
    print("🔍 Construction du mapping ID WordPress -> URL...")
    mapping = build_mapping()
    print(f"   {len(mapping)} pages mappées\n")
    
    print("🔧 Correction des liens...")
    fixed = fix_links_with_mapping(mapping)
    print(f"\n✅ {fixed} fichiers corrigés")

if __name__ == "__main__":
    main()
