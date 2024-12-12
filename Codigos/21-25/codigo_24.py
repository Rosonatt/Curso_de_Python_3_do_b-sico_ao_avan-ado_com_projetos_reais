#Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7
#  R o s o n a t t
# -6-5-4-3-2-1 0 1
# nome = 'Rosonatt'
# print(nome[2])
# print(nome[-4])
# print('natt' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('natt' not in nome)
# print('zero' not in nome)
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')