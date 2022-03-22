from django.db import models

# Create your models here.

class Flat(models.Model):
    flat = models.IntegerField()
    name = models.CharField(max_length=23)
    block = models.CharField(max_length=23)
    status = models.CharField(max_length=23)
    score = models.IntegerField()

    def __str__(self):
        return self.name


class Manager(models.Model):
    
    flat = models.IntegerField()
    name = models.CharField(max_length=23)
    bloc = models.CharField(max_length=23)
    segregated = models.CharField(max_length=23)

    def __str__(self):
        return self.name


class Analytics(models.Model):
    flat = models.IntegerField()
    name = models.CharField(max_length=23)
    bloc = models.CharField(max_length=23)
    violations = models.IntegerField()

    def __str__(self):
        return self.name