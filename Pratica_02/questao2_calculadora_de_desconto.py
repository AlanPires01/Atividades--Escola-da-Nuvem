""" 2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes. """

nomeProduto = "Camiseta"
precoOriginal = 50.00
porcentagem = 20

valorDesconto = precoOriginal*(porcentagem/100)

precoFinal = precoOriginal - valorDesconto

print("Nome     Preco  Desconto(%) Desconto(R$)  Preco Final ")
print(f"{nomeProduto}   {precoOriginal:.2f}    {porcentagem}%      R${valorDesconto:.2f}         R${precoFinal:.2f} ")