from django import forms

from portal.models import Professor  # Importação corrigida.

class ProfessorForm(forms.ModelForm):
    class Meta:  # A classe meta serve para configurar o form
        model = Professor  # Define o model que o form representa
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]
