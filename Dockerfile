# Python-Image als Basis
FROM python:3.12-slim

# Verhindert unnötige Python-Dateien und sorgt für direkte Ausgabe
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Arbeitsverzeichnis im Container erstellen
WORKDIR /app

# Nützliche Werkzeuge installieren
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Requirements-Datei kopieren und Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Eigenen App Code in den Container kopieren
COPY . .

# Benutzer für die Entwicklung anlegen
RUN groupadd --gid 1001 appgroup \
    && useradd --uid 1001 --gid appgroup --create-home --shell /bin/bash appuser \
    && chown -R appuser:appgroup /app

# Als normaler User und nicht als root ausführen
USER appuser

# Standardbefehl zum Ausführen der Tests
CMD [ "/bin/bash" ]

