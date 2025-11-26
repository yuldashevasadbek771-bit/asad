from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='photos/',blank=True, null=True)
    color = models.CharField(max_length=15)
    type = models.CharField(max_length=50)
    price = models.CharField()
    is_new = models.CharField()

    def __str__(self):
        return self.name


