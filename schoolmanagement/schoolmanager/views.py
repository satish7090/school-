from django.shortcuts import render
from .models import schoollist
from rest_framework import generics, parsers, permissions, renderers, viewsets, filters
from .serializers import schoollistSerializers 


# Create your views here.
class schoolview(viewsets.ModelViewSet):
    serializer_class= schoollistSerializers
    queryset= schoollist.objects.all()