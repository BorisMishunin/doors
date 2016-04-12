from django.contrib.auth.models import User, Group
from web.models import GoodsColors, GoodsImages, Goods, Countries
from sales.models import Actions
from rest_framework import serializers


class GoodsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImages
        fields = '__all__'

class GoodsColorsSerializer(serializers.ModelSerializer):
    color = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
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

class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = '__all__'

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'
