from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog1-home'),
    path('player/', views.player, name='blog1-player'),
    path('team/', views.team, name='blog1-team'),
]
