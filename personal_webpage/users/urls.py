from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name = "users"
urlpatterns = [
    path("register/", user_views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(success_url=reverse_lazy('users:password_reset_done'))
      #   ,template_name="users/password_reset.html"
        ,
        name="password-reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(

            template_name="users/password_reset_done.html"
        ),
        name="password-reset-done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('users:password_reset_complete'),
             template_name="users/password_reset_confirm.html"
        ),
        name="password-reset-confirm"),
#     path(
#         'reset_password/',
#         auth_views.PasswordResetView.as_view(success_url=reverse_lazy('users:password_reset_done')),
#         name='reset_password'
#     ),
#     path(
#         'reset_password_sent/',
#         auth_views.PasswordResetDoneView.as_view(),
#         name='password_reset_done'
#     ),
#     path(
#         'reset/<uidb64>/<token>/',
#         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('users:password_reset_complete')),
#         name='password_reset_confirm'
#     ),
#     path(
#         'reset_password_complete/',
#         auth_views.PasswordResetCompleteView.as_view(),
#         name='password_reset_complete'
#     ),

    path("profile/", user_views.profile, name="profile"),
]
# path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),