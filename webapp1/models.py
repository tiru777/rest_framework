from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    def __str__(self):
        return self.first_name