from django.db import models

# Create your models here.

class Country(models.Model):

    name = models.CharField(max_length=50, blank=False)
    code = models.CharField(max_length=10, blank=False)
    confirmed = models.PositiveIntegerField()
    recovered = models.PositiveIntegerField()
    critical = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    