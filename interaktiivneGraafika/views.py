# Lisa import get_object_or_404
from django.shortcuts import render, get_object_or_404
# Lisa import HttpResponse
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


# Andmebaasis vastava id'ga inimesele häääle lisamine
def h22leta(request, inimese_id):
    inimene = get_object_or_404(models.H22led, pk=inimese_id)
    inimene.h22lte_arv += 1
    inimene.save()
    return HttpResponse()
