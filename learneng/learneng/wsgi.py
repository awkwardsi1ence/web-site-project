"""
WSGI config for learneng project.

It exposes the WSGI callable as main module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learneng.settings')

application = get_wsgi_application()
