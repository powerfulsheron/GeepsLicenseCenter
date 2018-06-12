from django import forms

from .models import Demande

class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ('nom','prenom','email','phone','batiment','bureau','logiciel','version','os','host')