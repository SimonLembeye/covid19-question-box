from django.shortcuts import render

from project.settings import DEBUG


def index(request):
    return render(request, 'frontend/index.html', {
        'debug': DEBUG
    })