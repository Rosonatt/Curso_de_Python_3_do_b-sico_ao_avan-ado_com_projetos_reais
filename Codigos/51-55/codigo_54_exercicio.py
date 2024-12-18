"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']

# for nome in lista:
    # print(nome, type(nome))
lista.append("joão")

indices = range (len(lista))

for indice in indices:
    print(indice,lista[indice],type (lista[indice]))