from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Upazila)

class UnionAdmin(admin.ModelAdmin):
    list_display = ('name', 'union_code',)

admin.site.register(Union, UnionAdmin)

class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'word_code',)

    # def word_by_order(self, obj):
    #     return int(obj.union_word_no)
    # word_by_order.admin_order_field = '-union_word_no'

admin.site.register(Word, WordAdmin)


class VillageAdmin(admin.ModelAdmin):
    list_display = ('name','name_bangla', 'village_code',)

    list_filter = ['word',]

admin.site.register(Village, VillageAdmin)
