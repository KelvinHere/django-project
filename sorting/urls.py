from django.urls import path
from sorting import views

urlpatterns = [
    path("sorting/", views.sorting, name="sorting")
]