from django import forms

from my_music_app.profiles.models import Profile

class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileCreateForm(ProfileBaseForm):
    pass
