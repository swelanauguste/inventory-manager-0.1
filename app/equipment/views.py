from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import (
    Computer,
    ComputerModel,
    Manufacturer,
    Printer,
    PrinterModel,
    ScannerModel,
    Supplier,
)

from .forms import AddPrinterModelForm


class PrinterModelListView(LoginRequiredMixin, ListView):
    model = PrinterModel


class PrinterModelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PrinterModel
    form_class = AddPrinterModelForm
    success_url = reverse_lazy("printer-model-list")
    success_message = "%(name)s was created successfully"


class PrinterModelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PrinterModel
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class PrinterModelDetailView(LoginRequiredMixin, DetailView):
    model = PrinterModel


class PrinterListView(LoginRequiredMixin, ListView):
    model = Printer


class PrinterCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Printer
    fields = "__all__"
    success_url = reverse_lazy("printer-list")
    success_message = "%(serial_number)s was created successfully"


class PrinterUpdateView(SuccessMessageMixin, UpdateView):
    model = Printer
    fields = "__all__"
    success_message = "%(serial_number)s was updated successfully"


class PrinterDetailView(LoginRequiredMixin, DetailView):
    model = Printer


class ScannerModelListView(LoginRequiredMixin, ListView):
    model = ScannerModel


class ScannerModelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ScannerModel
    fields = "__all__"
    success_url = reverse_lazy("scanner-model-list")
    success_message = "%(name)s was created successfully"


class ScannerModelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ScannerModel
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class ScannerModelDetailView(LoginRequiredMixin, DetailView):
    model = ScannerModel


class ComputerModelListView(LoginRequiredMixin, ListView):
    model = ComputerModel


class ComputerModelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ComputerModel
    fields = "__all__"
    success_url = reverse_lazy("computer-model-list")
    success_message = "%(name)s was created successfully"


class ComputerModelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ComputerModel
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class ComputerModelDetailView(LoginRequiredMixin, DetailView):
    model = ComputerModel


class ComputerListView(LoginRequiredMixin, ListView):
    model = Computer
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get("computers")
        if query:
            return Computer.objects.filter(
                Q(serial_number__icontains=query)
                | Q(model__name__icontains=query)
                | Q(model__manufacturer__name__icontains=query)
                | Q(supplier__name__icontains=query)
            ).distinct()
        else:
            return Computer.objects.all()


class ComputerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Computer
    fields = "__all__"
    success_url = reverse_lazy("computer-list")
    success_message = "%(serial_number)s was created successfully"


class ComputerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Computer
    fields = "__all__"
    success_message = "%(serial_number)s was updated successfully"


class ComputerDetailView(LoginRequiredMixin, DetailView):
    model = Computer


class ManufacturerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("manufacturer-list")
    success_message = "%(name)s was created successfully"


class ManufacturerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class ManufacturerDetailView(LoginRequiredMixin, DetailView):
    model = Manufacturer


class ManufacturerListView(LoginRequiredMixin, ListView):
    model = Manufacturer
