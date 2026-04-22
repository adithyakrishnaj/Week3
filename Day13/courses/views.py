from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    context = {
        'title': 'Welcome to Klaw Courses',
        'user_name': 'Adithya',
        'courses': ['Python', 'Django', 'HTML', 'CSS']
    }
    return render(request, 'courses/course_list.html', context)

def detail_view(request, name):
    return HttpResponse(f"Course Name: {name}")