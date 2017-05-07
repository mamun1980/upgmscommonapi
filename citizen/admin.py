from django.contrib import admin
from .models import Citizen
# Register your models here.

class CitizenAdmin(admin.ModelAdmin):
    list_display = ('name_bangla', 'name', 'nid', 'citizen_id', 'village',)
    search_fields = ['name_bangla', 'name',]
    list_filter = ['union','village',]

admin.site.register(Citizen, CitizenAdmin)
