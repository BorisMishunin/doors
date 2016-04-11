from web_api.serializers import GoodsImagesSerializer, GoodsSerializer, GoodsColorsSerializer, ActionsSerializer
from web.models import GoodsColors, GoodsImages, Goods
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

class GoodsImagesList(generics.ListCreateAPIView):
    def get_queryset(self):
        color_pk = self.kwargs.get('color_pk')
        if not color_pk:
            return GoodsImages.objects.all()
        return GoodsImages.objects.filter(goodcolor_id = color_pk)

    serializer_class = GoodsImagesSerializer

class GoodsImagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoodsImages.objects.all()
    serializer_class = GoodsImagesSerializer

class ActionsDetail(generics.ListCreateAPIView):
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer
