from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def index(request):
    return render(request, 'index.html')

class games(TemplateView):
    template_name = 'games.html'

class cart(TemplateView):
    template_name = 'cart.html'


class platform(TemplateView):
    template_name = 'platform.html'
