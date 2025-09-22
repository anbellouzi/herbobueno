"""
ASGI config for herbo_bueno project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'herbo_bueno.settings')

application = get_asgi_application()

