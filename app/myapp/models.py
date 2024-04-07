from django.db import models

# Create your models here.

# Report signals every time a report is made (like every individual pot hole)
class Report(models.Model):
    Address = models.CharField(max_length=100)
    date = models.DateField()
    image = models.JSONField(null=True)
    coordinates = models.CharField(max_length=100)

# For every unit (as in like an area thats of high severity, one block?)
# Has an address range, a severity score, and an array of images
class Unit(models.Model):
    severity = models.FloatField()
    images = models.JSONField(null=True)
    frequency = models.IntegerField()
    flow_count = models.IntegerField()
    address = models.CharField(max_length=100)
    radius_m = models.FloatField()