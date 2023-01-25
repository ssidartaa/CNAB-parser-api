from django.contrib import admin
from django.urls import path, include
from drf_spectacular import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("transactions.urls")),
    path("docs/", views.SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/swagger-ui/",
        views.SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "docs/redoc/",
        views.SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
