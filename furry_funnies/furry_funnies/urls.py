from django.contrib import admin
from django.urls import path, include

from furry_funnies import authors, posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('furry_funnies.common.urls')),
    path('authors/', include('furry_funnies.authors.urls')),
    path('posts/', include('furry_funnies.posts.urls')),
]
