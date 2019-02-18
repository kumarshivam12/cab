from django.urls import path
from .import views

app_name = "bookcab1"

urlpatterns = [
    path("", views.app_page, name="app_page"),
]