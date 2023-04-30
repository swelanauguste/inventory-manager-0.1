from django.contrib import admin

from .models import (
    Computer,
    ComputerModel,
    Manufacturer,
    Printer,
    PrinterModel,
    Scanner,
    ScannerModel,
    PrinterRemark
)

admin.site.register(Manufacturer)


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ["serial_number", "model", "supplier"]

@admin.register(PrinterRemark)
class PrinterRemarkAdmin(admin.ModelAdmin):
    list_display = ["printer", "remarks",]


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ["serial_number", "model", "supplier", "pk"]


@admin.register(Scanner)
class ScannerAdmin(admin.ModelAdmin):
    list_display = ["serial_number", "model", "supplier"]


@admin.register(ComputerModel)
class ComputerModelAdmin(admin.ModelAdmin):
    list_display = ["name", "manufacturer", "processor", "memory", "storage"]


@admin.register(PrinterModel)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ["name", "manufacturer", "colour_printer"]


@admin.register(ScannerModel)
class ScannerModelAdmin(admin.ModelAdmin):
    list_display = ["name", "manufacturer"]
