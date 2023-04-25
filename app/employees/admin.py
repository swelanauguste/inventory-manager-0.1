from django.contrib import admin

from .models import Employee, Section

admin.site.register(Section)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "section", "ext"]
