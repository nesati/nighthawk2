from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('navod/', views.navod),
    path('seznam/', views.seznam)
]
