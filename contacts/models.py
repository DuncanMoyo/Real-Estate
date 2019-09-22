from django.db import models


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()

    def __str__(self):
        return self.name
