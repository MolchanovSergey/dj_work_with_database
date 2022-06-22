from django.contrib import admin

# Register your models here.
from .models import Phone


class PhoneAdmin(admin.ModelAdmin):
    # Поле slug будет заполнено на основе поля name
    repopulated_fields = {"slug": ("name",)}


admin.site.register(Phone, PhoneAdmin)
from django.contrib import admin

# Register your models here.
