from django import forms
from .models import AuthUser
from .models import Profile
from django.forms.widgets import ClearableFileInput



class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = ''

class ProfileUpdateForm(forms.ModelForm):
    delete_image = forms.BooleanField(label='Delete Profile Picture', required=False)

    class Meta:
        model = Profile
        fields = ['bio', 'image']

    def clean(self):
        cleaned_data = super().clean()
        delete_image = cleaned_data.get("delete_image")

        if delete_image:
            # If the user wants to delete the image, set the image field to default.png
            cleaned_data['image'] = 'default.png'

        return cleaned_data