#!/usr/bin/env python3
"""
Script pour repositionner la FAQ après le bloc province (carte + CTA),
sur toute la largeur de la page.
"""

import os
import re
import glob

SITE_DIR = "/Users/marc/Desktop/estimation-maison"

def fix_faq_position(filepath):
    """Déplace la FAQ après le bloc province"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Vérifier si FAQ présente
        if 'Questions fréquentes sur l\'immobilier à' not in content:
            return False
        
        # Extraire le bloc FAQ
        faq_pattern = r'<!-- FAQ personnalisée -->\s*<div style="margin-top: 40px; padding: 30px; background-color: #f8f9fa; border-radius: 8px;">.*?</div>\s*</div>'
        faq_match = re.search(faq_pattern, content, re.DOTALL)
        
        if not faq_match:
            return False
        
        faq_block = faq_match.group(0)
        
        # Supprimer la FAQ de sa position actuelle
        content = re.sub(faq_pattern, '', content, flags=re.DOTALL)
        
        # Trouver la fin du bloc province (après le CTA "Découvrez les prix au m² dans la province")
        # Le bloc province se termine par </div></div> avant </div></div></article>
        
        # Pattern pour trouver la fin du bloc province
        province_end_pattern = r'(Découvrez les prix au m² dans la province de [^<]+\.\s*<br />\s*</a>\s*)</div>\s*</div>'
        
        if re.search(province_end_pattern, content):
            # Insérer la FAQ après le bloc province, en dehors des divs imbriquées
            replacement = r'\1</div>\n</div>\n\n' + faq_block
            content = re.sub(province_end_pattern, replacement, content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Erreur {filepath}: {e}")
        return False

def main():
    print("🔧 Repositionnement de la FAQ sur les pages de villes...")
    
    city_pages = glob.glob(os.path.join(SITE_DIR, "prix-m2-a-*/index.html"))
    
    print(f"   {len(city_pages)} pages de villes à traiter\n")
    
    fixed = 0
    for filepath in city_pages:
        if fix_faq_position(filepath):
            fixed += 1
    
    print(f"\n✅ {fixed} pages corrigées")

if __name__ == "__main__":
    main()
