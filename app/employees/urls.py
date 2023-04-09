from django.urls import path

from .views import (
    DepartmentCreateView,
    DepartmentDetailView,
    DepartmentListView,
    DepartmentUpdateView,
    EmployeeCreateView,
    EmployeeDetailView,
    EmployeeListView,
    EmployeeUpdateView,
)

urlpatterns = [
    path(
        "",
        EmployeeListView.as_view(),
        name="employee-list",
    ),
    path(
        "employee/add/",
        EmployeeCreateView.as_view(),
        name="employee-create",
    ),
    path(
        "employee/edit/<int:pk>/",
        EmployeeUpdateView.as_view(),
        name="employee-update",
    ),
    path(
        "employee/detail/<int:pk>/",
        EmployeeDetailView.as_view(),
        name="employee-detail",
    ),
    path(
        "department",
        DepartmentListView.as_view(),
        name="department-list",
    ),
    path(
        "department/add/",
        DepartmentCreateView.as_view(),
        name="department-create",
    ),
    path(
        "department/edit/<int:pk>/",
        DepartmentUpdateView.as_view(),
        name="department-update",
    ),
    path(
        "department/detail/<int:pk>/",
        DepartmentDetailView.as_view(),
        name="department-detail",
    ),
]
