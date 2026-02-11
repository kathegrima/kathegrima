import random
import re
from pathlib import Path

def get_random_quote():
    """Legge una quote random dal file quotes.txt"""
    quotes_file = Path("quotes.txt")
    
    if not quotes_file.exists():
        return "🤖 Innovation is taking two things that exist and putting them together in a new way. - Tom Freston"
    
    with open(quotes_file, 'r', encoding='utf-8') as f:
        quotes = [line.strip() for line in f if line.strip()]
    
    return random.choice(quotes) if quotes else "🚀 Keep building awesome things!"

def update_readme():
    """Aggiorna il README.md con una nuova quote"""
    readme_file = Path("README.md")
    
    if not readme_file.exists():
        print("❌ README.md non trovato!")
        return
    
    # Leggi il contenuto del README
    with open(readme_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ottieni una nuova quote
    new_quote = get_random_quote()
    
    # Pattern per trovare il blocco tra i commenti
    pattern = r'<!-- QUOTE:START -->.*?<!-- QUOTE:END -->'
    replacement = f'<!-- QUOTE:START -->\n{new_quote}\n<!-- QUOTE:END -->'
    
    # Sostituisci il contenuto
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Scrivi il nuovo contenuto
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ README aggiornato con: {new_quote}")

if __name__ == "__main__":
    update_readme()
