#!/usr/bin/env python3
"""
Script pour ajouter une FAQ personnalisée sur chaque page ville.
Extrait les données de la page (prix, province, communes voisines) et génère 4 questions/réponses.
"""

import os
import re
import glob

SITE_DIR = "/Users/marc/Desktop/estimation-maison"

# Mapping des provinces
PROVINCE_MAPPING = {
    'anvers': 'Anvers',
    'antwerpen': 'Anvers',
    'brabant flamand': 'Brabant flamand',
    'brabant-flamand': 'Brabant flamand',
    'brabant wallon': 'Brabant wallon',
    'brabant-wallon': 'Brabant wallon',
    'bruxelles': 'Bruxelles',
    'flandre occidentale': 'Flandre occidentale',
    'flandre-occidentale': 'Flandre occidentale',
    'flandre orientale': 'Flandre orientale',
    'flandre-orientale': 'Flandre orientale',
    'hainaut': 'Hainaut',
    'liege': 'Liège',
    'liège': 'Liège',
    'limbourg': 'Limbourg',
    'luxembourg': 'Luxembourg',
    'namur': 'Namur',
}

def extract_city_name(content):
    """Extrait le nom de la ville depuis le H1"""
    match = re.search(r'<h1[^>]*>Prix m² à ([^<]+)</h1>', content)
    if match:
        return match.group(1).strip()
    return None

def extract_price(content):
    """Extrait le prix moyen au m²"""
    match = re.search(r'prix moyen au m² à [^p]+ pour tous les types de biens est de ([\d\s]+) €', content, re.IGNORECASE)
    if match:
        return match.group(1).strip().replace(' ', ' ')
    # Fallback: chercher dans les encadrés
    match = re.search(r'<p style="font-size: 80px[^>]*>([\d\s]+) € / m²</p>', content)
    if match:
        return match.group(1).strip()
    return "2 000"

def extract_province(content):
    """Extrait le nom de la province"""
    match = re.search(r'province (?:de |d&rsquo;|d\')([A-Za-zéè\-]+)', content, re.IGNORECASE)
    if match:
        province_raw = match.group(1).strip().lower().replace('.', '')
        if province_raw in PROVINCE_MAPPING:
            return PROVINCE_MAPPING[province_raw]
        return match.group(1).strip()
    return "la province"

def extract_neighbors(content):
    """Extrait les noms des communes voisines"""
    neighbors = []
    # Pattern pour les liens vers communes voisines
    pattern = r'<a href="\.\./prix-m2-a-[^/]+/"[^>]*>([^<]+)</a>'
    matches = re.findall(pattern, content)
    for m in matches[:3]:  # Max 3 voisines
        neighbors.append(m.strip())
    return neighbors

def generate_faq(city_name, price, province, neighbors):
    """Génère le bloc FAQ personnalisé"""
    
    # Construire la liste des voisines pour le texte
    if len(neighbors) >= 2:
        neighbors_text = f"{neighbors[0]} et {neighbors[1]}"
    elif len(neighbors) == 1:
        neighbors_text = neighbors[0]
    else:
        neighbors_text = "les communes voisines"
    
    faq_html = f'''
<!-- FAQ personnalisée -->
<div style="margin-top: 40px; padding: 30px; background-color: #f8f9fa; border-radius: 8px;">
<h2 style="color: #333; margin-bottom: 25px;">Questions fréquentes sur l'immobilier à {city_name}</h2>

<div style="margin-bottom: 25px;">
<h3 style="font-size: 18px; color: #28a745; margin-bottom: 10px;">Quel est le prix moyen au m² à {city_name} ?</h3>
<p style="color: #666;">Le prix moyen au mètre carré à {city_name} est d'environ {price} € pour l'ensemble des types de biens. Les maisons et les appartements peuvent cependant varier en fonction de la surface, de l'état et de la localisation précise dans la commune.</p>
</div>

<div style="margin-bottom: 25px;">
<h3 style="font-size: 18px; color: #28a745; margin-bottom: 10px;">Les prix à {city_name} sont-ils élevés par rapport au reste de la province ?</h3>
<p style="color: #666;">{city_name} se situe dans la moyenne de la province de {province}. Pour une comparaison détaillée, consultez notre page sur les prix au m² dans la province. Cela vous permettra de mieux situer {city_name} par rapport aux autres communes.</p>
</div>

<div style="margin-bottom: 25px;">
<h3 style="font-size: 18px; color: #28a745; margin-bottom: 10px;">{city_name} est-elle intéressante pour acheter ou investir ?</h3>
<p style="color: #666;">La commune peut convenir à différents profils : résidence principale, investissement locatif ou résidence secondaire. Pour un investissement, il est utile de comparer les rendements locatifs avec ceux des communes voisines comme {neighbors_text}, où la demande peut être différente.</p>
</div>

<div style="margin-bottom: 0;">
<h3 style="font-size: 18px; color: #28a745; margin-bottom: 10px;">Comment utiliser le prix au m² pour estimer un bien à {city_name} ?</h3>
<p style="color: #666;">Le prix au m² donne un point de départ, mais il doit être ajusté en fonction de l'état du bien, de son emplacement exact, de son terrain et de son type. Il est conseillé de comparer avec plusieurs biens similaires vendus récemment à {city_name} et dans les communes voisines pour affiner votre réflexion.</p>
</div>
</div>
'''
    return faq_html

def add_faq_to_page(filepath):
    """Ajoute la FAQ personnalisée à une page ville"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier si FAQ déjà présente
        if 'Questions fréquentes sur l\'immobilier à' in content:
            return False
        
        original = content
        
        # Extraire les données
        city_name = extract_city_name(content)
        if not city_name:
            return False
        
        price = extract_price(content)
        province = extract_province(content)
        neighbors = extract_neighbors(content)
        
        # Générer la FAQ
        faq_html = generate_faq(city_name, price, province, neighbors)
        
        # Insérer avant le footer (après la section province)
        # Chercher la fin de la section province
        pattern = r'(</div>\s*</div>\s*</div>\s*</div>\s*</article>)'
        
        if re.search(pattern, content):
            content = re.sub(pattern, faq_html + r'\1', content)
        else:
            # Fallback: insérer avant </article>
            content = content.replace('</article>', faq_html + '</article>')
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Erreur {filepath}: {e}")
        return False

def main():
    print("🔧 Ajout de FAQ personnalisées sur les pages de villes...")
    
    city_pages = glob.glob(os.path.join(SITE_DIR, "prix-m2-a-*/index.html"))
    
    print(f"   {len(city_pages)} pages de villes à traiter\n")
    
    fixed = 0
    for filepath in city_pages:
        if add_faq_to_page(filepath):
            fixed += 1
    
    print(f"\n✅ {fixed} pages avec FAQ ajoutée")

if __name__ == "__main__":
    main()
