from django.db import models


class Citi(models.Model):
    citi = models.CharField(max_length=100)

    def __str__(self):
        return self.citi


class Client(models.Model):
    citi = models.ForeignKey('Citi', on_delete=models.CASCADE)
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
    citi = models.OneToOneField('Citi', on_delete=models.CASCADE)

    def __str__(self):
        return self.distrib

