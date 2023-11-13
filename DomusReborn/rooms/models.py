from django.db import models
from django.shortcuts import render, get_object_or_404


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)  # Pour des descriptions plus longues
    plan = models.ImageField(upload_to='room_plans/')  # Stocke le chemin de l'image et gère l'upload

    def __str__(self):
        return self.name
