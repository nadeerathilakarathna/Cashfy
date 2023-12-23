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
    account = models.IntegerField()
    detail = models.TextField()
    category = models.IntegerField()
    expense = models.BooleanField()

class Config(models.Model):
    uid = models.IntegerField()
    selection = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f"Config {self.uid}: {self.start} to {self.end}"
