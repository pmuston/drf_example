from django.shortcuts import render
from desserts.models import Dessert
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DessertSerializer


class DessertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dessert.objects.all().order_by('name')
    serializer_class = DessertSerializer
