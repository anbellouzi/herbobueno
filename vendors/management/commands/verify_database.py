from django.core.management.base import BaseCommand
from django.db import connection
from vendors.models import Business


class Command(BaseCommand):
    help = 'Verify database is working correctly'

    def handle(self, *args, **options):
        self.stdout.write('🔍 Verifying database...')
        
        try:
            # Check if database file exists
            from django.conf import settings
            db_path = settings.DATABASES['default']['NAME']
            self.stdout.write(f'Database path: {db_path}')
            
            # Check tables
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                table_names = [table[0] for table in tables]
                self.stdout.write(f'Tables found: {len(table_names)}')
                
                if 'vendors_business' in table_names:
                    self.stdout.write('✅ vendors_business table exists')
                else:
                    self.stdout.write('❌ vendors_business table missing')
                    return
            
            # Check business count
            business_count = Business.objects.count()
            self.stdout.write(f'Businesses in database: {business_count}')
            
            if business_count > 0:
                self.stdout.write('✅ Database is working correctly')
            else:
                self.stdout.write('⚠️ Database is empty but working')
                
        except Exception as e:
            self.stdout.write(f'❌ Database error: {e}')
            raise
