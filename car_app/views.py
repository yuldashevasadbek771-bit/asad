from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import phone
from .serializers import CarSerializer


class PhoneListApiView(APIView):
    def get(self, request):
        phones = phone.objects.all()
        serializer = CarSerializer(phones, many=True)
        return Response(serializer.data)

class PhoneCreateApiView(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PhoneEditApiView(APIView):

    def get_object(self, pk):
        try:
            return phone.objects.get(pk=pk)
        except phone.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        obj = self.get_object(pk)
        serializer = CarSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = CarSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



class PhoneDeleteApiView(generics.DestroyAPIView):
    queryset = phone.objects.all()
    serializer_class = CarSerializer



class PhoneDetailApiView(generics.RetrieveAPIView):
    queryset = phone.objects.all()
    serializer_class = CarSerializer



class PhoneMixedApiView(APIView):

    def get_object(self, pk):
        try:
            return phone.objects.get(pk=pk)
        except phone.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = CarSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response({"xabar": "Telefon o‘chirildi"})

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = CarSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar": "Telefon to‘liq yangilandi"})
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        obj = self.get_object(pk)
        serializer = CarSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar": "Telefon qisman yangilandi"})
        return Response(serializer.errors, status=400)
