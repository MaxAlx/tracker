from django.urls import path
from events import views


# /api/v1/events/
urlpatterns = [
    path('', views.EventListCreateAPIView.as_view()),
    path('<int:pk>/', views.EventDetailAPIView.as_view()),
    path('tags/', views.EventTagListCreateAPIView.as_view()),
]
