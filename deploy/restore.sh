#!/bin/sh
set -e

# Immer im Projektverzeichnis arbeiten
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <backup-file>"
    exit 1
fi

BACKUP_FILE="$1"
DB_FILE="data/database.db"

if [ ! -f "$BACKUP_FILE" ]; then
    echo "Error: Backup not found: $BACKUP_FILE"
    exit 1
fi

mkdir -p data

cp "$BACKUP_FILE" "$DB_FILE"

echo "Database restored from:"
echo "  $BACKUP_FILE"