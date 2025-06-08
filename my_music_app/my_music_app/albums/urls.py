from django.urls import path

from my_music_app.albums import views

urlpatterns = [
    path('add/', views.AddAlbumView.as_view(), name='add'),
    path('<id>/details/', views.DetailsAlbumView.as_view(), name='details'),
    path('<id>/edit/', views.EditAlbumView.as_view(), name='edit'),
    path('<id>/delete/', views.AlbumDeleteView.as_view(), name='delete'),

]