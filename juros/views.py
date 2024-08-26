from django.shortcuts import render
from .forms import JurosForm

def calcular_juros(request):
    resultado = None

    if request.method == 'POST':
        form = JurosForm(request.POST)
        if form.is_valid():
            valor_compra = form.cleaned_data['valor_compra']
            porcentagem_juros_parcela = form.cleaned_data.get('porcentagem_juros_parcela') or 0
            porcentagem_juros_cartao = form.cleaned_data.get('porcentagem_juros_cartao') or 0
            numero_parcelas = form.cleaned_data.get('numero_parcelas') or 1
            
            juros_cartao = valor_compra * (porcentagem_juros_cartao / 100)
            
            valor_total_cartao = valor_compra + juros_cartao
            
            if numero_parcelas > 1:
                valor_total_parcelado = valor_total_cartao * (1 + (porcentagem_juros_parcela / 100) * numero_parcelas)
                valor_parcela = valor_total_parcelado / numero_parcelas
                juros_parcela_total = valor_total_parcelado - valor_total_cartao
            else:
                valor_parcela = valor_total_cartao
                juros_parcela_total = 0
            
            total_juros = juros_cartao + juros_parcela_total
            
            resultado = {
                'valor_total_cartao': valor_total_cartao,
                'juros_cartao': juros_cartao,
                'valor_parcela': valor_parcela,
                'juros_parcela_total': juros_parcela_total,
                'total_juros': total_juros,
            }
    else:
        form = JurosForm()

    return render(request, 'juros/calcular_juros.html', {'form': form, 'resultado': resultado})
