""" 3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais. """

def calcular_preco_com_desconto(preco, desconto_percentual):
    desconto = preco * (desconto_percentual / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)


preco_produto = float(input("Preço original do produto (R$): "))
percentual_desconto = float(input("Percentual de desconto (%): "))
print(f"Preço com desconto: R$ {calcular_preco_com_desconto(preco_produto, percentual_desconto):.2f}")
