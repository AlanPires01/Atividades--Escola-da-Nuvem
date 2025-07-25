""" 4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final. """

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = 2025
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365 
    return idade_dias


ano = int(input("Ano de nascimento: "))
print(f"Idade aproximada em dias: {calcular_idade_em_dias(ano)} dias")