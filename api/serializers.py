from rest_framework import serializers
from desserts.models import Dessert


class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = ['id', 'name', "calories", "fat", "carbs", "protein"]
