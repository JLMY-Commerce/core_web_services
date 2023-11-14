from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/produtos/', CategoriesDetailView.as_view(), name='categoria'),
]
