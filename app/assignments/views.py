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

from .forms import ComputerAssignmentCreateForm, ComputerUnAssignmentCreateForm
from .models import ComputerAssignment, Computer


class ComputerAssignmentListView(LoginRequiredMixin, ListView):
    model = ComputerAssignment


class ComputerAssignmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ComputerAssignment
    form_class = ComputerAssignmentCreateForm
    success_url = reverse_lazy("computer-list")
    success_message = "%(computer)s was assigned to %(employee)s successfully"

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

    def get_initial(self):
        return {
            "computer": self.kwargs["pk"],
            "employee": "",
            "date_returned": now,
        }

    def form_valid(self, form):
        self.object = form.save()
        computer_pk = self.object.computer.id
        form.instance.computer = Computer.objects.get(pk=computer_pk)
        return super().form_valid(form)


class ComputerAssignmentDetailView(LoginRequiredMixin, DetailView):
    model = ComputerAssignment


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
