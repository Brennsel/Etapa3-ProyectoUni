from django import forms
from .models import Alumno
#from .models import MATERIAS

class FormularioAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('id', 'nombre', 'edad', 'materia')
        labels = {            
            'nombre': 'Nombre',
            'edad': 'Edad',
            'materia': 'Materias',
        }

        nombre = forms.CharField(max_length=128)
        edad = forms.IntegerField() 
        materia = forms.ChoiceField()