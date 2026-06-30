#!/bin/sh
set -e

# Immer im Projektverzeichnis arbeiten
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

DB_FILE="data/database.db"
BACKUP_DIR="backups"

if [ ! -f "$DB_FILE" ]; then
    echo "Error: Database not found: $DB_FILE"
    exit 1
fi

mkdir -p "$BACKUP_DIR"

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/database_$TIMESTAMP.db"

cp "$DB_FILE" "$BACKUP_FILE"

echo "Backup created:"
echo "  $BACKUP_FILE"