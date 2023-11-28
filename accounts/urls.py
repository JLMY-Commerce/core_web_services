from django.urls import path, include
from .views import *

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("criar/", UserCreateView.as_view(), name="create-account"),
    path('vendedor/<str:username>/', VendedorDetailView.as_view(), name='vendedor_detail'),
]
