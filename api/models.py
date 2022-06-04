from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.IntegerField()
    opened_at = models.TimeField()
    closed_at = models.TimeField()

    def __str__(self):
        return self.name
