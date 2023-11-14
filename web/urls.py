from django.urls import path, include

urlpatterns = [
    path("produto/", include("web.views.products.urls"), name="products"),
    path("categorias/", include("web.views.categories.urls"), name="categories"),
    path("vendas/", include("web.views.vendas.urls"), name="vendas"),
]
