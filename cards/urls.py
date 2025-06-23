from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", views.card_list, name="card_list"),
    path("add/", views.add_card, name="add_card"),
    path("delete/<int:card_id>/", views.delete_card, name="delete_card"),
    path("edit/<int:card_id>/", views.edit_card, name="edit_card"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.register, name="register"),


]