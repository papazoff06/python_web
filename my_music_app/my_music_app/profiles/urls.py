from django.urls import path

from my_music_app.profiles import views

urlpatterns = [
    path('details/', views.ProfileDetailView.as_view(), name='details'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete'),
]