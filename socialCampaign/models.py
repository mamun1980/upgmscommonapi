from django.db import models

# Create your models here.
class CampaignType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    

    def __str__(self):
        return self.name

    def __unicode__(self):
        return 

class Campaign(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    camp_type = models.ForeignKey('CampaignType', null=True, on_delete=models.SET_NULL)
    tag_officer = models.CharField(max_length=50, blank=True, null=True)
    order_latter = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return 

    def __unicode__(self):
        return 
