from django.contrib import admin
from web.models import Colors, GoodsImages, Goods, GoodsColors, Countries, TypesOfGoods, Values, GoodsProperties, Properties
from web.widgets import ColorPickerWidget
# Register your models here.

class GoodsColorsInline(admin.StackedInline):
    model = GoodsImages
    extra = 3

class GoodsColorsAdmin(admin.ModelAdmin):
    inlines = [GoodsColorsInline,]

class GoodsInlines(admin.StackedInline):
    model = GoodsColors
    extra = 3

class GoodsAdmin(admin.ModelAdmin):
    inlines = [GoodsInlines, ]

class ColorsAdmin(admin.ModelAdmin):
    ordering = ('name', )
    search_fields = ('name',)


admin.site.register(Colors, ColorsAdmin)
admin.site.register(GoodsImages)
admin.site.register(GoodsColors,GoodsColorsAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Countries)
admin.site.register(TypesOfGoods)
admin.site.register(Values)
admin.site.register(GoodsProperties)
admin.site.register(Properties)