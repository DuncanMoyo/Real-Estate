from django.shortcuts import render
from .models import About
from realtors.models import Realtor


def about(request):
    about_page = About.objects.all()
    realtors = Realtor.objects.order_by('-hire_date')[:3]

    context = {
        'about_page': about_page,
        'realtors': realtors,
    }

    return render(request, 'about.html', context)
