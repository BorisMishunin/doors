from web_api.serializers import GoodsImagesSerializer, GoodsSerializer, ActionsSerializer
from web.models import GoodsImages, Goods
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

class GoodsImagesList(generics.ListCreateAPIView):
    def get_queryset(self):
        pk = self.kwargs.get('good_pk')
        if not pk:
            return GoodsImages.objects.all()
        return GoodsImages.objects.filter(id = pk)
    
    serializer_class = GoodsImagesSerializer

class GoodsImagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoodsImages.objects.all()
    serializer_class = GoodsImagesSerializer

class ActionsDetail(generics.ListCreateAPIView):
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer