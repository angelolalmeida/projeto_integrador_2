from django.contrib import admin
from .models import Morador

# Register your models here.


@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    pass
