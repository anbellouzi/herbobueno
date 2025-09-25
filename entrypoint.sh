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

# Check database connection
echo "🔍 Testing database connection..."
python manage.py check --database default

# Show current migrations status
echo "📋 Current migration status:"
python manage.py showmigrations

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate --noinput --verbosity=2

# Verify tables were created
echo "🔍 Verifying database tables..."
python manage.py shell -c "
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute('SELECT name FROM sqlite_master WHERE type=\"table\";')
    tables = cursor.fetchall()
    print('Tables in database:', [table[0] for table in tables])
"

# Collect static files (in case they weren't collected during build)
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Start the application
echo "🌐 Starting application..."
exec "$@"
