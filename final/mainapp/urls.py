from django.urls import path, include
from . import views


urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('error/', views.error, name = 'error'),
]

