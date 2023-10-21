from django.urls import path, include



urlpatterns = [
    path("", include("apis.accounts.urls"))
]
