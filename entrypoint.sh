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

# Ensure database file exists (for SQLite)
if [ ! "$DATABASE_URL" ]; then
    echo "🔍 Ensuring SQLite database file exists..."
    python manage.py shell -c "
import os
from django.conf import settings
db_path = settings.DATABASES['default']['NAME']
if not os.path.exists(db_path):
    print(f'Creating database file: {db_path}')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    open(db_path, 'a').close()
    print('Database file created')
else:
    print(f'Database file exists: {db_path}')
"
fi

# Show current migrations status
echo "📋 Current migration status:"
python manage.py showmigrations

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate --noinput --verbosity=2

# If migrations failed, try to create the database from scratch
if [ $? -ne 0 ]; then
    echo "⚠️ Migrations failed, trying to create database from scratch..."
    python manage.py makemigrations
    python manage.py migrate --noinput --verbosity=2
fi

# Verify tables were created
echo "🔍 Verifying database tables..."
python manage.py shell -c "
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute('SELECT name FROM sqlite_master WHERE type=\"table\";')
    tables = cursor.fetchall()
    print('Tables in database:', [table[0] for table in tables])
"

# Populate database with sample data if empty
echo "🌱 Populating database with sample data..."
python manage.py shell -c "
from vendors.models import Business
if Business.objects.count() == 0:
    print('Database is empty, populating with sample data...')
    from vendors.management.commands.populate_businesses import Command
    cmd = Command()
    cmd.handle()
    print('Sample data populated successfully')
else:
    print(f'Database already has {Business.objects.count()} businesses')
"

# Collect static files (in case they weren't collected during build)
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Start the application
echo "🌐 Starting application..."
exec "$@"
