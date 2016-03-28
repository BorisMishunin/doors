from django.contrib.auth.models import User, Group
from web.models import GoodsColors, GoodsImages, Goods
from rest_framework import serializers


class GoodsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImages
        fields = '__all__'

class GoodsColorsSerializer(serializers.ModelSerializer):
    color = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='color'
     )
    goods_images = GoodsImagesSerializer(many=True)
    class Meta:
        model = GoodsColors
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    goods_colors = GoodsColorsSerializer(many=True)
    class Meta:
        model = Goods
        fields = '__all__'

