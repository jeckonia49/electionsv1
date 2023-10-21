from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UserCreateApiView.as_view()),
    path("login/", views.UserLoginApiView.as_view()),
    path("logout/", views.UserLogoutApiView.as_view()),
    path("profile/", views.UserApiView.as_view()),
]
