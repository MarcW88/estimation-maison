#!/usr/bin/env python3
"""
Script pour corriger les liens vers les pages de villes
en utilisant le texte du lien pour trouver la bonne URL.
"""

import os
import re
import glob
from unidecode import unidecode

SITE_DIR = "/Users/marc/Desktop/estimation-maison"

def normalize_city_name(name):
    """Normalise le nom d'une ville pour le matcher avec le dossier"""
    # Enlève les accents
    name = unidecode(name.lower())
    # Remplace les espaces et caractères spéciaux par des tirets
    name = re.sub(r'[^a-z0-9]+', '-', name)
    # Enlève les tirets en début/fin
    name = name.strip('-')
    return name

def get_available_cities():
    """Récupère la liste des villes disponibles"""
    cities = {}
    for folder in glob.glob(os.path.join(SITE_DIR, "prix-m2-a-*")):
        if os.path.isdir(folder):
            folder_name = os.path.basename(folder)
            # Extrait le nom de la ville (après "prix-m2-a-")
            city_name = folder_name.replace("prix-m2-a-", "")
            cities[city_name] = f"{folder_name}/index.html"
    return cities

def fix_estimation_par_ville():
    """Corrige les liens dans estimation-par-ville/index.html"""
    filepath = os.path.join(SITE_DIR, "estimation-par-ville/index.html")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    cities = get_available_cities()
    
    # Pattern pour trouver les liens cassés avec le texte
    # <a href='../index.html%3Fp=XXX.html'>Estimation immobilière à VILLE</a>
    pattern = r"<a href='\.\.\/index\.html%3Fp=\d+\.html'>Estimation immobilière à ([^<]+)</a>"
    
    def replace_link(match):
        city_name = match.group(1).strip()
        normalized = normalize_city_name(city_name)
        
        # Cherche la ville dans les dossiers disponibles
        if normalized in cities:
            return f"<a href='../{cities[normalized]}'>{city_name}</a>"
        
        # Essaie des variations
        for city_key, city_url in cities.items():
            if normalized in city_key or city_key in normalized:
                return f"<a href='../{city_url}'>{city_name}</a>"
        
        # Si pas trouvé, garde le lien vers estimation-par-ville
        print(f"  ⚠️ Ville non trouvée: {city_name} ({normalized})")
        return f"<a href='../estimation-par-ville/index.html'>{city_name}</a>"
    
    content = re.sub(pattern, replace_link, content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("🔧 Correction des liens dans estimation-par-ville...")
    
    # Installe unidecode si nécessaire
    try:
        from unidecode import unidecode
    except ImportError:
        import subprocess
        subprocess.run(['pip3', 'install', 'unidecode', '-q'])
        from unidecode import unidecode
    
    cities = get_available_cities()
    print(f"   {len(cities)} villes disponibles\n")
    
    if fix_estimation_par_ville():
        print("\n✅ estimation-par-ville/index.html corrigé")
    else:
        print("\n⏭️ Aucune modification nécessaire")

if __name__ == "__main__":
    main()
