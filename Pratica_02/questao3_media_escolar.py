""" 3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais. """


n1 = 7.5
n2 = 8.0
n3 = 6.5


media = (n1+n2+n3)/3

print("Nota 01     Nota 02    Nota 03   Media" )
print(f" {n1}        {n2}       {n3}        {media:.2f}")