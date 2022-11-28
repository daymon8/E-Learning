# #5qs
# 1. Inputs - Escolher figura geométrica e introduzir medidas
#2. Ação necessaria para tratamento dos inputs - Calculo das operações
#3. restriçoes e/ou condiçoes - Introduzir valores positivos
#4. Output esperado - Area e perímetro da figura geométrica pretendida
#pseudocode

'''input escolher figura geometrica e introduzir medidas
calculo das operacoes
print dos resultados'''

import math
def quadrado():
    lado = float(input('Digite o lado do quadrado: '))
    areaq = lado**2
    perimetro = lado *4
    print('A área do quadrado é de ', areaq)
    print('O perímetro do quadrado é de ', perimetro)
    
def retangulo():
    alturaret = float(input('Digite a altura do retângulo: '))
    baseret = float(input('Digite a altura do retângulo: '))
    arearet = round((alturaret*baseret),2)
    perimetro = round(baseret)*2 + (alturaret)*2
    print('A área do retângulo é de ', arearet)
    print('O perímetro do retângulo é de ', perimetro)

def circulo ():
    raio = float(input('Digite o raio do circulo: '))
    areac = round((math.pi * raio**2),2)
    perimetro = round(2*math.pi*raio)
    print('A área do círculo  é de ', areac)
    print('O perímetro do círculo é de ', perimetro)

escolha=True
while escolha:
    print("\n")
    print("Calculadora de áreas e perímetros")
    print("""
    1.Calcular àrea e perímetro do quadrado
    2.Calcular àrea e perímetro do retângulo
    3.Calcular àrea e perímetro do círculo
    """)
    escolha= input("Escolha uma opção:  ")
    if escolha=="1":
      print('\n')
      quadrado()

    elif escolha=="2":
        print('\n')
        retangulo()
    elif escolha == "3":
        print('\n')
        circulo()
    else:
       print("\n Escolha não válida.\n Tente outra vez.")