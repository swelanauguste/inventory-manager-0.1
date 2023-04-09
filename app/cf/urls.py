from assignments.views import HomeView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("profiles/", include("users.urls")),
    path("accounts/", include("allauth.urls")),
    path("computer-assignment/", include("assignments.urls")),
    path("employees/", include("employees.urls")),
    path("equipment/", include("equipment.urls")),
    path("stock/", include("stock.urls")),
    path("suppliers/", include("suppliers.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
