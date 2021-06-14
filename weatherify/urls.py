from django.urls import path
from weatherify import views

urlpatterns = [
    path('', views.home, name='home'),
]