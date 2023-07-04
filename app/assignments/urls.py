from django.urls import path

from .views import (
    ComputerAssignmentCreateView,
    ComputerAssignmentDetailView,
    ComputerAssignmentListView,
    ComputerUnAssignmentCreateView,
    PrinterAssignmentCreateView,
    PrinterAssignmentDetailView,
    PrinterAssignmentListView,
    PrinterUnAssignmentUpdateView,
)

urlpatterns = [
    path(
        "computer-assignments/",
        ComputerAssignmentListView.as_view(),
        name="computer-assignment-list",
    ),
    path(
        "computer-assignment/create/<int:pk>/",
        ComputerAssignmentCreateView.as_view(),
        name="computer-assignment-create",
    ),
    path(
        "computer-assignment/update/<int:pk>/",
        ComputerUnAssignmentCreateView.as_view(),
        name="computer-unassignment-create",
    ),
    path(
        "computer-assignment/detail/<int:pk>/",
        ComputerAssignmentDetailView.as_view(),
        name="computer-assignment-detail",
    ),
    # #########
    path(
        "printer-assignments/",
        PrinterAssignmentListView.as_view(),
        name="printer-assignment-list",
    ),
    path(
        "printer-assignment/create/<int:pk>/",
        PrinterAssignmentCreateView.as_view(),
        name="printer-assignment-create",
    ),
    path(
        "printer-assignment/update/<int:pk>/",
        PrinterUnAssignmentUpdateView.as_view(),
        name="printer-unassignment",
    ),
    path(
        "printer-assignment/detail/<int:pk>/",
        PrinterAssignmentDetailView.as_view(),
        name="printer-assignment-detail",
    ),
]
