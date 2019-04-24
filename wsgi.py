from dj_static import Cling
from django.core.wsgi import get_wsgi_application

application = Cling(get_wsgi_application())
