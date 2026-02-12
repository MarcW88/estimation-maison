#!/usr/bin/env python3
"""
Script pour convertir la FAQ en format accordéon (expandable/collapsible).
Utilise HTML/CSS pur avec <details> et <summary> pour compatibilité maximale.
"""

import os
import re
import glob

SITE_DIR = "/Users/marc/Desktop/estimation-maison"

def convert_faq_to_accordion(filepath):
    """Convertit la FAQ en format accordéon"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Vérifier si FAQ présente et pas déjà en accordéon
        if 'Questions fréquentes sur l\'immobilier à' not in content:
            return False
        if '<details' in content:
            return False
        
        # Pattern pour trouver chaque question/réponse
        # Structure actuelle: <div><h3>Question</h3><p>Réponse</p></div>
        
        def replace_qa(match):
            question = match.group(1)
            answer = match.group(2)
            return f'''<details style="margin-bottom: 15px; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden;">
<summary style="padding: 15px 20px; background-color: #fff; cursor: pointer; font-size: 16px; font-weight: 600; color: #333; list-style: none; display: flex; justify-content: space-between; align-items: center;">
<span>{question}</span>
<span style="color: #28a745; font-size: 20px; transition: transform 0.3s;">+</span>
</summary>
<div style="padding: 15px 20px; background-color: #fafafa; border-top: 1px solid #e0e0e0;">
<p style="color: #666; margin: 0; line-height: 1.6;">{answer}</p>
</div>
</details>'''
        
        # Pattern pour matcher les blocs Q/R actuels
        qa_pattern = r'<div style="margin-bottom: (?:25px|0);">\s*<h3 style="font-size: 18px; color: #28a745; margin-bottom: 10px;">([^<]+)</h3>\s*<p style="color: #666;">([^<]+)</p>\s*</div>'
        
        content = re.sub(qa_pattern, replace_qa, content)
        
        # Mettre à jour le style du conteneur FAQ
        content = content.replace(
            '<div style="margin-top: 40px; padding: 30px; background-color: #f8f9fa; border-radius: 8px;">',
            '<div style="margin-top: 40px; padding: 30px; background-color: #f8f9fa; border-radius: 12px;">'
        )
        
        # Ajouter le style CSS pour l'accordéon dans le head si pas déjà présent
        if 'details summary::-webkit-details-marker' not in content:
            accordion_css = '''<style>
details summary::-webkit-details-marker { display: none; }
details summary::marker { display: none; }
details[open] summary span:last-child { transform: rotate(45deg); }
details summary:hover { background-color: #f5f5f5; }
</style>
</head>'''
            content = content.replace('</head>', accordion_css)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Erreur {filepath}: {e}")
        return False

def main():
    print("🔧 Conversion de la FAQ en accordéon...")
    
    city_pages = glob.glob(os.path.join(SITE_DIR, "prix-m2-a-*/index.html"))
    
    print(f"   {len(city_pages)} pages de villes à traiter\n")
    
    fixed = 0
    for filepath in city_pages:
        if convert_faq_to_accordion(filepath):
            fixed += 1
    
    print(f"\n✅ {fixed} pages converties en accordéon")

if __name__ == "__main__":
    main()
