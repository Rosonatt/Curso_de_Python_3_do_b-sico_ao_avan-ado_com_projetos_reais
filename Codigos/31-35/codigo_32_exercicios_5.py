"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#primeira forma
numero = input("Digite um Número por favor: ") 

if numero.isdigit():
    numero_int =  int(numero)
    par_impar =  numero_int %2 == 0
    par_impar_texto = 'ímpar'
    
    if par_impar:
        par_impar_texto = 'par '
    print(f'O número {numero_int} é {par_impar_texto}')
else: 
    print(' voce não digitou um numero inteiro')

#segunda forma
numero = int(input("Digite um Número por favor: "))
try:
    numero %2 == 0
    print('esse numero é par')
    numero  %3 ==0  or numero %5 == 0
    print('esse numero é impar')
except:
    print('vc não digitou um numero inteiro')

   

  
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora =  input('Que horas são? ')
try:
    hora_int =  int(hora)
    if hora_int <= 11 and hora_int >= 00: 
        print('Bom dia')

    elif hora_int <= 17 and hora_int >= 12:
        print('Boa Tarde')

    elif hora_int <= 23 and hora_int >= 18:
        print('Boa noite')
    else:
        print('não conheço essa hora')     
except:
    print(f' a hora digitada {hora} não é um numero inteiro')     

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome_usuario =  input('Qual o seu primeiro nome?')
tamanho_nome =  len(nome_usuario)

if tamanho_nome >= 1:
    if tamanho_nome <=4:
        print(f'seu nome {nome_usuario} é muito pequeno')
    elif tamanho_nome <=6 and tamanho_nome >=5:
        print(f'Seu nome {nome_usuario} é normal')
    elif tamanho_nome > 6:
        print(f'Seu nome é muito grande')
else:
    print('Digite mais de uma letra')    