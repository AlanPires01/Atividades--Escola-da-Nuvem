""" 1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas. 
O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.
 """ 

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            try:
                resultado = num1 / num2
            except ZeroDivisionError:
                print("Erro: Divisão por zero não é permitida.")
                continue
        else:
            print("Operação inválida. Tente novamente.")
            continue

        print(f"Resultado: {resultado}")
        break

    except ValueError:
        print("Entrada inválida. Digite números válidos.")


