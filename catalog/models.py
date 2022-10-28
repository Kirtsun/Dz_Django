from django.db import models


class City(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Client(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    goods = models.ManyToManyField('Goods')
    names = models.CharField(max_length=100)

    def __str__(self):
        return self.names


class Goods(models.Model):
    products = models.CharField(max_length=100)

    def __str__(self):
        return self.products


class Distributor(models.Model):
    distrib = models.CharField(max_length=100)
    city = models.OneToOneField('City', on_delete=models.CASCADE)

    def __str__(self):
        return self.distrib

