from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('staff/<int:pk>', views.StaffView.as_view(), name='staff'),
    path('calendar/<int:pk>/', views.CalendarView.as_view(), name='calendar'), # 追加
    path('calendar/<int:pk>/<int:year>/<int:month>/<int:day>/', views.CalendarView.as_view(), name='calendar'), # 追加
]