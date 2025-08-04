""" 3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`. """

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print(f"CEP: {dados['cep']}")
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    except requests.exceptions.RequestException as e:
        print("Erro ao consultar o CEP:", e)

cep = input("Digite o CEP (somente números): ")
consultar_cep(cep)
