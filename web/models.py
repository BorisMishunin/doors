from _json import make_encoder

from django.db import models



# Create your models here.

TYPES_OF_GOODS = ((0, 'Двери'), (1, 'Акссесуары'))

class Goods(models.Model):
    article = models.CharField('Артикул',max_length=50)
    name = models.CharField('Название', max_length=150)
    desc = models.TextField('Описание',null=True, blank=True)
    type = models.IntegerField('Тип товара', choices=TYPES_OF_GOODS, default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '%s - %s' % (self.article, self.name)


class Colors(models.Model):
    name = models.CharField('Цвет', max_length=150)
    color = models.CharField('RGB', max_length=7)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name

class GoodsColors(models.Model):
    good = models.ForeignKey(Goods, verbose_name='Товар', related_name='goods_colors')
    color = models.ForeignKey(Colors, verbose_name='Цвет', null = True, blank = True)

    class Meta:
        verbose_name = 'Товар с цветом'
        verbose_name_plural = 'Товары с цветами'

    def __str__(self):
        return '%s - %s' % (str(self.good), self.color.name)

class GoodsImages(models.Model):
    goodcolor = models.ForeignKey(GoodsColors, verbose_name='Товар', related_name='goods_images')
    image = models.ImageField('Фото', upload_to='goods_foto')

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товара'

    def __str__(self):
        return str(self.goodcolor)

