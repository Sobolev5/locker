import os.path
import sys

PROJECT_PATH = "%s" % os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PROJECT_PATH))
sys.path.insert(0, os.path.join(PROJECT_PATH, "apps"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()