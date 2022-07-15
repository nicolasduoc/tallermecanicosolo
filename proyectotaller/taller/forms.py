from django import forms
from .models import Atencion,Contacto

class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = '__all__'

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'