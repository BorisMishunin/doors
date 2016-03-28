from web_api.serializers import GoodsImagesSerializer, GoodsSerializer, GoodsColorsSerializer
from web.models import GoodsColors, GoodsImages, Goods
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

class GoodsImagesList(generics.ListCreateAPIView):
    queryset = GoodsImages.objects.all()
    serializer_class = GoodsImagesSerializer

class GoodsImagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoodsImages.objects.all()
    serializer_class = GoodsImagesSerializer