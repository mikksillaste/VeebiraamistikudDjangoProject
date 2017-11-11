from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Impordi JsonResponse
from django.http import JsonResponse


def index(request):
    h22led = models.H22led.objects.all()
    context = {'h22led': h22led}
    return render(request, 'index.html', context)


# Andmete saamine JSON'i kujul
def get_data(request):
    h22led = models.H22led.objects.all().values('inimese_nimi', 'h22lte_arv')
    return JsonResponse(list(h22led), safe=False)