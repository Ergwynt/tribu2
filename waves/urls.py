from django.urls import path

from . import views

app_name = 'waves'

urlpatterns = [
    path('waves/<pk>/edit', views.edit_wave, name='edit-wave'),
    path('waves/<pk>/delete', views.delete_wave, name='delete-wave'),
]
