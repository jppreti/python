usuarios = []
opcao = ''
menu = '''
[1] - Cadastrar
[2] - Excluir
[3] - Exibir todos

[0] - Sair

'''
while opcao != '0':
    print(menu)
    opcao = input('Digite a opção desejada: ')

    if (opcao == '1'): usuarios.append(input('Novo usuário: '))
    if (opcao == '2'): usuarios.remove(input('Usuário a ser excluído: '))
    if (opcao == '3'):
        for u in usuarios:
            print(u)
        input('')

