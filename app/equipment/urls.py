from django.urls import path

from .views import (
    ComputerCreateView,
    ComputerDetailView,
    ComputerListView,
    ComputerModelCreateView,
    ComputerModelDetailView,
    ComputerModelListView,
    ComputerModelUpdateView,
    ComputerUpdateView,
    ManufacturerCreateView,
    ManufacturerDetailView,
    ManufacturerListView,
    ManufacturerUpdateView,
    PrinterCreateView,
    PrinterDetailView,
    PrinterListView,
    PrinterModelCreateView,
    PrinterModelDetailView,
    PrinterModelListView,
    PrinterModelUpdateView,
    PrinterUpdateView,
    ScannerModelCreateView,
    ScannerModelDetailView,
    ScannerModelListView,
    ScannerModelUpdateView,
)

urlpatterns = [
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path(
        "manufacturer/add/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturer/edit/<int:pk>/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturer/detail/<int:pk>/",
        ManufacturerDetailView.as_view(),
        name="manufacturer-detail",
    ),
    path("printers/", PrinterListView.as_view(), name="printer-list"),
    path(
        "printer/add/",
        PrinterCreateView.as_view(),
        name="printer-create",
    ),
    path(
        "printer/edit/<int:pk>/",
        PrinterUpdateView.as_view(),
        name="printer-update",
    ),
    path(
        "printer/detail/<int:pk>/",
        PrinterDetailView.as_view(),
        name="printer-detail",
    ),
    # ---------------------
    path("printer-models/", PrinterModelListView.as_view(), name="printer-model-list"),
    path(
        "printer-model/add/",
        PrinterModelCreateView.as_view(),
        name="printer-model-create",
    ),
    path(
        "printer-model/edit/<int:pk>/",
        PrinterModelUpdateView.as_view(),
        name="printer-model-update",
    ),
    path(
        "printer-model/detail/<int:pk>/",
        PrinterModelDetailView.as_view(),
        name="printer-model-detail",
    ),
    # ---------------------
    path("computers/", ComputerListView.as_view(), name="computer-list"),
    path(
        "computer/add/",
        ComputerCreateView.as_view(),
        name="computer-create",
    ),
    path(
        "computer/edit/<int:pk>/",
        ComputerUpdateView.as_view(),
        name="computer-update",
    ),
    path(
        "computer/detail/<int:pk>/",
        ComputerDetailView.as_view(),
        name="computer-detail",
    ),
    # ---------------------
    path(
        "computer-models/", ComputerModelListView.as_view(), name="computer-model-list"
    ),
    path(
        "computer-model/add/",
        ComputerModelCreateView.as_view(),
        name="computer-model-create",
    ),
    path(
        "computer-model/edit/<int:pk>/",
        ComputerModelUpdateView.as_view(),
        name="computer-model-update",
    ),
    path(
        "computer-model/detail/<int:pk>/",
        ComputerModelDetailView.as_view(),
        name="computer-model-detail",
    ),
    path("computers/", ComputerListView.as_view(), name="computer-list"),
    path(
        "computer/add/",
        ComputerCreateView.as_view(),
        name="computer-create",
    ),
    path(
        "computer/edit/<int:pk>/",
        ComputerUpdateView.as_view(),
        name="computer-update",
    ),
    path(
        "computer/detail/<int:pk>/",
        ComputerDetailView.as_view(),
        name="computer-detail",
    ),
    # ---------------------
    path("scanner-models/", ScannerModelListView.as_view(), name="scanner-model-list"),
    path(
        "scanner-model/add/",
        ScannerModelCreateView.as_view(),
        name="scanner-model-create",
    ),
    path(
        "scanner-model/edit/<int:pk>/",
        ScannerModelUpdateView.as_view(),
        name="scanner-model-update",
    ),
    path(
        "scanner-model/detail/<int:pk>/",
        ScannerModelDetailView.as_view(),
        name="scanner-model-detail",
    ),
]
