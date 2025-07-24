""" 1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais). """

try:
    idade = int(input('Digite sua idade: '))
except ValueError:
    print('Idade inválida! Por favor, digite o valor na forma númerica. Exemplo: 11')
else:
    if idade<0:
        print('Idade inválida!')
    elif (idade<13):
        print('Sua categoria de idade é Criança')
    elif (idade<18):
        print('Sua categoria de idade é Adolescente')
    elif idade<60:
        print('Sua categoria de idade é Adulto')
    else:
        print('Sua categoria de idade é Idoso')