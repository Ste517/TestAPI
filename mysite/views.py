from django.http import HttpResponse
from django.template import loader
from .days import DateCalculator

def index(request):
    template = loader.get_template("templates/index.html")
    return HttpResponse(template.render(request))

def schoolcountdown(request):
    result = DateCalculator((2023,6,10),weekmask="1111110",holidays=["2023-06-10"]).calculate()
    return HttpResponse(result, content_type="text/plain")
