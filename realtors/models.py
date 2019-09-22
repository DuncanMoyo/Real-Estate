from django.db import models
from datetime import datetime
from django.urls import reverse


class Realtor(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField()
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name

    def get_realtor_url(self):
        return reverse('realtors:realtor', kwargs={
            'slug': self.slug
        })


