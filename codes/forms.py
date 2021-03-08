from django import forms
from .models import Codigo

class CodeForm(forms.ModelForm):
    class Meta:
        number = forms.CharField(label = 'code', help_text='Entra codigo de verificacion')
        model = Codigo
        fields = ('number',)