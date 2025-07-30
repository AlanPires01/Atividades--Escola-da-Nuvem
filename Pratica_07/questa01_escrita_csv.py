""" Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.
 """

import csv
lista = [
    ['nome','email','cidade'],
    ['alan','alan@gmail.com','Sobral'],
    ['ian','ian@gmail.com','Massapê'],
    ['Joaquim','joa@gmail.com','Senador Sá']
        
]

def escrever_arquivo(arquivo):
    with open (arquivo,'w',newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerows(lista)


try:
    arquivo = input('Digite o nome do arquivo: ')
    if not arquivo.endswith('.csv'):
        arquivo += '.csv'

    escrever_arquivo(arquivo)
    print(f"Arquivo '{arquivo}' gravado com sucesso!")
except Exception as e:
    print(f'Ocorreu um erro ao gravar o arquivo:{e}')




    