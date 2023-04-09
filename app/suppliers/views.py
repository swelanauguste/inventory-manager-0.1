from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .models import Supplier


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    paginate_by = 10
    

    def get_queryset(self):
        query = self.request.GET.get("suppliers")
        if query:
            return Supplier.objects.filter(
                Q(name__icontains=query)
                | Q(address__icontains=query)
                | Q(phone__icontains=query)
                | Q(email__icontains=query)
            ).distinct()
        else:
            return Supplier.objects.all()


class SupplierCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    fields = "__all__"
    success_url = reverse_lazy("supplier-list")
    success_message = "%(name)s was created successfully"


class SupplierUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
