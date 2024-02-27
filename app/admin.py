from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Kitten)
class KittensAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'cuteness', 'softness', 'created_at', 'updated_at')
