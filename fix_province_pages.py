#!/usr/bin/env python3
"""
Script pour corriger les liens sur les pages de provinces
- Corrige les liens vers les villes (index.html%3Fp=XXX.html -> prix-m2-a-ville/index.html)
- Corrige le CTA simulateur.html -> index.html
"""

import os
import re
import glob
from unidecode import unidecode

SITE_DIR = "/Users/marc/Desktop/estimation-maison"

def normalize_city_name(name):
    """Normalise le nom d'une ville pour le matcher avec le dossier"""
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

def fix_province_page(filepath, cities):
    """Corrige les liens dans une page de province"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Corrige le CTA simulateur
        content = content.replace('href="../simulateur.html"', 'href="../index.html"')
        content = content.replace("href='../simulateur.html'", "href='../index.html'")
        
        # Pattern pour trouver les liens cassés avec le texte
        pattern = r"<a href='\.\.\/index\.html%3Fp=\d+\.html'>([^<]+)</a>"
        
        def replace_link(match):
            link_text = match.group(1).strip()
            # Extrait le nom de la ville du texte
            city_match = re.search(r'(?:Estimation immobilière à |Prix m² à )(.+)', link_text)
            if city_match:
                city_name = city_match.group(1).strip()
            else:
                city_name = link_text
            
            normalized = normalize_city_name(city_name)
            
            # Cherche la ville dans les dossiers disponibles
            if normalized in cities:
                return f"<a href='../{cities[normalized]}'>{link_text}</a>"
            
            # Essaie des variations
            for city_key, city_url in cities.items():
                if normalized in city_key or city_key in normalized:
                    return f"<a href='../{city_url}'>{link_text}</a>"
            
            # Si pas trouvé, retourne le lien original
            return match.group(0)
        
        content = re.sub(pattern, replace_link, content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Erreur {filepath}: {e}")
        return False

def main():
    print("🔧 Correction des pages de provinces...")
    
    cities = get_available_cities()
    print(f"   {len(cities)} villes disponibles\n")
    
    # Liste des pages de provinces
    province_pages = [
        "prix-m2-anvers/index.html",
        "prix-m2-brabant-flamand/index.html",
        "prix-m2-brabant-wallon/index.html",
        "prix-m2-bruxelles/index.html",
        "prix-m2-flandre-occidentale/index.html",
        "prix-m2-flandre-orientale/index.html",
        "prix-m2-hainaut/index.html",
        "prix-m2-liege/index.html",
        "prix-m2-limbourg/index.html",
        "prix-m2-luxembourg/index.html",
        "prix-m2-namur/index.html",
    ]
    
    fixed = 0
    for page in province_pages:
        filepath = os.path.join(SITE_DIR, page)
        if os.path.exists(filepath):
            if fix_province_page(filepath, cities):
                print(f"  ✅ {page}")
                fixed += 1
            else:
                print(f"  ⏭️ {page} (pas de modification)")
        else:
            print(f"  ❌ {page} (fichier non trouvé)")
    
    print(f"\n✅ {fixed} pages corrigées")

if __name__ == "__main__":
    main()
