from django.db import models
from django.contrib.auth import get_user_model
from tinymce import HTMLField
from django.urls import reverse

User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Blog', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    timestamp = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(blank=True, null=True)
    content = HTMLField('Content', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_blog_url(self):
        return reverse('blog:post', kwargs={
            'slug': self.slug
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')







