from django.urls import path
from . import views


urlpatterns = [
    path("", views.indexPage, name="index"),
    path("browse/", views.browsePage, name="browse"),
    path("details/", views.detailsPage, name="details"),
    path("profile/", views.profilePage, name="profile"),
    path("streams/", views.streamsPage, name="streams")
]
