#!/usr/bin/env python3
"""
Script pour corriger les liens sur les pages de villes (prix-m2-a-*)
- Corrige les liens vers les villes voisines (index.html%3Fp=XXX.html -> prix-m2-a-ville/index.html)
- Corrige le lien vers la page province spécifique
"""

import os
import re
import glob
from unidecode import unidecode

SITE_DIR = "/Users/marc/Desktop/estimation-maison"

# Mapping des provinces
PROVINCE_MAPPING = {
    'anvers': 'prix-m2-anvers/index.html',
    'brabant flamand': 'prix-m2-brabant-flamand/index.html',
    'brabant-flamand': 'prix-m2-brabant-flamand/index.html',
    'brabant wallon': 'prix-m2-brabant-wallon/index.html',
    'brabant-wallon': 'prix-m2-brabant-wallon/index.html',
    'bruxelles': 'prix-m2-bruxelles/index.html',
    'flandre occidentale': 'prix-m2-flandre-occidentale/index.html',
    'flandre-occidentale': 'prix-m2-flandre-occidentale/index.html',
    'flandre orientale': 'prix-m2-flandre-orientale/index.html',
    'flandre-orientale': 'prix-m2-flandre-orientale/index.html',
    'hainaut': 'prix-m2-hainaut/index.html',
    'liege': 'prix-m2-liege/index.html',
    'liège': 'prix-m2-liege/index.html',
    'limbourg': 'prix-m2-limbourg/index.html',
    'luxembourg': 'prix-m2-luxembourg/index.html',
    'namur': 'prix-m2-namur/index.html',
}

def normalize_city_name(name):
    """Normalise le nom d'une ville"""
    name = unidecode(name.lower())
    name = re.sub(r'[^a-z0-9]+', '-', name)
    name = name.strip('-')
    return name

def get_available_cities():
    """Récupère la liste des villes disponibles"""
    cities = {}
    for folder in glob.glob(os.path.join(SITE_DIR, "prix-m2-a-*")):
        if os.path.isdir(folder):
            folder_name = os.path.basename(folder)
            city_name = folder_name.replace("prix-m2-a-", "")
            cities[city_name] = f"{folder_name}/index.html"
    return cities

def fix_city_page(filepath, cities):
    """Corrige les liens dans une page de ville"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # 1. Corrige les liens vers les villes voisines
        # Pattern: href="../index.html%3Fp=XXX.html" ... >NomVille</a>
        pattern = r'<a href="\.\.\/index\.html%3Fp=\d+\.html"([^>]*)>([^<]+)</a>'
        
        def replace_city_link(match):
            attrs = match.group(1)
            city_name = match.group(2).strip()
            normalized = normalize_city_name(city_name)
            
            if normalized in cities:
                return f'<a href="../{cities[normalized]}"{attrs}>{city_name}</a>'
            
            for city_key, city_url in cities.items():
                if normalized in city_key or city_key in normalized:
                    return f'<a href="../{city_url}"{attrs}>{city_name}</a>'
            
            return match.group(0)
        
        content = re.sub(pattern, replace_city_link, content)
        
        # 2. Corrige le lien vers la page province
        # Cherche le nom de la province dans le texte
        province_match = re.search(r'province de ([^\.]+)\.', content)
        if province_match:
            province_name = province_match.group(1).strip().lower()
            province_name = re.sub(r'&rsquo;', "'", province_name)
            
            for key, url in PROVINCE_MAPPING.items():
                if key in province_name or province_name in key:
                    # Remplace le lien générique par le lien spécifique
                    content = content.replace(
                        'href="../prix-m2-par-province/index.html"',
                        f'href="../{url}"'
                    )
                    break
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Erreur {filepath}: {e}")
        return False

def main():
    print("🔧 Correction des pages de villes...")
    
    cities = get_available_cities()
    print(f"   {len(cities)} villes disponibles\n")
    
    # Trouve toutes les pages de villes
    city_pages = glob.glob(os.path.join(SITE_DIR, "prix-m2-a-*/index.html"))
    
    print(f"   {len(city_pages)} pages de villes à traiter\n")
    
    fixed = 0
    for filepath in city_pages:
        if fix_city_page(filepath, cities):
            fixed += 1
    
    print(f"\n✅ {fixed} pages corrigées")

if __name__ == "__main__":
    main()
