#!/bin/sh
set -e

echo "Waiting for database and running migrations..."

until alembic upgrade head; do
  echo "Migration failed, retrying in 2 seconds..."
  sleep 2
done

echo "Migrations complete. Starting server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
