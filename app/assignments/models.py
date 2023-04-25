from django.db import models
from django.urls import reverse
from employees.models import Department, Employee, UnitSection
from equipment.models import Computer, Printer, Scanner
from stock.models import Item


class ComputerAssignment(models.Model):
    computer = models.ForeignKey(
        Computer, on_delete=models.CASCADE, related_name="computer_assignments"
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="computer_assignments",
    )
    dept = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    unit_section = models.ForeignKey(
        UnitSection,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    date_assigned = models.DateTimeField(auto_now_add=True, null=True)
    date_returned = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("computer-assignment-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.computer} assigned to {self.employee}"


class PrinterAssignment(models.Model):
    printer = models.ForeignKey(
        Printer,
        on_delete=models.CASCADE,
        related_name="printer_assignments",
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="printer_assignments",
    )
    dept = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="printer_assignments",
    )
    unit_section = models.ForeignKey(
        UnitSection,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="printer_assignments",
    )

    date_assigned = models.DateField(auto_now_add=True)
    date_returned = models.DateField(null=True, blank=True)

    @property
    def get_printer_assignment(self):
        if self.employee or self.dept or self.unit_section:
            return True
        return False

    def __str__(self):
        return f"{self.printer} assigned to {self.employee}"


class ScannerAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dept = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    unit_section = models.ForeignKey(
        UnitSection,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now_add=True)
    date_returned = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.scanner} assigned to {self.employee}"
