from django.shortcuts import render, get_object_or_404
from .models import Listing, Amenity
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import bedroom_choices, price_choices, state_choices
from django.views.generic import DetailView
from django.db.models import Count


def get_category_count():
    queryset = Listing.objects.values('amenities__name').annotate(Count('amenities__name'))
    return queryset


def index(request):
    listings = Listing.objects.order_by('list_date').filter(is_published=True)
    context = {
        'listings': listings
    }

    return render(request, 'index.html', context)


def property_list(request):
    listings = Listing.objects.filter(is_published=True)
    paginator = Paginator(listings, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'listings': listings,
        'page_request_var': page_request_var,
        'queryset': paginated_queryset
    }
    return render(request, 'property-grid.html', context)


def listing(request, slug):
    listing = get_object_or_404(Listing, slug=slug)

    context = {
        'listing': listing,
    }

    return render(request, 'property-single.html', context)


class ListingDetailView(DetailView):
    model = Listing
    template_name = 'property-single.html'


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'search.html', context)

