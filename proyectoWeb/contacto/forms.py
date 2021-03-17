from django import forms

class FormContact(forms.Form):
    nombre = forms.CharField(label='Nombre',required=True, max_length=100)
    email = forms.CharField(label='Email',required=True, max_length=80)
    contenido = forms.CharField(label='Contenido',required=True, widget=forms.Textarea)
