from django.urls import path

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echo, name='echos'),
    path('echo/<pk>/', views.echo_details, name='echos-details'),
    path('add/', views.echo_add, name='echos-add'),
    path('echo/<pk>/waves', views.echo_wave, name='echos-wave'),
    path('echo/<pk>/waves/add', views.echo_add_wave, name='echos-add-wave'),
]
