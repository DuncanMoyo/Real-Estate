from django.urls import path
from .views import Contact

app_name = 'contacts'
urlpatterns = [
    path('contact/', Contact, name='contact')
]
