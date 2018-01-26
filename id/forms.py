from django import forms

from .models import Id_number

class IdForm(forms.ModelForm):
    class Meta:
        model = Id_number
        fields = ['id_numbers']
        labels = {'id_numbers':''}