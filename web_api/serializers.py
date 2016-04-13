from django.contrib.auth.models import User, Group
from web.models import GoodsColors, GoodsImages, Goods, Countries, GoodsProperties, Values
from sales.models import Actions
from rest_framework import serializers

class ValuesSerializer(serializers.ModelSerializer):
    good_property = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model = Values
        fields = '__all__'

class GoodsPropertiesSerializer(serializers.ModelSerializer):
    property = serializers.ReadOnlyField(source='value.good_property.name')
    value = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='value'
     )
    class Meta:
        model = GoodsProperties
        fields = '__all__'

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
    goods_properties = GoodsPropertiesSerializer(many=True)
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
