from django.urls import include, re_path
from rest_framework.authtoken import views


urlpatterns = [
    re_path(r'^v\d+/api-token-auth/$', views.obtain_auth_token),
    re_path(r'v\d+/', include('api.urls')),
]
