"""
WSGI config for ihi_backend_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys

# add the hellodjango project path into the sys.path
sys.path.append('/home/ihior354/new_website/ihi_backend_web')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/ihior354/new_website/venv/lib/python3.6/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ihi_backend_web.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
