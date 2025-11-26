from django.db import models

# Create your models here.


class phone(models.Model):
    model = models.CharField(max_length=120)
    description = models.CharField(max_length=15)
    price = models.IntegerField()
    stock = models.IntegerField()
    catergorya = models.CharField(max_length=120)
    create_at = models.IntegerField()


    def __str__(self):
        return self.model


