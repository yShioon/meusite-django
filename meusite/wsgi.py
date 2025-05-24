import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meusite.settings')
application = get_wsgi_application()  # <-- Este nome deve bater com o comando