from django import forms
from votacao_app.models import Email



class Codigo(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'

        widgets = {
            'codigo': forms.TextInput(),
            'preco_peca': forms.NumberInput(attrs={'step': '0.01'}),
            'preco_de_custo': forms.NumberInput(attrs={'step': '0.01'}),
            'valor_entrada': forms.NumberInput(attrs={'step': '0.01'}),
            
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(Codigo, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['usuario'].widget = forms.HiddenInput()
        
        self.fields['data_vencimento'].widget = forms.HiddenInput()
        self.fields['qtd_parcela'].widget = forms.HiddenInput()
        self.fields['valor_entrada'].widget = forms.HiddenInput()

        self.fields['fornecedor'].queryset = Email.objects.filter(usuario=user)

