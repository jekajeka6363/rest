from django.db import models

class Restorant(models.Model):
    name_restorant = models.CharField(max_length=20)
    rescription_restorant = models.CharField(max_length=20)
    rating_restorant = models.IntegerField()


    def __str__(self):
        return self.name_restorant
