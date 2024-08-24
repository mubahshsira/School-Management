from . import views
from django.urls import path

urlpatterns = [
    path("", views.school_list, name="school_list"),
    path("create/", views.school_create, name="school_create"),
    path("<int:id>/update/", views.school_update, name="school_update"),
    path("<int:id>/delete/", views.school_delete, name="school_delete"),
]