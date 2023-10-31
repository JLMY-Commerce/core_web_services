from django.urls import path, include
from .views import *

urlpatterns = [
    path("produto/", include("web.views.products.urls"), name="products")
]
