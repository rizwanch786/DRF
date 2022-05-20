from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['enrollment','name','email','discipline', 'view']
    radio_fields = {'discipline': admin.HORIZONTAL}

    def view(self, obj):
        return format_html(f'<a href="/admin/orm/student/{obj.id}" class="button button5">View<a/>')

@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email','department']
    radio_fields = {'department': admin.VERTICAL}