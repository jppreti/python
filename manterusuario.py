import os
usuarios = [] #lista de usuários para manter em memória principal
opcao = ''    #guarda a opção escolhida pelo usuário
#menu que será exibido para o usuário
menu = '''    
[1] - Cadastrar novo usuário
[2] - Excluir um usuário
[3] - Exibir todos os usuários (total: {})

[0] - Sair

'''
with open('usuarios.dat','r') as arquivo:
    for linha in arquivo:
        if len(linha.strip())>0: usuarios.append(linha.strip())

while opcao != '0':
    os.system('clear') or None #limpa a tela do console
    print(menu.format(len(usuarios))) #adiciona a qtde de usuarios cadastrados no menu
    opcao = input('Digite a opção desejada: ')

    if (opcao == '1'): usuarios.append(input('Novo usuário: '))
    if (opcao == '2'): usuarios.remove(input('Usuário a ser excluído: '))
    if (opcao == '3'):
        usuarios.sort() #ordena os elementos da lista
        for u in usuarios:
            print(u.strip()) #retira o \n porque o print já faz quebra de linha
        input('') #serve apenas para pausar após exibir a lista

with open('usuarios.dat','w') as arquivo:
    usuarios.sort()
    for usuario in usuarios:
        arquivo.write('\n'+ usuario.strip())