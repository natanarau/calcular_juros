from django import forms

class JurosForm(forms.Form):
    valor_compra = forms.DecimalField(label='Valor da Compra', decimal_places=2)
    porcentagem_juros_parcela = forms.DecimalField(label='Porcentagem de Juros por Parcela (%)', decimal_places=2, required=False)
    porcentagem_juros_cartao = forms.DecimalField(label='Porcentagem de Juros no Cartão (%)', decimal_places=2, required=False)
    numero_parcelas = forms.IntegerField(label='Número de Parcelas', required=False)
