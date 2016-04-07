from django.contrib.auth.models import User, Group
from web.models import GoodsImages, Goods
from sales.models import Actions
from rest_framework import serializers


class GoodsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImages
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    goods_images = GoodsImagesSerializer(many=True)
    class Meta:
        model = Goods
        fields = '__all__'

class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = '__all__'

