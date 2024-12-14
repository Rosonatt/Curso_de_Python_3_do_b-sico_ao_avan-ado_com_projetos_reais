''' Calculdoera com while'''

while True:
    numero_1 =  input('Digite um número:')
    numero_2 =  input('Digite outro número:')
    operador =  input('Digite um operador (+-/*):')

    numeros_validos =  None
    num_1_float = 0
    num_2_float = 0

    try:
         num_1_float =  float(numero_1)
         num_2_float =  float(numero_2)
         numeros_validos = True
         
    except:
        numeros_validos = None

    if numeros_validos is None:
        print(' um ou ambos números são invalidos')
        continue

    operadores_permitidos = "+-/*"  

    if operador not  in operadores_permitidos:
        print('Operador invalido')
        continue

    if len (operador ) >1:
        print('Digite um operador. ')
        continue

    print('Realizando a sua conta. confira o resultado abaixo:')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)

    if operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)

    if operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)

    if operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)

    sair = input ('quer sair? [s]im: '). lower(). startswith('s')
      


    if sair is True:
        print('saindo....')
        break