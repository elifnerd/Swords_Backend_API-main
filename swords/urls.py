from django.urls import path
from . import views

urlpatterns = [
    path('', views.swords_list),
    path('<int:pk>/', views.swords_detail)
]