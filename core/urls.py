from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('service_auth.urls')),
    path('api/v1/schedules/', include('schedules.urls')),
    path('admin/', admin.site.urls),
]
