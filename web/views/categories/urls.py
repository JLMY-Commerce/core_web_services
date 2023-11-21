from django.urls import path
from .views import CategoriesDetailView

urlpatterns = [
    path(
        '<int:pk>/produtos/',
        CategoriesDetailView.as_view(),
        name='categoria'
    ),
]
