#!/bin/sh
set -e

# Immer im Projektverzeichnis arbeiten
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

echo "Creating backup..."
./deploy/backup.sh

echo "Stopping application..."
docker compose -f docker-compose.prod.yml down

echo "Building and starting application..."
docker compose -f docker-compose.prod.yml up -d --build

echo "Release completed successfully."