from django.urls import path

from .views import (
    ComputerAssignmentCreateView,
    ComputerAssignmentDetailView,
    ComputerAssignmentListView,
    ComputerUnAssignmentCreateView,
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
]
