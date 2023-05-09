# from io import BytesIO

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
# from django.http import HttpResponse
# from django.template.loader import get_template
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.timezone import now
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)
# from xhtml2pdf import pisa

from .forms import ItemUpdateForm
from .models import Category, ChangeItem, Item


# class ReportListView(ListView):
#     model = ChangeItem
#     template_name = "stock/report_list.html"

#     def get_queryset(self):
#         # Get the current month and year
#         current_month = timezone.now().month
#         current_year = timezone.now().year

#         # Filter the model by month and year
#         queryset = ChangeItem.objects.filter(
#             created_at__year=current_year, created_at__month=current_month
#         )

#         return queryset


# class StockReportView(View):
#     def get(self, request):
#         items = Item.objects.all()
#         context = {"items": items}
#         template = get_template("stock/stock_report.html")
#         html = template.render(context)
#         pdf = self.generate_pdf(html)
        # response = HttpResponse(pdf, content_type="application/pdf")
#         response["Content-Disposition"] = 'filename="stock_report.pdf"'
#         return response

#     def generate_pdf(self, html):
#         pdf_file = BytesIO()
#         pisa.CreatePDF(
#             BytesIO(html.encode("utf-8")),
#             pdf_file,
#             encoding="utf-8",
#             show_error_as_pdf=True,
#         )
#         return pdf_file.getvalue()


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
    # paginate_by = 100

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
    form_class = ItemUpdateForm

    success_url = reverse_lazy("item-list")
    success_message = "%(name)s was created successfully"


class ItemUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Item
    form_class = ItemUpdateForm
    success_message = "%(name)s was updated successfully"


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


class AddItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ChangeItem
    fields = [
        "item",
        "qty",
    ]
    success_url = reverse_lazy("item-list")
    success_message = "%(qty)s %(item)s(s) added  to stock"
    template_name = "stock/add_item_form.html"

    def get_initial(self):
        return {"item": self.kwargs["pk"]}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class RemoveItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ChangeItem
    fields = ["item", "qty", "section", "employee"]
    success_url = reverse_lazy("item-list")
    success_message = "%(qty)s %(item)s(s) removed from stock"
    template_name = "stock/remove_item_form.html"

    def get_initial(self):
        return {"item": self.kwargs["pk"]}

    def form_valid(self, form):
        form.instance.qty = -abs(form.instance.qty)
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class AddItemDetailViewCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ChangeItem
    fields = [
        "item",
        "qty",
    ]
    success_message = "%(qty)s %(item)s(s) added to stock"
    template_name = "stock/add_item_form.html"
    success_url = reverse_lazy("item-list")

    def get_initial(self):
        return {"item": self.kwargs["pk"]}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class RemoveItemDetailViewCreateView(
    LoginRequiredMixin, SuccessMessageMixin, CreateView
):
    model = ChangeItem
    fields = ["item", "qty", "section", "employee"]
    success_url = reverse_lazy("item-list")
    success_message = "%(qty)s %(item)s(s) removed from stock"
    template_name = "stock/remove_item_form.html"

    def get_initial(self):
        return {"item": self.kwargs["pk"]}

    def form_valid(self, form):
        form.instance.qty = -abs(form.instance.qty)
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
