"""
WSGI config for herbo_bueno project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'herbo_bueno.settings')

application = get_wsgi_application()

