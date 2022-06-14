from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.Title