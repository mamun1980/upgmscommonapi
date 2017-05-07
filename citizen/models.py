from django.db import models

GENDER = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('B', 'Both')
)

# Create your models here.

class Citizen(models.Model):
    citizen_id = models.CharField(max_length=25, blank=False, null=False, db_index=True, primary_key=True)
    name_bangla = models.CharField(max_length=50, blank=False, null=False, db_index=True)
    name = models.CharField(max_length=50, blank=False, null=False, db_index=True)
    nid = models.CharField(max_length=30, blank=False, null=False, db_index=True, unique=True)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER)
    # Address in NID card
    village = models.ForeignKey('country.Village', blank=True, null=True, on_delete=models.SET_NULL)
    word = models.ForeignKey('country.Word', blank=True, null=True, on_delete=models.SET_NULL)
    union = models.ForeignKey('country.Union', blank=True, null=True, on_delete=models.SET_NULL)

    post_office = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    post_code = models.CharField(max_length=10, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    spouse_name = models.CharField(max_length=50, blank=True, null=True, db_index=True)


    @property
    def get_bangla_name(self):
        return self.name_bangla

    def __str__(self):
        return self.name
