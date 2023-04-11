from django.contrib import admin

from .models import Department, Employee, UnitSection

admin.site.register(Department)
admin.site.register(UnitSection)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "dept", "ext"]
