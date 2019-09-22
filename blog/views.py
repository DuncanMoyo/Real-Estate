from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Author
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import DetailView
from .forms import CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def blog_list(request):
    blogs = Blog.objects.filter(featured=True)
    paginator = Paginator(blogs, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'blogs': blogs,
        'page_request_var': page_request_var,
        'queryset': paginated_queryset
    }
    return render(request, 'blog-grid.html', context)


@login_required
def post(request, slug):
    post = get_object_or_404(Blog, slug=slug)

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('blog:post', kwargs={
                'slug': post.slug
            }))

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'blog-single.html', context)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-single.html'

