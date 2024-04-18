from django.contrib import admin

# Register your models here.
from .models import VacationRequest

class VacationRequestAdmin(admin.ModelAdmin):
    model = VacationRequest


admin.site.register(VacationRequest, VacationRequestAdmin)