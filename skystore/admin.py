
from django.contrib import admin

from skystore.models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active',)
    list_filter = ('first_name', 'last_name', 'is_active',)

