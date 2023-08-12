from django import forms
from .models import Album


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        labels = {
            'name': 'Album name',
            'artist': 'Artist',
            'description': 'Description',
            'image': 'Image URL',
            'price': 'Price'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'})
        }

class CreateAlbumForm(BaseAlbumForm):
    pass

class EditAlbumForm(BaseAlbumForm):
    pass

class DeleteAlbumForm(BaseAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
