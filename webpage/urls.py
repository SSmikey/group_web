from django.urls import path
from . import views


urlpatterns = [
    path("", views.indexPage, name="index"),
    path("details/", views.detailsPage, name="details"),
    path("browse/", views.browsePage, name="browse"),
    path("profile/", views.profilePage, name="profile"),
    path("streams/", views.streamsPage , name="streams")
]