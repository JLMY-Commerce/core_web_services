# Create your views here.
from django.shortcuts import render


def docs_page_view(request):
    if request.method == "GET":
        return render(request, "home.html")


def docs_product_view(request):
    if request.method == "GET":
        return render(request, "product.html")


def docs_office_view(request):
    if request.method == "GET":
        return render(request, "office.html")


def docs_life_cycle_view(request):
    if request.method == "GET":
        return render(request, "life-cycle.html")


def docs_process_home_view(request):
    if request.method == "GET":
        return render(request, "process.html")
