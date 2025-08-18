from django.contrib import admin
from .models import contact

# Register your models here.

@admin.register(contact)
class contactsubmissionAdmin(admin.ModelAdmin):
    list_display = ("name","email","created_at")
    search_fields = ("name","email")