""" 4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais. """

distancia = 300
combustivel = 25

consumoMedio = 300/25

print("Distancia percorrida     Combustivel Gasto     Consumo Medio")
print(f"   {distancia} km                   {combustivel} l                {consumoMedio:.2f} km/l")