from django.db import models


class Item(models.Model):
    COLOR_CHOICES = (
        ('RED', 'red'),
        ('GREEN', 'green'),
        ('BLUE', 'blue'),
        ('WHITE', 'white'),
        ('BLACK', 'black'),
    )

    name = models.CharField(primary_key=True, max_length=60)
    price = models.FloatField()
    is_archived = models.BooleanField(default=False)
    color = models.CharField(max_length=5, choices=COLOR_CHOICES, default='RED')

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)

    def __str__(self):
        return f'{id} {self.name}'