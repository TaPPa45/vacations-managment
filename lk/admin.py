from django.contrib import admin

# Register your models here.
from .models import User

class UsersAdmin(admin.ModelAdmin):
    model = User


admin.site.register(User, UsersAdmin)
