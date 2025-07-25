""" 1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais. """

def calcular_gorjeta(valor_conta, porcentagem):
    gorjeta = valor_conta * (porcentagem / 100)
    return round(gorjeta, 2)


valor = float(input("Valor da conta (R$): "))
percentual = float(input("Porcentagem da gorjeta (%): "))
print(f"Gorjeta: R$ {calcular_gorjeta(valor, percentual):.2f}")
