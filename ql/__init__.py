# bootstrap Django for ORM
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ql.settings")
from django.core.wsgi import get_wsgi_application
get_wsgi_application()
