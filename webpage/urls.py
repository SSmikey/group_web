from django.urls import path
from . import views


urlpatterns = [
    path("", views.indexPage, name="index"),
    path("login/", views.loginPage, name="login"),
    path("registers/", views.registersPage, name="registers"),
    path("profile/", views.profilePage, name="profile"),
    path("streams/", views.streamsPage , name="streams")
]