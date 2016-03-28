from django.contrib import admin
from web.models import Colors, GoodsImages, Goods, GoodsColors
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
    list_display = ('name', 'color')
    ordering = ('name', )
    search_fields = ('name',)
    fieldsets = ((None, {'fields': ('name', 'color')}),)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'color':
            kwargs['widget'] = ColorPickerWidget
        return super(ColorsAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Colors, ColorsAdmin)
admin.site.register(GoodsImages)
admin.site.register(GoodsColors,GoodsColorsAdmin)
admin.site.register(Goods, GoodsAdmin)

