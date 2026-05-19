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
