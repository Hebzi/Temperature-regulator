from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account for {username} has been created! You can log in now.")
            return redirect('temp_regulator:home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', context={'form': form})
