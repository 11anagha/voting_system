from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_in/", auth_views.LoginView.as_view(template_name="user/sign_in.html"), name="sign_in"),
    path("sign_out/", views.sign_out, name="sign_out")
]