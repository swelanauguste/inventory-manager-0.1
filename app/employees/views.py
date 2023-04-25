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

from .models import Section, Employee


class SectionListView(LoginRequiredMixin, ListView):
    model = Section

    def get_queryset(self):
        query = self.request.GET.get("sections")
        if query:
            return Section.objects.filter(
                Q(name__icontains=query) | Q(ext__icontains=query)
            ).distinct()
        else:
            return Section.objects.all()


class SectionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Section
    fields = "__all__"
    success_url = reverse_lazy("section-list")
    success_message = "%(name)s was created successfully"


class SectionUpdateView(SuccessMessageMixin, UpdateView):
    model = Section
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class SectionDetailView(LoginRequiredMixin, DetailView):
    model = Section


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("employees")
        if query:
            return Employee.objects.filter(
                Q(name__icontains=query) | Q(ext__icontains=query) | Q(department__name__icontains=query)
            ).distinct()
        else:
            return Employee.objects.all()


class EmployeeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Employee
    fields = "__all__"
    success_url = reverse_lazy("employee-list")
    success_message = "%(name)s was created successfully"


class EmployeeUpdateView(SuccessMessageMixin, UpdateView):
    model = Employee
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
