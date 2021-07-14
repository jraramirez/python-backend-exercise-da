from rest_framework import serializers

from .models import Item, Vehicle

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'price', 'is_archived', 'color')

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'name', 'manufacturer')