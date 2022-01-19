from email.policy import default
from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    cost = models.TextField(max_length=300, default="")
    # description = models.TextField(max_length=300, default="")
    quantity = models.TextField(max_length=300, default="")
    image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        pass
