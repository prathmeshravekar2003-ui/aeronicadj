"""
WSGI config for aeronica project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Ensure the Django project root (aeronica/) is in sys.path.
# This is required when running from the repo root (e.g. on Vercel),
# so that 'aeronica.settings' resolves to aeronica/aeronica/settings.py
DJANGO_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(DJANGO_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(DJANGO_PROJECT_ROOT))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aeronica.settings')

application = get_wsgi_application()

app = application
