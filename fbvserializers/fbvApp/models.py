from django.db import models


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.name
