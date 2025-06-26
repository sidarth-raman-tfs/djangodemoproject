from rest_framework import serializers
from .models import ItemOne

class ItemOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOne
        fields = ['id', 'name', 'description']