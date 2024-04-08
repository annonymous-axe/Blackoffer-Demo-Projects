from django.urls import path 

from . import views

urlpatterns = [

    path("", views.index, name="index"),

    path("login", views.login, name="login"),

    path("register", views.register, name="register"),

    path("profile", views.profile, name="profile"),

    path("update_profile", views.update_profile, name="update_profile"),

    path("logout", views.logout, name="logout"),

    path("register", views.register, name="doctors"),

    path("diabetes_prediction", views.diabetes_prediction, name="diabetes_prediction"),

    path("diabetes_result", views.diabetes_result, name="diabetes_result"),

    path("download/result", views.download, name="download"), 
    
]