#!/bin/sh
set -e

if [ ! -f /app/yoyo.ini ]; then
  echo "Initializing yoyo configuration..."
  poetry run yoyo init --database postgresql+psycopg://${DATABASE_USER}:${DATABASE_PASSWORD}@${DATABASE_HOST}:${DATABASE_PORT}/${DATABASE_NAME} migrations
fi

echo "Applying migrations"
poetry run yoyo develop

echo "Starting uvicorn..."
poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000