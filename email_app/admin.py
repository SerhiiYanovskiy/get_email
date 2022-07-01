from django.contrib import admin
from .models import Email


@admin.register(Email)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at", "ip_address")



