from django.conf.urls import url
from .view import user_register, activate, upload_avatar

urlpatterns = [
    url(r'^register/', user_register, name="register"),
    url(r'^activate/(?P<code>\w+)$', activate),
    url(r'^uploadavatar/', upload_avatar),
]
