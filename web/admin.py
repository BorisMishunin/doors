from django.contrib import admin
from web.models import GoodsImages, Goods
from web.widgets import ColorPickerWidget
# Register your models here.

class GoodsInlines(admin.StackedInline):
    model = GoodsImages
    extra = 3

class GoodsAdmin(admin.ModelAdmin):
    inlines = [GoodsInlines, ]

admin.site.register(GoodsImages)
admin.site.register(Goods, GoodsAdmin)

