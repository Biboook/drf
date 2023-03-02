from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Warehouse(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    numbers = models.PositiveIntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=64)
    quantity = models.PositiveIntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product} ({self.sender} -> {self.receiver})'