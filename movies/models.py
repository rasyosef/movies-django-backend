from django.db import models
from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=128)
    year_of_release = models.PositiveSmallIntegerField()
    description = models.TextField()
    categories = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    writers = models.CharField(max_length=256)
    image = models.URLField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
