from django.urls import path

from .views import (
    CategoryCreateView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView,
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView,
    ReceiveItemCreateView,
    RemoveItemCreateView,
)

urlpatterns = [
    path("items/", ItemListView.as_view(), name="item-list"),
    path("item/create/", ItemCreateView.as_view(), name="item-create"),
    path("item/update/<int:pk>/", ItemUpdateView.as_view(), name="item-update"),
    path("item/detail/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path(
        "item-remove/remove/<int:pk>/",
        RemoveItemCreateView.as_view(),
        name="item-remove",
    ),
    path(
        "item-receive/receive/<int:pk>/",
        ReceiveItemCreateView.as_view(),
        name="item-receive",
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
