from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home/home.html"


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
