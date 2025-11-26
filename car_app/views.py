from gc import get_objects
from logging import exception

from django.core.serializers import serialize
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Car
from .serializers import CarSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


#class BookListApiView(generics.ListAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
class CarListApiView(APIView):
    def get(self, request):
        cars=Car.objects.all()
        serializer=CarSerializer(cars,many=True)
        return Response(serializer.data)

#class BookCreateApiView(generics.CreateAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
class CarCreateApiView(APIView):
    def post(self,request):
        try:
            serializer=CarSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"status":"Nimadur xatto ketdi"})
        except:
            return Response({"status":"Nimadur xatto ketdi"})

#class BookEditApiView(generics.UpdateAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
class CarEditApiView(APIView):
    def put(self,request,pk):
        cars=Car.objects.get(id=pk)
        serializer=CarSerializer(cars,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"boldi yangilandi","yangilangani":serializer.data})
        else:
            return  Response({"javob":"Edit qilinmadi"})

    def patch(self,request,pk):
        cars=Car.objects.get(id=pk)
        serializer=CarSerializer(cars,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"boldi yangilandi","yangilangani":serializer.data})
        else:
            return  Response({"javob":"Edit qilinmadi"})


#class BookDeleteApiView(generics.DestroyAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
class CarDeleteApiView(APIView):
    def delete(self, request,pk):
        cars=Car.objects.get(id=pk)
        cars.delete()
        return Response({"xabar":"car ochirildi"})



#class BookDetailApiView(generics.RetrieveAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
class CarDetailApiView(APIView):
    def get(self,request,pk):
        try:
            cars=Car.objects.get(id=pk)
            serializer=CarSerializer(cars)
            return Response(serializer.data)
        except:
            return Response({"xabar":"bunday id-li car yuq mavjud emas"})

#class BookMixedApiView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer

class CarMixedApiView(APIView):
    def get(self,request,pk):
        try:
            cars=Car.objects.get(id=pk)
            serializer=CarSerializer(cars)
            return Response(serializer.data)
        except:
            return Response({"xabar":"bunday id-li kitob yuq mavjud emas"})

    def put(self,request,pk):
        cars=Car.objects.get(id=pk)
        serializer=CarSerializer(cars,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"boldi yangilandi","yangilangani":serializer.data})
        else:
            return  Response({"javob":"Edit qilinmadi"})

    def patch(self,request,pk):
        cars=Car.objects.get(id=pk)
        serializer=CarSerializer(cars,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar": "boldi yangilandi", "yangilangani": serializer.data})
        else:
            return Response({"javob": "Edit qilinmadi"})


def delete(self, request, pk):
            cars = Car.objects.get(id=pk)
            cars.delete()
            return Response({"xabar": "car"})
