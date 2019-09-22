from django.shortcuts import render, get_object_or_404
from .models import Realtor
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import DetailView


def realtor_list(request):
    agents = Realtor.objects.filter(is_mvp=True)
    paginator = Paginator(agents, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'agents': agents,
        'page_request_var': page_request_var,
        'queryset': paginated_queryset
    }

    return render(request, 'agents-grid.html', context)


def realtor(request, slug):
    agent = get_object_or_404(Realtor, slug=slug)

    context = {
        'agent': agent,
    }

    return render(request, 'agent-single.html', context)


class RealtorDetailView(DetailView):
    model = Realtor
    template_name = 'agent-single.html'
