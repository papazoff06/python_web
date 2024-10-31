from django.urls import path

from furry_funnies.authors.views import author_details_page, author_edit_page, author_delete_page, AuthorCreate

urlpatterns = [
    path('create/', AuthorCreate.as_view(), name='author_create_page'),
    path('details/', author_details_page, name='author_details_page'),
    path('edit/', author_edit_page, name='author_edit_page'),
    path('delete/', author_delete_page, name='author_delete_page'),

]