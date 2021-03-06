from web_api.serializers import  GoodsSerializer, \
    GoodsColorsSerializer, ActionsSerializer, CountriesSerializer, ValuesSerializer, GoodsPropertiesSerializer, PropertiesSerializer
from web.models import GoodsColors, Goods, Countries, Values, GoodsProperties, Properties
from sales.models import Actions
from rest_framework import generics
from rest_framework import filters


class GoodsList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Goods.objects.all()
    serializer_class = GoodsSerializer

class GoodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

class GoodsColorsList(generics.ListCreateAPIView):
    queryset = GoodsColors.objects.all()
    serializer_class = GoodsColorsSerializer

class GoodsColorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoodsColors.objects.all()
    serializer_class = GoodsColorsSerializer

class ActionsList(generics.ListCreateAPIView):
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer

class CountriesList(generics.ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer

class ValuesList(generics.ListCreateAPIView):
    queryset = Values.objects.all()
    serializer_class = ValuesSerializer

class GoodsPropertiesList(generics.ListCreateAPIView):
    queryset = GoodsProperties.objects.all()
    serializer_class = GoodsPropertiesSerializer

class PropertiesList(generics.ListCreateAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer