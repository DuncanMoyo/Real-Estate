from django.db import models
from realtors.models import Realtor
from datetime import datetime
from listings.choices import state_choices, price_choices, bedroom_choices, bathroom_choices, garage_choices
from django.urls import reverse


class Amenity(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=state_choices, max_length=20)
    zip_code = models.CharField(max_length=6)
    description = models.TextField()
    price = models.CharField(choices=price_choices, max_length=30)
    bedrooms = models.CharField(choices=bedroom_choices, max_length=3, default=3)
    bathrooms = models.CharField(choices=bathroom_choices, max_length=3, default=2)
    garages = models.CharField(choices=garage_choices, max_length=3, default=1)
    square_ft = models.IntegerField()
    # TODO : GET AMENITY RUNNING, FIND A WAY TO HAVE SELECTED amenities showing instead of all of them
    amenities = models.ManyToManyField('Amenity')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    # TODO : FIND A BETTER WAY TO SHOW MULTIPLE IMAGES
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    floor_plan = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    video_url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('listings:listing', kwargs={
            'slug': self.slug
        })
