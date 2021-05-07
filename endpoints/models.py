from django.db import models


class Item(models.Model):

    name = models.CharField(max_length=60)
    price = models.FloatField()
    is_archived = models.BooleanField(default=False)


    def __str__(self):
        return self.name