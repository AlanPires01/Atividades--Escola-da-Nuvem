""" 1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais. """

valorReal = 100.00
taxaDolar = 5.20
taxaEuro = 6.15

print("Valor em reais: R$", valorReal)

print(f"Valor em dolar: US$ {(valorReal/taxaDolar):.2f}")
print(f"Valor em euro: € {(valorReal/taxaEuro):.2f}")