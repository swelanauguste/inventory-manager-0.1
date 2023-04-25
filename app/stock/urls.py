from django.urls import path

from .views import AddItemCreateView  # ReportListView,; StockReportView,
from .views import (
    AddItemDetailViewCreateView,
    CategoryCreateView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView,
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView,
    RemoveItemCreateView,
    RemoveItemDetailViewCreateView,
)

urlpatterns = [
    # path("report-list", ReportListView.as_view(), name="report-list"),
    # path("report-items", StockReportView.as_view(), name="report-items"),
    path("items/", ItemListView.as_view(), name="item-list"),
    path("item/create/", ItemCreateView.as_view(), name="item-create"),
    path("item/update/<int:pk>/", ItemUpdateView.as_view(), name="item-update"),
    path("item/detail/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path(
        "item-add/add/<int:pk>/",
        AddItemCreateView.as_view(),
        name="item-add",
    ),
    path(
        "item-remove/remove/<int:pk>/",
        RemoveItemCreateView.as_view(),
        name="item-remove",
    ),
    path(
        "item-add-detail-view/add/<int:pk>/",
        AddItemDetailViewCreateView.as_view(),
        name="item-add-detail-view",
    ),
    path(
        "item-remove-detail-view/remove/<int:pk>/",
        RemoveItemDetailViewCreateView.as_view(),
        name="item-remove-detail-view",
    ),
    # ----------
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("category/ad/", CategoryCreateView.as_view(), name="category-create"),
    path(
        "category/edit/<int:pk>/",
        CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "category/detail/<int:pk>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),
]
