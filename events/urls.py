from django.urls import path
from events import views

urlpatterns = [
    path('', views.EventListCreateAPIView.as_view()),
    path('<int:pk>/', views.EventDetailAPIView.as_view()),
]