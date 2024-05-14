from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignupForm, AuthenticationForm


def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    next_url = request.GET.get("next")
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect("accounts:login")
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("accounts:login")
