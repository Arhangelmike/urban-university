from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(default=0, decimal_places=3, max_digits=5)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(default=0, decimal_places=3, max_digits=5)
    size = models.DecimalField(default=0, decimal_places=3, max_digits=5)
    description = models.CharField(default='Game', max_length=100000000)
    age_limited = models.BooleanField(False)
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title
