from .Register import urlpatterns as register_urlpatterns
from .login import urlpatterns as login_urlpatterns
from .ecommerce import urlpatterns as ecommerce_urlpatterns

urlpatterns = (
    [] + register_urlpatterns + login_urlpatterns+ecommerce_urlpatterns
)
