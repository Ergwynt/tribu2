from django.contrib import admin

from .models import Wave


@admin.register(Wave)
class EchoAdmin(admin.ModelAdmin):
    list_display = ('content', 'echo', 'user', 'created_at')
