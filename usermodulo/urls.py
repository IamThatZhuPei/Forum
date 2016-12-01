from django.conf.urls import url
from .view import user_register, activate

urlpatterns = [
    url(r'^register/', user_register, name="register"),
    url(r'^activate/(?P<code>\w+)$', activate),
]
