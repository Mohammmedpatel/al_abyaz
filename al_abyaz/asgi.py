"""
ASGI config for al_abyaz project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'al_abyaz.settings')

application = get_asgi_application()
