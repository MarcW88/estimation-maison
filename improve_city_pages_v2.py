#!/usr/bin/env python3
"""
Script pour améliorer les pages de villes selon les recommandations:
1. Ajouter H2 "Prix immobilier à [Ville] : résumé" après le H1
2. Ajouter lien vers province dans l'intro
3. Ajouter bloc "Pour quel type de projet ?"
4. Renforcer le maillage interne
"""

import os
import re
import glob

SITE_DIR = "/Users/marc/Desktop/estimation-maison"

# Mapping des provinces
PROVINCE_MAPPING = {
    'anvers': ('Anvers', '../prix-m2-anvers/'),
    'antwerpen': ('Anvers', '../prix-m2-anvers/'),
    'brabant flamand': ('Brabant flamand', '../prix-m2-brabant-flamand/'),
    'brabant-flamand': ('Brabant flamand', '../prix-m2-brabant-flamand/'),
    'brabant wallon': ('Brabant wallon', '../prix-m2-brabant-wallon/'),
    'brabant-wallon': ('Brabant wallon', '../prix-m2-brabant-wallon/'),
    'bruxelles': ('Bruxelles', '../prix-m2-bruxelles/'),
    'flandre occidentale': ('Flandre occidentale', '../prix-m2-flandre-occidentale/'),
    'flandre-occidentale': ('Flandre occidentale', '../prix-m2-flandre-occidentale/'),
    'flandre orientale': ('Flandre orientale', '../prix-m2-flandre-orientale/'),
    'flandre-orientale': ('Flandre orientale', '../prix-m2-flandre-orientale/'),
    'hainaut': ('Hainaut', '../prix-m2-hainaut/'),
    'liege': ('Liège', '../prix-m2-liege/'),
    'liège': ('Liège', '../prix-m2-liege/'),
    'limbourg': ('Limbourg', '../prix-m2-limbourg/'),
    'luxembourg': ('Luxembourg', '../prix-m2-luxembourg/'),
    'namur': ('Namur', '../prix-m2-namur/'),
}

def extract_city_name(filepath):
    """Extrait le nom de la ville depuis le H1"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'<h1[^>]*>Prix m² à ([^<]+)</h1>', content)
    if match:
        return match.group(1).strip()
    return None

def extract_province(content):
    """Extrait le nom de la province depuis le contenu"""
    match = re.search(r'province (?:de |d&rsquo;|d\')([A-Za-zé\-]+)', content, re.IGNORECASE)
    if match:
        province_name = match.group(1).strip().lower().replace('.', '')
        if province_name in PROVINCE_MAPPING:
            return PROVINCE_MAPPING[province_name]
    return None

def improve_city_page(filepath):
    """Améliore une page de ville avec toutes les recommandations"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        city_name = extract_city_name(filepath)
        province_info = extract_province(content)
        
        if not city_name:
            return False
        
        # 1. Ajouter H2 "Prix immobilier à [Ville] : résumé" après le H1 (si pas déjà présent)
        if 'Prix immobilier à' not in content and f': résumé' not in content:
            h1_pattern = r'(<h1[^>]*>Prix m² à [^<]+</h1></div></div>)'
            h2_summary = f'\\1<h2 style="margin-top: 10px; font-size: 22px; color: #666;">Prix immobilier à {city_name} : résumé</h2>'
            content = re.sub(h1_pattern, h2_summary, content)
        
        # 2. Ajouter lien vers province dans l'intro (après le premier paragraphe)
        if province_info and 'Pour comparer avec le reste de la province' not in content:
            province_name, province_url = province_info
            intro_pattern = r'(<p style="margin-bottom: 20px;">[^<]+</p>)'
            province_link = f'''\\1
<p style="margin-bottom: 20px; font-size: 14px; color: #666;">Pour comparer avec le reste de la province, consultez aussi notre page sur le <a href="{province_url}" style="color: #28a745;">prix au m² en province de {province_name}</a>.</p>'''
            content = re.sub(intro_pattern, province_link, content, count=1)
        
        # 3. Ajouter bloc "Pour quel type de projet ?" après "Pourquoi acheter"
        if 'Pour quel type de projet' not in content:
            pourquoi_pattern = r'(<h2 style="margin-top: 40px;">Pourquoi acheter à [^<]+\?</h2>)'
            projet_block = f'''\\1
<div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="color: #28a745; margin-bottom: 15px;">Pour quel type de projet ?</h3>
<ul style="list-style: none; padding: 0; margin: 0;">
<li style="margin-bottom: 10px; padding-left: 25px; position: relative;"><span style="color: #28a745; position: absolute; left: 0;">✓</span> <strong>Résidence principale</strong> : idéal pour les familles et les actifs</li>
<li style="margin-bottom: 10px; padding-left: 25px; position: relative;"><span style="color: #28a745; position: absolute; left: 0;">✓</span> <strong>Investissement locatif</strong> : rendement potentiel selon le quartier</li>
<li style="margin-bottom: 10px; padding-left: 25px; position: relative;"><span style="color: #28a745; position: absolute; left: 0;">✓</span> <strong>Résidence secondaire</strong> : selon l'attrait touristique de la région</li>
</ul>
</div>'''
            content = re.sub(pourquoi_pattern, projet_block, content)
        
        # 4. Ajouter lien vers hub "autres villes" (améliorer celui existant ou l'ajouter)
        if "Voir les prix au m² dans d'autres villes" not in content:
            # Chercher la fin de la section communes voisines
            pattern = r'(</ul>\s*</div>\s*<div style="display: flex; align-items: center;)'
            if re.search(pattern, content):
                replacement = '''</ul>
<p style="margin-top: 20px; text-align: center;"><a href="../estimation-par-ville/" style="color: #28a745; font-weight: bold;">→ Voir les prix au m² dans d'autres villes de Belgique</a></p>
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
    print("🔧 Amélioration complète des pages de villes...")
    
    city_pages = glob.glob(os.path.join(SITE_DIR, "prix-m2-a-*/index.html"))
    
    print(f"   {len(city_pages)} pages de villes à traiter\n")
    
    fixed = 0
    for filepath in city_pages:
        if improve_city_page(filepath):
            fixed += 1
    
    print(f"\n✅ {fixed} pages améliorées")

if __name__ == "__main__":
    main()
