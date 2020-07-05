from django.urls import path, register_converter
from customizations.url_converters import DateConverter
from events import views


register_converter(DateConverter, 'Ymd')

# /api/v1/events/
urlpatterns = [
    path('', views.EventListCreateAPIView.as_view()),
    path('<int:pk>/', views.EventDetailAPIView.as_view()),
    path('<Ymd:date>/', views.EventListByDateAPIView.as_view()),
    path('tags/', views.EventTagListCreateAPIView.as_view()),
]
