from django.urls import path, include
from .views import *

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("criar/", UserCreateView.as_view(), name="registry")
]
