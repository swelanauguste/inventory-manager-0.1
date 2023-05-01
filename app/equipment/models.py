from django.conf import settings
from django.db import models
from django.urls import reverse
from stock.models import Item
from suppliers.models import Supplier

User = settings.AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse("manufacturer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name.upper()


class ComputerModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, null=True, blank=True
    )
    processor = models.CharField(max_length=255, blank=True, default="i5")
    memory = models.CharField(max_length=255, blank=True, default="8")
    storage = models.CharField(max_length=255, blank=True, default="500")

    def get_absolute_url(self):
        return reverse("computer-model-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name.title()}"


class Computer(models.Model):
    serial_number = models.CharField(max_length=255, unique=True, db_index=True)
    model = models.ForeignKey(
        ComputerModel, on_delete=models.CASCADE, related_name="computer"
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="computers",
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        return reverse("computer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.serial_number}"


class MonitorModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, null=True, blank=True
    )
    size = models.CharField(max_length=255, blank=True, default='22"')

    def get_absolute_url(self):
        return reverse("monitor-model-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f" {self.manufacturer} {self.name}"


class Monitor(models.Model):
    serial_number = models.CharField(max_length=255, unique=True, db_index=True)
    model = models.ForeignKey(
        MonitorModel, on_delete=models.CASCADE, related_name="monitor", blank=True
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="monitors",
        null=True,
    )

    def get_absolute_url(self):
        return reverse("monitor-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.serial_number} {self.model}"


class PrinterModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, null=True, blank=True
    )
    ink = models.ManyToManyField(Item)
    # print_technology = models.ForeignKey(
    #     PrintTechnology, on_delete=models.CASCADE, null=True, blank=True
    # )
    colour_printer = models.BooleanField(default=False)

    def __str__(self):
        return self.name.title()


class Printer(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    model = models.ForeignKey(PrinterModel, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("printer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.serial_number} {self.model}"


class PrinterRemark(models.Model):
    printer = models.ForeignKey(
        Printer, on_delete=models.CASCADE, related_name="printers"
    )
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"{self.printer} remarks"


class ScannerModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    manufacturer = models.CharField(max_length=255)
    scan_technology = models.CharField(max_length=255, blank=True)
    scan_resolution = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Scanner(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    model = models.ForeignKey(ScannerModel, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse("scanner-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.serial_number} {self.model}"
