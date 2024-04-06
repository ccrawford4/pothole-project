from django.db import models

# Create your models here.

# Report signals every time a report is made (like every individual pot hole)
class Report(models.Model):
    Address = models.CharField(max_length=100)
    Date = models.DateField()
    Coordinates = models.CharField(max_length=100)
    image = models.JSONField(null=True)

# For every unit (as in like an area thats of high severity, one block?)
# Has an address range, a severity score, and an array of images
class Unit(models.Model):
    Address_range_low = models.CharField(max_length=100)
    Address_range_high = models.CharField(max_length=100)
    severity = models.FloatField()
    images = models.JSONField(null=True)
