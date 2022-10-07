from django.contrib import admin
from django.urls import path, include
from . import views as parent_site_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# from django.urls import reverse_lazy
# app_name = "parent_site"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", parent_site_views.contact, name="contact"),
    # apps
    path("portfolio/", include("portfolio.urls", namespace="portfolio")),
    path("users/", include("users.urls", namespace="users")),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
    ),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
