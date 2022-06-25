from django.db import models


# Create your models here.
class Goods(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=20)
    cost = models.TextField(max_length=20)

    def __str__(self):
        return f'{self.name}:{self.cost}'
