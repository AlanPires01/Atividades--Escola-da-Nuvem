
""" 1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios """


import random
import string

def gerar_senha(tamanho):
    if tamanho < 4:
        return "A senha deve ter pelo menos 4 caracteres."

    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

try:
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    senha = gerar_senha(tamanho)
    print(f"Senha gerada: {senha}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
