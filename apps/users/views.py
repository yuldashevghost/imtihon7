import datetime

from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import LoginForm, UserRegistrationForm




@login_required
def logout_view(request):
    messages.info(request, f"{request.user.username} user successfulley loged out")
    logout(request)
    return redirect("liberity:home")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
            if user is not None:
                login(request, user)
                messages.success(request, "user succesfully loged in")
                return redirect("liberity:home")
            else:
                messages.warning(request, "User not found")
                return redirect("login-page")
        else:
            return render(request, "users/login.html", {"form": form})

    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


def register_view(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User successfully registered")
            return redirect('login-page')
        else:
            return render(request, "users/register.html", {"form": form})
    else:
        return render(request, "users/register.html", {"form": form})