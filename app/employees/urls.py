from django.urls import path

from .views import (
    SectionCreateView,
    SectionDetailView,
    SectionListView,
    SectionUpdateView,
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
        "section",
        SectionListView.as_view(),
        name="section-list",
    ),
    path(
        "section/add/",
        SectionCreateView.as_view(),
        name="section-create",
    ),
    path(
        "section/edit/<int:pk>/",
        SectionUpdateView.as_view(),
        name="section-update",
    ),
    path(
        "section/detail/<int:pk>/",
        SectionDetailView.as_view(),
        name="section-detail",
    ),
]
