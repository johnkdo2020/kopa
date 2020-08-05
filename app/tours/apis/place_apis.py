from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, DestroyAPIView

from tours.models import Place
from tours.serializers import PlaceSerializer, PlaceDetailSerializer


class PlaceAPIView(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDetailAPIView(RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceDetailSerializer

class PlaceCreateAPIView(CreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDeleteAPIView(DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
