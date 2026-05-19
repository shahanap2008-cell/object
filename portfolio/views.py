from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render


def home(request):
    profile = {
        "name": "Your Name",
        "role": "Python Django Developer",
        "email": "hello@example.com",
        "location": "India",
        "summary": (
            "I build clean, responsive web applications with Django, HTML, CSS, "
            "and JavaScript."
        ),
    }

    skills = ["Python", "Django", "HTML", "CSS", "JavaScript", "SQLite"]

    projects = [
        {
            "title": "Portfolio Website",
            "description": "A responsive personal website powered by Django templates.",
            "tags": ["Django", "Frontend", "Responsive"],
        },
        {
            "title": "Task Manager",
            "description": "A simple CRUD app concept for tracking everyday work.",
            "tags": ["Python", "SQLite", "CRUD"],
        },
        {
            "title": "Weather Dashboard",
            "description": "A JavaScript dashboard concept for displaying live weather data.",
            "tags": ["JavaScript", "API", "UI"],
        },
    ]

    return render(
        request,
        "portfolio/home.html",
        {"profile": profile, "skills": skills, "projects": projects},
    )


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "portfolio/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Welcome back.")
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "portfolio/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")
