from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from my_music_app.albums.forms import AlbumCreateForm, AlbumDeleteForm
from my_music_app.albums.models import Album
from my_music_app.utils import get_user_obj


# Create your views here.
class AddAlbumView(generic.CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        form.instance.owner_id = get_user_obj().pk
        return super().form_valid(form)


class DetailsAlbumView(generic.DetailView):
    model = Album
    template_name = 'albums/album-details.html'
    pk_url_kwarg = 'id'

class EditAlbumView(generic.UpdateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AlbumDeleteView(generic.DeleteView):
    model = Album
    template_name = 'albums/album-delete.html'
    form_class = AlbumDeleteForm
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"

        return form




