from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from my_music_app.profiles.models import Profile
from my_music_app.utils import get_user_obj


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_user_obj()

class ProfileDeleteView(DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()
