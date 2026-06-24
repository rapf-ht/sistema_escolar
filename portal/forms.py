from django import forms

from models import Professor  # ERRO 3: importação incorreta. Deve ser: from portal.models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:  # A classe meta serve para configurar o form
        model = Professor  # Define o model que o form representa
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]
