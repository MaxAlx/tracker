from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('service_auth.urls')),
    path('admin/', admin.site.urls),
]
