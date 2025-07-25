""" 3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".   """

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == "sair":
        print("Programa encerrado.")
        break

    possui_numero = False

    for caractere in senha:
        if caractere.isdigit():
            possui_numero = True
            break

    if len(senha) >= 8 and possui_numero:
        print("Senha forte.")
        break
    else:
        print("Senha fraca. A senha deve ter pelo menos 8 caracteres e conter ao menos um número.")
