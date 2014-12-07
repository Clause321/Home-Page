"""
WSGI config for wyfHP project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import sys
from os import path
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wyfHP.settings_product")

projectPath = path.dirname(path.dirname(path.abspath(__file__)))
if not projectPath in sys.path:
    sys.path.append(projectPath)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
