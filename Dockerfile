# Utilise une image officielle Python
FROM python:3.13-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Installer uv (gestionnaire si tu utilises uv, sinon pip classique)
RUN pip install uv \
 && uv pip install --system --no-cache-dir .

# OU si tu n’utilises pas `uv`, fais simplement :
# RUN pip install -r requirements.txt

# Lancer le bot
CMD ["python", "main.py"]
