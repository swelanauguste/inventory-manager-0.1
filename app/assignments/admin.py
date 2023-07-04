from django.contrib import admin

from .models import ComputerAssignment, PrinterAssignment, ScannerAssignment


@admin.register(ComputerAssignment)
class ComputerAssignmentAdmin(admin.ModelAdmin):
    list_display = ["computer", "employee", "date_assigned", "date_returned"]


@admin.register(PrinterAssignment)
class PrinterAssignmentAdmin(admin.ModelAdmin):
    list_display = ["printer", "employee", "date_assigned", "date_returned"]


@admin.register(ScannerAssignment)
class ScannerAssignmentAdmin(admin.ModelAdmin):
    list_display = ["scanner", "employee", "date_assigned", "date_returned"]
