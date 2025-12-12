# cadastros/forms.py
from django import forms
from .models import Pessoa
import re
from datetime import date

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'endereco', 'data_nascimento', 'cpf', 'email']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        # Limpa o CPF para ter apenas dígitos
        cpf_limpo = re.sub(r'[^\d]', '', cpf)
        
        # Aqui você pode adicionar a mesma lógica de validação matemática do seu script Python puro
        # Por simplicidade, vamos verificar apenas o tamanho por enquanto
        if len(cpf_limpo) != 11:
            raise forms.ValidationError("CPF deve conter 11 dígitos.")
        
        return cpf_limpo

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        if data_nascimento and data_nascimento > date.today():
            raise forms.ValidationError("A data de nascimento не pode ser no futuro.")
        # Pode adicionar validação de maioridade aqui se quiser
        return data_nascimento