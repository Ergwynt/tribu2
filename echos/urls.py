from django.urls import path

from . import views

app_name = 'echos'

urlpatterns = [
    path('echos/', views.echo, name='echos'),
    path('echos/<pk>/', views.echo_details, name='echos-details'),
    path('echos/add/', views.echo_add, name='echos-add'),
    path('echos/<pk>/waves', views.echo_wave, name='echos-wave'),
    path('echos/<pk>/waves/add', views.echo_add_wave, name='echos-add-wave'),
]
