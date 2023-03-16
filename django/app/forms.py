from django import forms

from .models import AvisoPreco


class CreateAvisoPrecoForm(forms.ModelForm):
    class Meta:
        model = AvisoPreco
        fields = ('cotacao_code', 'buy_value', 'sell_value')
