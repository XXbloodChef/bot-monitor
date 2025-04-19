import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    print("Token Discord manquant dans .env")
else:
    print("Le bot va être lancé ici (code à compléter).")
