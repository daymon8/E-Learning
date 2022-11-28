# #5qs
# 1. Inputs - Medidas do retângulo 
#2. Ação necessaria para tratamento dos inputs - Calcular area e perimetro
#3. restriçoes e/ou condiçoes - Introduzir valores positivos
#4. Output esperado - Area e perímetro do retângulo
#pseudocode

'''input lados do retangulo
calculo das operaçoes
print resultado das operacoes'''

alturaret = float(input('Digite a altura do retângulo: '))
baseret = float(input('Digite a altura do retângulo: '))

area = float(baseret) * float(alturaret)
perimetro = float(baseret)*2 + float(alturaret)*2

print ('Area =  ', area)
print ('Perimetro = ', perimetro)