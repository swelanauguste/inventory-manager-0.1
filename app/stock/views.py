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

from .models import Category, Item, ReceiveItem, RemoveItem


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("category-list")
    success_message = "%(name)s was created successfully"


class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("items")
        if query:
            return Item.objects.filter(
                Q(name__icontains=query)
                | Q(category__name__icontains=query)
                | Q(supplier__name__icontains=query)
            ).distinct()
        else:
            return Item.objects.all()


class ItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Item
    fields = "__all__"
    success_url = reverse_lazy("item-list")
    success_message = "%(name)s was created successfully"


class ItemUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Item
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


class ReceiveItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ReceiveItem
    fields = ["item", "qty"]
    success_url = reverse_lazy("item-list")
    success_message = "%(qty)s %(item)s(s) were added"

    def get_initial(self):
        return {"item": self.kwargs["pk"]}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class RemoveItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = RemoveItem
    fields = ["item", "qty"]
    success_url = reverse_lazy("item-list")
    success_message = "%(qty)s %(item)s(s) were removed"

    def get_initial(self):
        return {"item": self.kwargs["pk"]}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
