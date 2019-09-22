from django.urls import path
from .views import listing, index, property_list, ListingDetailView

app_name = 'listings'

urlpatterns = [
    path('', index),
    path('listing/<slug>/', listing, name='listing'),
    path('property-grid/', property_list, name='property-grid'),
    path('property/', ListingDetailView.as_view(), name='property')
]
