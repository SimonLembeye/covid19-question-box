from django.shortcuts import render

from project.settings import DEBUG, MODE


def index(request):
    return render(request, 'frontend/index.html', {
        'debug': DEBUG,
        'mode': MODE
    })