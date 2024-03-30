from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name=''),

    path("register", views.register, name='register'),

    path('my-login', views.login, name='my-login'),

    path("logout", views.logout, name="logout"),

    path("dashboard", views.dashboard, name="dashboard"),

    path("new-record", views.create_record, name="new-record"),

    path("update-record/<int:pk>", views.update_record, name="update-record"),

    path("view-record/<int:pk>", views.singular_record, name="view-record"),

    path("delete-record/<int:pk>", views.delete_record, name="delete-record"),
]