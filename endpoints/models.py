from django.db import models


class Item(models.Model):

    name = models.CharField(max_length=60)
    price = models.FloatField()


    def __str__(self):
        return self.name