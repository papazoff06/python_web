

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from my_music_app.albums.models import Album
from my_music_app.profiles.forms import ProfileCreateForm

from my_music_app.utils import get_user_obj


# Create your views here.
class ShowHomePageView(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        if get_user_obj() is not None:
            return ['common/home-with-profile.html']
        return ['common/home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# just for test
#
#
# another test!!!





