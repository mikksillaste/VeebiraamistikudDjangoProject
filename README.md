# VeebiraamistikudDjangoProject
See projekt on Veebiraamistike 15.11 Interaktiivse graafilise andmelehestiku sidumine Djangoga seminariks
1. Alustuseks laadige alla algne projekt siit https://github.com/mikksillaste/VeebiraamistikudDjangoProjectAlgus
2. Käivitage alla laetud projekt mis loob veebiserveri: python manage.py runserver
3. Minge brauseris aadressile: localhost:8000. Laetud leht peaks välja nägema selline:
![alt text](Screenshots/1.png)
5. Avage views.py ja lisage
   ```python
   # Impordi JsonResponse
   from django.http import JsonResponse
   
   # Andmete saamine JSON'i kujul
   def get_data(request):
       h22led = models.H22led.objects.all().values('inimese_nimi', 'h22lte_arv')
       return JsonResponse(list(h22led), safe=False)
   ```
6. Avage interaktiivneGraafika/urls.py lisage
   ```python
   urlpatterns = [
       url(r'^$', views.index, name='index'),
       # Lisa endpoint
       url(r'^api/data$', views.get_data, name='api-data'),
   ]
   ```
6. Minge brauseris aadressile: localhost:8000/api/data. Laetud lehel peaks olema andmed json'i kujul