from django.db import models

# Create your models here.


class Dessert(models.Model):
    name = models.CharField(max_length=30)
    calories = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    protein = models.FloatField()

    def __str__(self):
        return self.name
