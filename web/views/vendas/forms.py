from django import forms

from web.models import Venda


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['produto', 'quantidade', 'preco', "vendedor"]
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'vendedor': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


