from django.shortcuts import render
from .models import Car
from .serializers import CarSerializer
from rest_framework import generics
# Create your views here.


class CarListApiView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarCreateApiView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarEditApiView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_url_kwarg = 'pk'

class CarDeleteApiView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer