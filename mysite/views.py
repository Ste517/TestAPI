from django.http import HttpResponse
from .days import DateCalculator

def index(request):
    return HttpResponse("Hello, world!")

def schoolcountdown(request):
    result = DateCalculator((2023,6,10),weekmask="1111110",holidays=["2023-06-10"]).calculate()
    return HttpResponse(result, content_type="text/plain")
