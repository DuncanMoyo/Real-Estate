from django.urls import path
from .views import realtor_list, realtor, RealtorDetailView

app_name = 'realtors'

urlpatterns = [
    path('agents-grid/', realtor_list, name='agents-grid'),
    path('realtor/<slug>', realtor, name='realtor'),
    path('agent/', RealtorDetailView.as_view(), name='agent')
]