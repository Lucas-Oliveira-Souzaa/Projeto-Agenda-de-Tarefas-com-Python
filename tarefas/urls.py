from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("add/", views.add, name="add"),
    path("toggle/<int:id>/", views.toggle, name="toggle"),
    path("delete/<int:id>/", views.delete, name="delete"),
]