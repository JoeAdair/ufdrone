from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_sighting, name='submit_sighting'),
    path('success/', views.sighting_success, name='sighting_success'),
    path('list/', views.list_sightings, name='list_sightings'),
]
