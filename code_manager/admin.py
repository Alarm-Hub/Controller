from django.contrib import admin
from code_manager.models import Code


# Register your models here.

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    pass
