from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Temperature


def home(request):
    context = {
        'title': 'Home page',
        'date': datetime.now(),
        'temperature': Temperature.objects.get(pk=1),
    }

    return render(request, 'temp_regulator/home.html', context=context)


@login_required
def modes(request):
    context = {
        'title': 'Modes page',
    }
    return render(request, 'temp_regulator/modes.html', context=context)


@login_required
def heating_plan(request):
    context = {
        'title': 'Heating plan'
    }
    return render(request, 'temp_regulator/heating_plan.html', context=context)


@login_required
def party_mode(request):
    pm = Temperature.objects.get(pk=1)
    pm.temp = 20.0
    pm.save()

    return render(request, 'temp_regulator/party_mode.html')


@login_required
def vacation_mode(request):
    vm = Temperature.objects.get(pk=1)
    vm.temp = 10.0
    vm.save()

    return render(request, 'temp_regulator/vacation_mode.html')


@login_required
def conditioning_mode(request):
    cm = Temperature.objects.get(pk=1)
    cm.temp = 16.0
    cm.save()

    return render(request, 'temp_regulator/conditioning_mode.html')
