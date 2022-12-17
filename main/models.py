from django.db import models    #type: ignore

class Visit(models.Model):
    visits = models.IntegerField()

    def __str__(self):
        return str(self.visits)
