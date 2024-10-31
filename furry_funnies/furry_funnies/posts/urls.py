from django.urls import path, include

from furry_funnies.posts.views import create_post_page, details_page, edit_page, delete_page

urlpatterns = [
    path('create/', create_post_page, name='create_post'),
    path('<int:id>/', include([
        path('details/', details_page, name='details'),
        path('edit/', edit_page, name='edit'),
        path('delete/', delete_page, name='delete'),
    ])),
]
