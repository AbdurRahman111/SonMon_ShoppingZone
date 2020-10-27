from django.contrib import admin
from .models import register

# Register your models here.

class register_dis(admin.ModelAdmin):
    list_display = ['name','email']



admin.site.register(register, register_dis)
