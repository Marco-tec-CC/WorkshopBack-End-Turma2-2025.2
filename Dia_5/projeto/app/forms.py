from django import forms
from . models import ViaCep

class ViaCepForm(forms.ModelForm):      #aqui fica toda visão e a formação do projeto!!
        class Meta:
            model = ViaCep
            fields = ['cep']
            labels = {
        'cep': 'CEP' 
    }
        widgets = {
        'cep': forms.TextInput(attrs={'placeholder': 'Digite um CEP'})
}