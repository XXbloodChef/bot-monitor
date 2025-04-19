#!/bin/bash
echo "=== Création de l'environnement virtuel ==="
python3 -m venv env
source env/bin/activate
echo "=== Installation des dépendances ==="
pip install --upgrade pip
pip install -r requirements.txt
echo "=== Installation des navigateurs Playwright ==="
playwright install
echo "=== Copie du .env.example vers .env ==="
cp .env.example .env
echo "=== Installation terminée ==="
