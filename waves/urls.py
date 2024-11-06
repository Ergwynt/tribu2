from django.urls import path

from . import views

app_name = 'waves'

urlpatterns = [
    path('wave/<pk>/edit', views.edit_wave, name='edit-wave'),
    path('wave/<pk>/delete', views.delete_wave, name='delete-wave'),
]
