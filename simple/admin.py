from django.contrib import admin
from .models import User, Product
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Product)
# Register your models here.
