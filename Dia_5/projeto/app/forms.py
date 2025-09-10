from django import forms
from . models import ViaCep

class ViaCepForm(forms.ModelForm):
    model = ViaCep
    fields = ['cep']
    label = {
        'cep': 'CEP' 
    }
    widgets = {
    'cep': forms.TextInput(attrs={'placeholder': 'Digite um CEP'})
}