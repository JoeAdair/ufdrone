from django import forms
from .models import DroneSighting

class DroneSightingForm(forms.ModelForm):
    class Meta:
        model = DroneSighting
        fields = ['city', 'state', 'latitude', 'longitude', 'description', 'image_link', 'video_link']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter latitude'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter longitude'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description'}),
            'image_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter image URL'}),
            'video_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter video URL'}),
        }
