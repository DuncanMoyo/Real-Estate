from django.db import models
from tinymce import HTMLField


class About(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    category = models.CharField(max_length=50, null=True, blank=True)
    vertical_title = models.CharField(max_length=50, null=True, blank=True)
    content_image = models.ImageField(null=True, blank=True)
    content = HTMLField('Content')

    def __str__(self):
        return self.title
