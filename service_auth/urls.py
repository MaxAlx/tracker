from django.urls import path, include
from service_auth.views import GoogleLogin

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('google/', GoogleLogin.as_view(), name='google_login')
]
