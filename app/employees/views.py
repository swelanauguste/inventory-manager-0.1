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

from .models import Department, Employee


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department

    def get_queryset(self):
        query = self.request.GET.get("departments")
        if query:
            return Department.objects.filter(
                Q(name__icontains=query) | Q(ext__icontains=query)
            ).distinct()
        else:
            return Department.objects.all()


class DepartmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Department
    fields = "__all__"
    success_url = reverse_lazy("department-list")
    success_message = "%(name)s was created successfully"


class DepartmentUpdateView(SuccessMessageMixin, UpdateView):
    model = Department
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class DepartmentDetailView(LoginRequiredMixin, DetailView):
    model = Employee


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
