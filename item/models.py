from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(
        max_length=20,
    )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

