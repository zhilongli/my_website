from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    about = "I am currently a senior in computer science and mechanical engineering at Cornell University.\
    I love learning about anything related to these two subjects; recently I also started \
    reading about history. This website, built using Django in Python, is a personal project to \
    have an understanding of web development."
    context = {'about_me': about}
    return render(request, 'index.html', context=context)


def travels(request):
    return render(request, 'travels.html')

def projects(request):
    return HttpResponse("Here is the list of projects that I have worked on, \
    either for school coursework or for personal interest. Click on each one \
    of them for more information.")

def classes(request):
    return HttpResponse("Here are the classes that I have taken in my three years \
    at Cornell.")
