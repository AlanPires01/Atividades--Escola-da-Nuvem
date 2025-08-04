""" ---

4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.

--- """

import requests
from datetime import datetime

def consultar_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Código de moeda inválido.")
            return

        cotacao = dados[chave]
        print(f"Moeda: {cotacao['code']} -> BRL")
        print(f"Valor atual: R$ {cotacao['bid']}")
        print(f"Valor máximo: R$ {cotacao['high']}")
        print(f"Valor mínimo: R$ {cotacao['low']}")
        
        data_hora = datetime.fromtimestamp(int(cotacao['timestamp']))
        print(f"Última atualização: {data_hora.strftime('%d/%m/%Y %H:%M:%S')}")

    except requests.exceptions.RequestException as e:
        print("Erro na conexão ou código inválido:", e)

moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR): ").upper()
consultar_moeda(moeda)
