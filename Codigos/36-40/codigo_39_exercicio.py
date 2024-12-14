"""
Iterando strings com while
"""
#       012345678910
nome = 'Rosonatt'# Iteráveis
#       
index= 0
nome_novo = ''
while index < len(nome):
    letra = nome[index]
    nome_novo += f'*{letra}'
    index +=1
nome_novo  += '*'
print(nome_novo)
