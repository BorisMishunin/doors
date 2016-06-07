from django.contrib import admin
from .models import DoorSize, Accessories, AccessoriesGroupPrise, AccessoriesGroups, DoorType, GoodsAccessories, TypeAccessories, DoorTypeAccessoriesValues

class DoorTypeAccessoriesInlines(admin.StackedInline):
    model = DoorTypeAccessoriesValues
    extra = 3

class DoorTypeAdmin(admin.ModelAdmin):
    inlines = [DoorTypeAccessoriesInlines,]

admin.site.register(DoorSize)
admin.site.register(Accessories)
admin.site.register(AccessoriesGroupPrise)
admin.site.register(TypeAccessories)
admin.site.register(AccessoriesGroups)
admin.site.register(DoorType, DoorTypeAdmin)
admin.site.register(GoodsAccessories)



