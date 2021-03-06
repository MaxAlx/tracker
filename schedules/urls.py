from django.urls import path
from schedules import views


# /api/v1/schedules/
urlpatterns = [
    path('', views.DayScheduleListCreateAPIView.as_view()),
    path('<int:pk>/', views.DayScheduleRetrieveUpdateDestroyAPIView.as_view()),
    path('tasks/', views.TaskListCreateAPIView.as_view()),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyAPIView.as_view()),
    path('common/', views.ScheduleRetrieveUpdateAPIView.as_view()),
    path('common/reset/', views.ScheduleResetAPIView.as_view()),
]
