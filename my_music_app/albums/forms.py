from django import forms

from my_music_app.albums.models import Album



class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image': forms.FileInput(attrs={'placeholder': 'Image'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price'}),
        }


class AlbumDeleteForm(AlbumCreateForm):
    class Meta:
        model = Album
        exclude = ['owner']


