from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'less_address', 'view']
    
    def less_address(self, obj):
        return obj.address[:100]
    
    def view(self, obj):
        return format_html(f'<a href="/admin/{obj.id}" class="button button5">View</a>')
