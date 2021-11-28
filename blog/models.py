from django.db import models


class Blog (models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    #look up field reference for functions on model
    date = models.DateField()

    def __str__(self):
        return self.title
