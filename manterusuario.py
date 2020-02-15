usuarios = [] #lista de usuários para manter em memória principal
opcao = ''    #guarda a opção escolhida pelo usuário
#menu que será exibido para o usuário
menu = '''    
[1] - Cadastrar novo usuário
[2] - Excluir um usuário
[3] - Exibir todos os usuários (total: {})

[0] - Sair

'''
while opcao != '0':
    print(menu.format(len(usuarios)))
    opcao = input('Digite a opção desejada: ')

    if (opcao == '1'): usuarios.append(input('Novo usuário: '))
    if (opcao == '2'): usuarios.remove(input('Usuário a ser excluído: '))
    if (opcao == '3'):
        usuarios.sort()
        for u in usuarios:
            print(u)
        input('') #serve apenas para pausar após exibir a lista

