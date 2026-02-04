"""
WSGI config for al_abyaz project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'al_abyaz.settings')

application = get_wsgi_application()
