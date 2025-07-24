""" 3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter. """


temp = int(input("Digite o valor da temperatura: "))
print("Digite uma das opções para a unidade de origem")
print("C p/Celsius")
print("F p/Fahrenheit")
print("K p/Kelvin")
uniOrigem = input(": ")

print("Digite uma das opções para a unidade para qual deseja converter")
print("C p/Celsius")
print("F p/Fahrenheit")
print("K p/Kelvin")
uniDestino = input(": ")


if uniOrigem=="C":
    minOrigem = 0
    maxOrigem = 100
elif uniOrigem =="F":
    minOrigem = 32
    maxOrigem = 212
elif uniOrigem =="F":
    minOrigem = 273
    maxOrigem = 373
else:
    print("Entrada inválida! Digite uma opção válida!")

if uniDestino=="C":
    minDestino = 0
    maxDestino = 100
elif uniDestino =="F":
    minDestino = 32
    maxDestino = 212
elif uniDestino =="K":
    minDestino = 273
    maxDestino = 373
else:
    print("Entrada inválida! Digite uma opção válida!")

#FORMULA DO TEOREMA DE THALES
tempConvertida = minDestino + ((temp - minOrigem) * (maxDestino - minDestino)) / (maxOrigem - minOrigem)

if uniDestino=="C":
    print(f"A temperatura convertida é {tempConvertida:.2f}°C")
elif uniDestino =="F":
    print(f"A temperatura convertida é {tempConvertida:.2f}°F")

elif uniDestino =="K":
    print(f"A temperatura convertida é {tempConvertida:.2f}°K")

else:
    print("Entrada inválida! Digite uma opção válida!")

    


