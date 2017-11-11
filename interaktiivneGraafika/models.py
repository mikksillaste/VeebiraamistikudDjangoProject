from django.db import models


class H22led(models.Model):
    inimese_nimi = models.CharField(max_length=200)
    h22lte_arv = models.IntegerField(default=0)
