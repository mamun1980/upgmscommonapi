from django.db import models

# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    division_code = models.CharField(max_length=2, blank=False, null=False)
    
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    district_code = models.CharField(max_length=4, blank=False, null=False)
    population = models.PositiveIntegerField(blank=True, null=True)
    division = models.ForeignKey('Division', related_name='division',null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

class Upazila(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    upazila_code = models.CharField(max_length=6, blank=False, null=False)
    population = models.PositiveIntegerField(blank=True, null=True)
    division = models.ForeignKey('Division', related_name='bivag', null=True, on_delete=models.SET_NULL)
    district = models.ForeignKey('District', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

class Union(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    union_code = models.CharField(max_length=8, blank=False, null=False)
    population = models.PositiveIntegerField(blank=True, null=True)
    district = models.ForeignKey('District', null=True, on_delete=models.SET_NULL)
    upazila = models.ForeignKey('Upazila', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

class Word(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    union_word_no = models.CharField(max_length=6, blank=False, null=False)
    word_code = models.CharField(max_length=10, blank=False, null=False)
    population = models.PositiveIntegerField(blank=True, null=True)
    upazila = models.ForeignKey('Upazila', null=True, on_delete=models.SET_NULL)
    union = models.ForeignKey('Union', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name

class Village(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    alias_name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    village_code = models.CharField(max_length=12, blank=False, null=False)
    population = models.PositiveIntegerField(blank=True, null=True)
    upazila = models.ForeignKey('Upazila', null=True, on_delete=models.SET_NULL)
    union = models.ForeignKey('Union', null=True, on_delete=models.SET_NULL)
    word = models.ForeignKey('Word', null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return self.name