from django.shortcuts import render, redirect
from datetime import datetime
from .models import Temperature
from .forms import ModesForm
from django.contrib import messages


def home(request):
    context = {
        'title': 'Home page',
        'date': datetime.now(),
        'temperature': Temperature.objects.get(pk=1),
    }

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


# def party_mode(request):
#     if request.method == 'POST':
#         form = ModesForm(request.POST)
#         if form.is_valid():
#             btn = form.cleaned_data.get("btn")
#             messages.success(request, f"Temperature changed successful.")
#             return redirect('home')
#     else:
#         form = ModesForm()
#     return render(request, 'temp_regulator/modes.html')
