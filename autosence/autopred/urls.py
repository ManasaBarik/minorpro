from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),          # root URL → index.html
    path("about/", views.about, name="about"),
    path("details/", views.details, name="details"),
    path("predict/", views.predict, name="predict"),
    path("contact/", views.contact, name="contact"),

    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
]
