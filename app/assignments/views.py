from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import (
    ComputerAssignmentCreateForm,
    ComputerUnAssignmentCreateForm,
    PrinterAssignmentCreateForm,
    PrinterUnAssignmentCreateForm,
)
from .models import Computer, ComputerAssignment, Printer, PrinterAssignment


class PrinterAssignmentListView(LoginRequiredMixin, ListView):
    model = PrinterAssignment


class PrinterAssignmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PrinterAssignment
    form_class = PrinterAssignmentCreateForm
    success_url = reverse_lazy("printer-list")
    success_message = "%(printer)s was assigned to %(employee)s successfully"
    template_name = "assignments/assign_printer_form.html"

    def get_initial(self):
        return {"printer": self.kwargs["pk"]}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["printer_name"] = Printer.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        self.object = form.save()
        printer_pk = self.object.printer.id
        form.instance.printer = Printer.objects.get(pk=printer_pk)
        return super().form_valid(form)


class PrinterUnAssignmentCreateView(
    LoginRequiredMixin, SuccessMessageMixin, CreateView
):
    model = PrinterAssignment
    form_class = PrinterUnAssignmentCreateForm
    success_url = reverse_lazy("printer-list")
    success_message = "%(printer)s was unassigned"
    template_name = "assignments/unassign_printer_form.html"

    def get_initial(self):
        return {
            "printer": self.kwargs["pk"],
            "employee": "",
            "date_returned": now,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["printer_name"] = Printer.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        self.object = form.save()
        printer_pk = self.object.printer.id
        form.instance.Printer = Printer.objects.get(pk=printer_pk)
        return super().form_valid(form)


class PrinterAssignmentDetailView(LoginRequiredMixin, DetailView):
    model = PrinterAssignment


class ComputerAssignmentListView(LoginRequiredMixin, ListView):
    model = PrinterAssignment


class ComputerAssignmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ComputerAssignment
    form_class = ComputerAssignmentCreateForm
    success_url = reverse_lazy("computer-list")
    success_message = "%(computer)s was assigned to %(employee)s successfully"
    template_name = "assignments/assign_computer_form.html"

    def get_initial(self):
        return {"computer": self.kwargs["pk"]}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["computer_name"] = Computer.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        self.object = form.save()
        computer_pk = self.object.computer.id
        form.instance.computer = Computer.objects.get(pk=computer_pk)
        return super().form_valid(form)


class ComputerUnAssignmentCreateView(
    LoginRequiredMixin, SuccessMessageMixin, CreateView
):
    model = ComputerAssignment
    form_class = ComputerUnAssignmentCreateForm
    success_url = reverse_lazy("computer-list")
    success_message = "%(computer)s was unassigned"
    template_name = "assignments/unassign_computer_form.html"

    def get_initial(self):
        return {
            "computer": self.kwargs["pk"],
            "employee": "",
            "date_returned": now,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["computer_name"] = Computer.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        self.object = form.save()
        computer_pk = self.object.computer.id
        form.instance.computer = Computer.objects.get(pk=computer_pk)
        return super().form_valid(form)


class ComputerAssignmentDetailView(LoginRequiredMixin, DetailView):
    model = ComputerAssignment


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
