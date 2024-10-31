from django import forms

from furry_funnies.authors.models import Author


class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.TextInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.TextInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }