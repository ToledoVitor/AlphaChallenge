from django import forms
# from django.utils.translation import ugettext_lazy as _

from .models import AvisoPreco


class CreateAvisoPrecoForm(forms.ModelForm):
    class Meta:
        model = AvisoPreco
        fields = ('cotacao_code', 'value')
        # labels = {
        #     'cotacao_code': _('Código do Ativo'),
        #     'value': _('Preço'),
        # }
