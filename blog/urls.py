from django.urls import path
from .views import blog_list, post, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('blog-grid/', blog_list, name='blog-grid'),
    path('post/<slug>/', post, name='post'),
    path('blog/', BlogDetailView.as_view(), name='blog'),
]