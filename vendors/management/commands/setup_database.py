from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
import os


class Command(BaseCommand):
    help = 'Set up the database with migrations and sample data'

    def handle(self, *args, **options):
        self.stdout.write('🗄️ Setting up database...')
        
        try:
            # Check if database file exists (for SQLite)
            from django.conf import settings
            if hasattr(settings, 'DATABASES') and 'sqlite3' in settings.DATABASES['default']['ENGINE']:
                db_path = settings.DATABASES['default']['NAME']
                if not os.path.exists(db_path):
                    self.stdout.write(f'Creating database file: {db_path}')
                    os.makedirs(os.path.dirname(db_path), exist_ok=True)
                    open(db_path, 'a').close()
                    self.stdout.write('✅ Database file created')
                else:
                    self.stdout.write(f'✅ Database file exists: {db_path}')
            
            # Run migrations
            self.stdout.write('🔄 Running migrations...')
            call_command('migrate', verbosity=0)
            self.stdout.write('✅ Migrations completed')
            
            # Check if tables exist
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                table_names = [table[0] for table in tables]
                self.stdout.write(f'📋 Tables in database: {len(table_names)} tables')
                
                if 'vendors_business' in table_names:
                    self.stdout.write('✅ vendors_business table exists')
                else:
                    self.stdout.write('❌ vendors_business table missing')
            
            # Populate with sample data if empty
            from vendors.models import Business
            if Business.objects.count() == 0:
                self.stdout.write('🌱 Database is empty, populating with sample data...')
                call_command('populate_businesses')
                self.stdout.write('✅ Sample data populated')
            else:
                self.stdout.write(f'✅ Database has {Business.objects.count()} businesses')
                
        except Exception as e:
            self.stdout.write(f'❌ Error setting up database: {e}')
            raise
        
        self.stdout.write('🎉 Database setup completed successfully!')
