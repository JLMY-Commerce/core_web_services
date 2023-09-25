
from django.urls import path
from .views import *

urlpatterns = [
    path("", docs_page_view, name="docs/home"),
    path("produto", docs_product_view, name="docs/product"),
    path("papeis", docs_office_view, name="docs/office"),

    # Processos
    path("processos", docs_process_home_view, name="docs/process"),
    path("processos/ciclodevida", docs_life_cycle_view, name="docs/lifecycle")
]
