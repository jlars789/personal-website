from django.db import models    #type: ignore

class Visits(models.Model):
    visits = models.IntegerField()
