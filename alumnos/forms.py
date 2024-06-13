from django.forms import ModelForm
from .models import Genero

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = "__all__"
        labels = {'genero': 'Genero'}