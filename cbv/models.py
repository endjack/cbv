from django.db import models
from django.contrib import admin

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)


admin.site.register(Pessoa)