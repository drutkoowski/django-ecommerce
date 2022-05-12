from django.shortcuts import render, redirect
from .forms import RegistrationForm
from accounts.models import Account
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = email.split("@", 1)[0]
            user = Account(first_name=first_name, last_name=last_name, email=email,
                           password=password, username=username)
            user.phone_number = phone_number
            user.save()
            messages.success(request, "Registration completed!")
            return redirect("register")
    else:
        form = RegistrationForm()
    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')
