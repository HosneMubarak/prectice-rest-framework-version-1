from django.db import models


# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
