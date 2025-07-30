""" 4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo. """

import json

# Dicionário com dados da pessoa
pessoa = {
    'nome': 'Alan',
    'idade': 25,
    'cidade': 'Sobral'
}

def escrever_json(arquivo, dados):
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        print(f" Arquivo '{arquivo}' gravado com sucesso!")
    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")

def ler_json(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        print("Conteúdo do arquivo:")
        print(dados)
    except Exception as e:
        print(f"O seguinte erro ocorreu: {e}")

# Programa principal
arquivo = input("Digite o nome do arquivo (ex: dados.json): ")
if not arquivo.endswith('.json'):
    arquivo += '.json'

escrever_json(arquivo, pessoa)
ler_json(arquivo)
