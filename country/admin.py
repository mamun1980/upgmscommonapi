from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Upazila)
admin.site.register(Union)
admin.site.register(Word)

class VillageAdmin(admin.ModelAdmin):
    list_display = ('__str__','name','population', 'village_code',)

    list_filter = ['word',]

    # search_fields = ['union', 'name',]

admin.site.register(Village, VillageAdmin)
