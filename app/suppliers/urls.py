from django.urls import path

from .views import (
    SupplierCreateView,
    SupplierDetailView,
    SupplierListView,
    SupplierUpdateView,
)

urlpatterns = [
    path("suppliers/", SupplierListView.as_view(), name="supplier-list"),
    path("supplier/add/", SupplierCreateView.as_view(), name="supplier-create"),
    path(
        "supplier/edit/<int:pk>/",
        SupplierUpdateView.as_view(),
        name="supplier-update",
    ),
    path(
        "supplier/detail/<int:pk>/",
        SupplierDetailView.as_view(),
        name="supplier-detail",
    ),
]
