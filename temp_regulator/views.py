from django.shortcuts import render
from datetime import datetime
from .models import Temperature


def home(request):
    temperature = 20.0
    context = {
        'title': 'Home page',
        'date': datetime.now(),
        'temp': temperature,
    }

    if request.GET.get('add-btn'):
        temperature += 1

    return render(request, 'temp_regulator/home.html', context=context)


def modes(request):
    context = {
        'title': 'Modes page'
    }
    return render(request, 'temp_regulator/modes.html', context=context)


def heating_plan(request):
    context = {
        'title': 'Heating plan'
    }
    return render(request, 'temp_regulator/heating_plan.html', context=context)
