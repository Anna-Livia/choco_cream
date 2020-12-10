from django.db import models

# Create your models here.
class Spending(models.Model):
    amount = models.FloatField(default=0)
