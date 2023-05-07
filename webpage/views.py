from django.shortcuts import render
from .days import DateCalculator

def index(request):
    days = DateCalculator((2023,6,10),weekmask="1111110",holidays=["2023-06-02"]).calculate()
    context = {
        'days': days
    }
    return render(request, 'index.html', context=context)