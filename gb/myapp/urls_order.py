from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_index, name='index'),
    path('<int:pk>/', views.get_orders, name='orders'),
    path('<int:pk>/time/', views.get_orders_by_time, name='orders_by_time'),
]
