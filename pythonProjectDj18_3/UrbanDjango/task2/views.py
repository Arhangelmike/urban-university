from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def class_template(request):
    return render(request, 'class_template.html')

class index(TemplateView):
    template_name = 'index.html'

class func_template(TemplateView):
    template_name = 'func_template.html'