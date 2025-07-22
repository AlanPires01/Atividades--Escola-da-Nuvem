""" 4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final. """

nomeDoProduto = "Cadeira Infantil"
preco = 12.40
quantidade = 3

precoTotal = preco * quantidade

print(f"       Nome         |     Preço unitário    |     Quantidade |     Total    ")
print(f"   {nomeDoProduto} |    R$ {preco:.2f}           |          {quantidade}     |  R$ {precoTotal:.2f} ")