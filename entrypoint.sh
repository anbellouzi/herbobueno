#!/bin/bash
set -e

echo "🚀 Starting Herbo Bueno deployment..."

# Debug environment
echo "🔍 Environment variables:"
echo "DATABASE_URL: ${DATABASE_URL:-'Not set'}"
echo "RAILWAY_ENVIRONMENT: ${RAILWAY_ENVIRONMENT:-'Not set'}"
echo "DEBUG: ${DEBUG:-'Not set'}"

# Wait for database to be ready (if using PostgreSQL)
if [ "$DATABASE_URL" ]; then
    echo "🗄️ Waiting for database to be ready..."
    sleep 5
fi

# Set up database using our custom command
echo "🗄️ Setting up database..."
python manage.py setup_database

# Collect static files (in case they weren't collected during build)
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Start the application
echo "🌐 Starting application..."
exec "$@"
