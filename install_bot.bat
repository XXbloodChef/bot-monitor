@echo off
echo === Création de l'environnement virtuel ===
python -m venv env
call env\Scripts\activate
echo === Installation des dépendances ===
pip install --upgrade pip
pip install -r requirements.txt
echo === Installation des navigateurs Playwright ===
playwright install
echo === Copie du .env.example vers .env ===
copy .env.example .env
echo === Installation terminée ===
pause
