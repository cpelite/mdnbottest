#!/bin/sh
echo "Ziehe Änderungen aus dem Github-Repo"
git pull
echo "Aktiviere VENV"
source /venv/bin/activate
echo "Starte Bot"
nohup python3 bot.py
echo "Bot gestartet"