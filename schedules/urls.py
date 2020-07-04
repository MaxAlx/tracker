from django.urls import path
from schedules import views


urlpatterns = [
    path('tasks/', views.TaskListCreateAPIView.as_view()),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyAPIView.as_view()),
]
