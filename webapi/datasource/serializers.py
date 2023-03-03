from rest_framework import serializers
from .models import User
from .models import Location
from .models import Establishment


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    status = serializers.CharField(default='offline')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class LocationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    review = serializers.IntegerField(required=True)
    type = serializers.CharField(required=True)

    def create(self, validated_data):
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.review = validated_data.get('review', instance.review)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance


class EstablishmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    review = serializers.CharField(required=True)
    type = serializers.CharField(required=True)
    about = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    address = serializers.CharField(required=True)

    def create(self, validated_data):
        return Establishment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.review = validated_data.get('review', instance.review)
        instance.type = validated_data.get('type', instance.type)
        instance.about = validated_data.get('about', instance.about)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
