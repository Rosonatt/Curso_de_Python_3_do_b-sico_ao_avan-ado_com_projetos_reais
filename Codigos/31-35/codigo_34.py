"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um codigo não tem fim 
"""
condicao = True

while condicao:

    nome  =  input( 'Qual o seu nome:' )
    print(f' o seu nome é {nome}')
    
    if nome  == 'sair':
        break
print('acabou')    
 
