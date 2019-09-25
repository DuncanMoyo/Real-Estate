from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('listings.urls', namespace='listings')),
    path('', include('realtors.urls', namespace='realtors')),
    path('', include('blog.urls', namespace='blog')),
    path('', include('about.urls', namespace='about')),
    path('', include('contacts.urls', namespace='contacts')),
    path('tinymce/', include('tinymce.urls')),
    url(r'^account/', include('allauth.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

