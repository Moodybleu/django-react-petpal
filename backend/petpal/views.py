from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PetpalSerializer
from .models import Petpal

# Create your views here.

class PetpalView(viewsets.ModelViewSet):
    serializer_class = PetpalSerializer
    queryset = Petpal.objects.all()