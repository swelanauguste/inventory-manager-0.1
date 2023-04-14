from django.db import models
from django.urls import reverse
from employees.models import Employee
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
    date_assigned = models.DateTimeField(auto_now_add=True, null=True)
    date_returned = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("computer-assignment-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.computer} assigned to {self.employee}"


class PrinterAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now_add=True)
    date_returned = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.printer} assigned to {self.employee}"


class ScannerAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now_add=True)
    date_returned = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.scanner} assigned to {self.employee}"

# class ItemAssignment(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
#     date_assigned = models.DateField(auto_now_add=True)
#     date_returned = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.scanner} assigned to {self.employee}"
