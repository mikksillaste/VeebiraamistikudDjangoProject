from django.shortcuts import render

from django.http import HttpResponse
from . import models


def index(request):
    h22led = models.H22led.objects.all()
    context = {'h22led': h22led}
    return render(request, 'index.html', context)
