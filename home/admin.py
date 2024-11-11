from django.contrib import admin

from .models import UploadedFile


@admin.register(UploadedFile)
class GameTableAdmin(admin.ModelAdmin):
    list_display = ('file',)