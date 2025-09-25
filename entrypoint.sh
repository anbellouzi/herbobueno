#!/bin/bash
set -e

echo "🚀 Starting Herbo Bueno deployment..."

# Create database file if it doesn't exist
echo "🗄️ Ensuring database file exists..."
python -c "
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

# Run migrations
echo "🔄 Running migrations..."
python manage.py migrate --noinput

# Populate with sample data
echo "🌱 Populating sample data..."
python manage.py populate_businesses

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Start the application
echo "🌐 Starting application..."
exec "$@"
