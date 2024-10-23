from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog2-home'),
    path('player/', views.player, name='blog2-player'),
    path('team/', views.team, name='blog2-team'),
]
