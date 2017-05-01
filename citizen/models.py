from django.db import models
from citizen.models import *

GENDER = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('B', 'Both')
)

# Create your models here.

class Citizen(models.Model):
    name_bangla = models.CharField(max_length=100, blank=False, null=False, db_index=True)
    name_english = models.CharField(max_length=100, blank=False, null=False, db_index=True)
    citizen_uid = models.CharField(max_length=100, blank=False, null=False, db_index=True)
    nid = models.CharField(max_length=30, blank=False, null=False, db_index=True)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER)
    village = models.ForeignKey('Village', blank=True, null=True, on_delete=models.SET_NULL)
    union = models.ForeignKey('Union', blank=True, null=True, on_delete=models.SET_NULL)
    district = models.ForeignKey('District', blank=True, null=True, on_delete=models.SET_NULL)


    @property
    def get_bangla_name(self):
        return self.name_bangla

    def __str__(self):
        return self.name_english
