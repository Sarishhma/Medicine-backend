from .Register import urlpatterns as register_urlpatterns
from .login import urlpatterns as login_urlpatterns

urlpatterns = (
    [] + register_urlpatterns + login_urlpatterns
)
