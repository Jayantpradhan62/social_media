from django.urls import path

from . import views

urlpatterns = [
    path("create-account",views.RegisterView.as_view(),name="create-account"),
    path("login",views.UserLoginView.as_view(),name="user-login"),
    path("logout",views.LogoutView,name="user-logout"),
    path("reset-password/",views.ResetPasswordView.as_view(),name="reset-password"),
    path("reset-password-done/",views.ResetPasswordDoneView.as_view(),name="reset-password-done"),
    path("reset/<uidb64>/<token>/",views.ResetPasswordConfirmView.as_view(),name="reset-password-confirm"),
    path("reset-password-complete/",views.ResetPasswordCompleteView.as_view(),name="reset-password-complete"),
]
