from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id","user","product","quantity"]

