from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters


from .models import *
from .serializers import *


class SuvModelViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer

class SuvAPI(APIView):
    def get(self, request, son):
        suv = Suv.objects.get(id=son)
        serializer = SuvSerializer(suv)
        return Response(serializer.data)


class MijozModelViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ["ism", "tel"]

class MijozAPI(APIView):
    def get(self, request, son):
        mijoz = Mijoz.objects.get(id=son)
        serializer = MijozSerializer(mijoz)
        return Response(serializer.data)


class BuyurtmaAPI(APIView):
    def get(self, request):
        buyurtma = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtma, many=True)
        return Response(serializer.data)

    def post(self, request):
        buyurta = request.data
        serializer = BuyurtmaSerializer(data=buyurta)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AdminlarAPI(APIView):
    def get(self, request):
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)

class AdminAPI(APIView):
    def get(self, request, son):
        admin = Admin.objects.get(id=son)
        serializer = AdminSerializer(admin)
        return Response(serializer.data)

class HaydovchilarAPI(AdminAPI):
    def get(self, request):
        haydovchi = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchi, many=True)
        return Response(serializer.data)

class HaydovchiAPI(AdminAPI):
    def get(self, request, son):
        haydovchi = Haydovchi.objects.get(id=son)
        serializer = HaydovchiSerializer(haydovchi)
        return Response(serializer.data)
