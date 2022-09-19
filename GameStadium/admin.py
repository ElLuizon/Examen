from django.contrib import admin
from .models import GStadium
# Register your models here.


@admin.register(GStadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ["name","location","sponsor","status"]