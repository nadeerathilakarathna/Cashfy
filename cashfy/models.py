from django.db import models


# Create your models here.
class Icon(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    expense = models.BooleanField()

class Account(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    checked = models.BooleanField()

class Transaction(models.Model):
    uid = models.IntegerField()
    timestamp = models.DateTimeField()
    amount = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    detail = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expense = models.BooleanField()