from django.db import models
from django.urls import reverse
from suppliers.models import Supplier


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("manufacturer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class ComputerModel(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, null=True, blank=True
    )
    processor = models.CharField(max_length=255, blank=True, default="i5")
    memory = models.CharField(max_length=255, blank=True, default='8')
    storage = models.CharField(max_length=255, blank=True, default='500')

    def get_absolute_url(self):
        return reverse("computer-model-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f" {self.manufacturer} {self.name}"


class PrinterModel(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, null=True, blank=True
    )
    # print_technology = models.ForeignKey(
    #     PrintTechnology, on_delete=models.CASCADE, null=True, blank=True
    # )
    colour_printer = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ScannerModel(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    scan_technology = models.CharField(max_length=255, blank=True)
    scan_resolution = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


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
    )

    def get_absolute_url(self):
        return reverse("computer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.serial_number} {self.model}"


class Printer(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    model = models.ForeignKey(PrinterModel, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse("printer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.serial_number} {self.model}"


class Scanner(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    model = models.ForeignKey(ScannerModel, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse("scanner-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.serial_number} {self.model}"
