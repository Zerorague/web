from django.contrib import admin
from avisosApp import models

# Register your models here.


class AvisoAdmin(admin.ModelAdmin):
    search_fields = ("id", "asunto", "mensaje")
    list_display = ("id", "asunto")


admin.site.register(models.Aviso, AvisoAdmin)
