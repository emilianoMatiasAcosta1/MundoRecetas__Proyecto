from django import forms 
from Recetas.models import MundoRecetas 

class MundoRecetas(forms.ModelForm):
    class Meta:
        model : MundoRecetas
        fields = ['nombre','grupo','receta','detalle']