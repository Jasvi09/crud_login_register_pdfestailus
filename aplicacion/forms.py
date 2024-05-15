from django import forms
from .models import Cursos

class FormularioCursos(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre', 'descripcion', 'duracion', 'link', 'creador']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'creador': forms.TextInput(attrs={'class': 'form-control'}),
            
        
        }