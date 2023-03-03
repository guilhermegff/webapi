from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .models import Location
from .models import Establishment
from .serializers import UserSerializer
from .serializers import LocationSerializer
from .serializers import EstablishmentSerializer


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            user = self.get_object(pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EstablishmentList(APIView):
    def get(self, request):
        establishments = Establishment.objects.all()
        serializer = EstablishmentSerializer(establishments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EstablishmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstablishmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Establishment.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            establishment = self.get_object(pk)
            serializer = EstablishmentSerializer(establishment)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        establishment = self.get_object(pk)
        serializer = EstablishmentSerializer(establishment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        establishment = self.get_object(pk)
        establishment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LocationList(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
