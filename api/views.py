from datetime import datetime

from rest_framework import generics

from api.models import City, Shop, Street
from api.serializers import (
    CitySerializer,
    StreetSerializer,
    ShopSerializer
)


class CityAPI(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetAPI(generics.ListAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class ShopAPI(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_queryset(self):
        queryset = Shop.objects.all()

        street = self.request.query_params.get('street')  # type: ignore
        if street is not None:
            queryset = queryset.filter(street=street)

        city = self.request.query_params.get('city')  # type: ignore
        if city is not None:
            queryset = queryset.filter(city=city)

        opened = self.request.query_params.get('opened')  # type: ignore
        if opened is not None:
            current_time = datetime.now()
            if opened == 1:
                queryset = queryset.filter(opened_at__gte=current_time, closed_at__lte=current_time)
            elif opened == 0:
                queryset = queryset.filter(opened_at__lt=current_time, closed_at__gt=current_time)

        return queryset
