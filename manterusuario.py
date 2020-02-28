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
#abre o arquivo usuarios.dat e carrega cada linha como um usuario dentro da lista
with open('usuarios.dat','r') as arquivo:
    for linha in arquivo: #para cada linha do arquivo
        #se o tamanho da linha desconsiderando os espaços em branco for maior que zero
        #adiciona essa linha na lista como sendo o nome de um usuario
        if len(linha.strip())>0: usuarios.append(linha.strip())

while opcao != '0':
    os.system('clear') or None #limpa a tela do console
    print(menu.format(len(usuarios))) #adiciona a qtde de usuarios cadastrados no menu
    opcao = input('Digite a opção desejada: ')

    if (opcao == '1'):
        while True:
            nome = input('Nome: ')
            if nome=='sair': break
            telefone = input('Telefone: ')
            usuarios.append(nome + ';' + telefone)
    if (opcao == '2'):
        nome = input('Usuário a ser excluído: ')
        for u in usuarios:
            if u.strip().split(';')[0] == nome:
                usuarios.remove(u)
                break
    if (opcao == '3'):
        usuarios.sort() #ordena os elementos da lista
        for u in usuarios:
            #retira o \n porque o print já faz quebra de linha
            registro = u.strip().split(';')
            print(registro[0] + '\t' + registro[1])
        input('') #serve apenas para pausar após exibir a lista

with open('usuarios.dat','w') as arquivo:
    usuarios.sort()
    for usuario in usuarios:
        arquivo.write('\n'+ usuario.strip())