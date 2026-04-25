from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),

    path("news", views.news),
    path("news/", views.news),
    path("news/<path:extra_path>", views.news),

    path("management", views.management),
    path("management/", views.management),
    path("management/<path:extra_path>", views.management),

    path("facts", views.facts),
    path("facts/", views.facts),
    path("facts/<path:extra_path>", views.facts),

    path("contacts", views.contacts),
    path("contacts/", views.contacts),
    path("contacts/<path:extra_path>", views.contacts),
]