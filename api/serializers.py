from rest_framework import serializers
from api.models import City, Shop, Street


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
