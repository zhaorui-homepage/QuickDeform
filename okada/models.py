from django.db import models

# Create your models here.
# class earthquake(models.Model):
#
#     Etitle = models.CharField(max_length=50)
#     Edatetime = models.CharField(max_length=50)
#     Latitude = models.FloatField()
#     Longitude = models.FloatField()
#     Moment = models.FloatField()
#     Magnitude = models.FloatField()
#     Depth = models.FloatField()
#     Strike = models.FloatField()
#     Dip = models.FloatField()
#     Rake = models.FloatField()

class parameters(models.Model):

    Etitle = models.CharField(max_length=100)
    Edatetime = models.CharField(max_length=50)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Magnitude = models.FloatField()
    Depth = models.FloatField()
    Strike1 = models.FloatField()
    Dip1 = models.FloatField()
    Rake1 = models.FloatField()
    Strike2 = models.FloatField()
    Dip2 = models.FloatField()
    Rake2 = models.FloatField()
