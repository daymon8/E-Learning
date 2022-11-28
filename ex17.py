pontuacao = {'.',',',';',':','!','?'}

x = input('Digite um caracter:')

if len(x) !=1:
    print('Digite apenas um caracter!')
else:
    if x.isalpha() == True:
        if x == x.upper():
            print('Letra Maiuscula')
        elif x == x.lower():
            print('Letra Minuscula')
        else:
            print()
    elif x.isnumeric() == True:
        print('Numero')
    elif x in pontuacao:
        print ('Pontuacao')
    else:
        print('Outro Caracter')