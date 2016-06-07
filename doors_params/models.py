from django.db import models
from web.models import Goods

# Create your models here.

class DoorType(models.Model):
    name = models.CharField('Название', max_length=150)

    class Meta:
        verbose_name = 'Тип дверей'
        verbose_name_plural = 'Типы дверей'

    def __str__(self):
        return self.name


class TypeAccessories(models.Model):
    name = models.CharField('Название', max_length=150)

    class Meta:
        verbose_name = 'Аксессуары типов дверей'
        verbose_name_plural = 'Аксессуары типов дверей'

    def __str__(self):
        return self.name

class DoorTypeAccessoriesValues(models.Model):
    door_type = models.ForeignKey(DoorType, verbose_name='Тип двери')
    accessory = models.ForeignKey(TypeAccessories, verbose_name='Аксессуар')
    value = models.CharField('Значение', max_length=150)

    class Meta:
        verbose_name = 'Значение аксессуаров типов дверей'
        verbose_name_plural = 'Значения аксессуаров типов дверей'

    def __str__(self):
        return self.name

class DoorSize(models.Model):
    size = models.CharField('Размер', max_length=150)

    class Meta:
        verbose_name = 'Размер дверей'
        verbose_name_plural = 'Размеры дверей'

    def __str__(self):
        return self.size

class Accessories(models.Model):
    name = models.CharField('Название', max_length=150)

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'

    def __str__(self):
        return self.name

class AccessoriesGroups(models.Model):
    name = models.CharField('Название', max_length=150)

    class Meta:
        verbose_name = 'Группа аксессуаров'
        verbose_name_plural = 'Группы аксессуаров'

    def __str__(self):
        return self.name

class AccessoriesGroupPrise(models.Model):
    #group = models.ForeignKey(AccessoriesGroups, verbose_name='Группа аксессуаров')
    size = models.ForeignKey(DoorSize, verbose_name="Размер")
    accessory = models.ForeignKey(Accessories, verbose_name='Аксессуар')
    price = models.IntegerField('Цена')

    class Meta:
        verbose_name = 'Цены аксессуаров'
        verbose_name_plural = 'Цены аксессуаров'

    def __str__(self):
        return self.group.name + '-' + self.accessory.name

class GoodsAccessories(models.Model):
    good = models.ForeignKey(Goods, verbose_name='Товар')
    door_type = models.ForeignKey(DoorType, verbose_name='Тип двери')
    size = models.ForeignKey(DoorSize, verbose_name='Размер')
    group = models.ForeignKey(AccessoriesGroups, verbose_name='Группа аксессуаров')

    class Meta:
        verbose_name = 'Aксессуар дверей'
        verbose_name_plural = 'Aксессуары дверей'

    def __str__(self):
        return self.good.name + '-' + self.group.name

