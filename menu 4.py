<<<<<<< HEAD
#thiago silva lima
#Analise e desenvolvimento de sistemas 

# Inicializa uma lista vazia para armazenar nomes
nome = []

# Loop principal do programa
while True:
    print('AGUARDE ENQUANTO O MENU É INCIADO')
    print("-" * 15 + 'MENU PRINCIPAL' + "-" * 15)
    
    # Exibe opções do menu principal e solicita uma escolha
    OpcaoPrimeiroMenu = int(input('(1) Gerenciar estudantes.'
                                '\n(2) Gerenciar professores.'
                                '\n(3) Gerenciar disciplinas'
                                '\n(4) Gerenciar turmas'
                                '\n(5) Gerenciar matrículas'
                                '\n(9) Sair'
                                '\nInforme a opção desejada a seguir: '))

    # Se a opção selecionada for sair (9), encerra o programa
    if OpcaoPrimeiroMenu == 9:
        print('Finalizando aplicação. Obrigado por utilizar nosso Software.')
        break

    # Se a opção selecionada estiver entre 1 e 5, executa as ações correspondentes
    if OpcaoPrimeiroMenu in [1, 2, 3, 4, 5]:
        # Determina qual opção foi selecionada e ajusta o texto correspondente
        if OpcaoPrimeiroMenu == 1:
            escrito = 'ESTUDANTES'
        elif OpcaoPrimeiroMenu == 2:
            escrito = 'PROFESSORES'
        elif OpcaoPrimeiroMenu == 3:
            escrito = 'DISCIPLINAS'
        elif OpcaoPrimeiroMenu == 4:
            escrito = 'TURMAS'
        elif OpcaoPrimeiroMenu == 5:
            escrito = 'MATRÍCULAS'

        # Loop para o menu secundário correspondente à opção selecionada
        while True:
            print(f'***** MENU DE {escrito} *****')
            OpcaoSegundoMenu = int(input('(1) Incluir'
                                       '\n(2) Listar'
                                       '\n(3) Atualizar'
                                       '\n(4) Excluir'
                                       '\n(9) Voltar ao menu principal: '))

            # Se escolher voltar (9), sai deste menu e volta ao menu principal
            if OpcaoSegundoMenu == 9:
                print('Voltando ao menu principal.')
                break

            # Opção para incluir um novo nome
            if OpcaoSegundoMenu == 1:
                NomeAluno = input('Qual o nome a ser adicionado? ')
                nome.append(NomeAluno)

            # Opção para listar todos os nomes adicionados
            elif OpcaoSegundoMenu == 2:
                print("-" * 15 + 'LISTANDO' + "-" * 15)
                if len(nome)==0:
                    print('não a estudantes cadastrados por favor cadastre um estudante')
                else:
                    for aluno in nome:
                        print(aluno)

            # Opção para atualizar um nome existente (não implementada)
            elif OpcaoSegundoMenu == 3:
                print("-" * 15 + 'ATUALIZANDO' + "-" * 15)
                # Implemente a lógica de atualização aqui

            # Opção para excluir um nome existente (não implementada)
            elif OpcaoSegundoMenu == 4:
                print("-" * 15 + 'EXCLUINDO' + "-" * 15)
                # Implemente a lógica de exclusão aqui

            # Se a opção não for válida, exibe mensagem de erro
            else:
                print('Opção inválida. Por favor, escolha uma opção válida.')

    # Se a opção do menu principal não for válida, exibe mensagem de erro
    else:
=======
#thiago silva lima
#Analise e desenvolvimento de sistemas 

# Inicializa uma lista vazia para armazenar nomes
nome = []

# Loop principal do programa
while True:
    print('AGUARDE ENQUANTO O MENU É INCIADO')
    print("-" * 15 + 'MENU PRINCIPAL' + "-" * 15)
    
    # Exibe opções do menu principal e solicita uma escolha
    OpcaoPrimeiroMenu = int(input('(1) Gerenciar estudantes.'
                                '\n(2) Gerenciar professores.'
                                '\n(3) Gerenciar disciplinas'
                                '\n(4) Gerenciar turmas'
                                '\n(5) Gerenciar matrículas'
                                '\n(9) Sair'
                                '\nInforme a opção desejada a seguir: '))

    # Se a opção selecionada for sair (9), encerra o programa
    if OpcaoPrimeiroMenu == 9:
        print('Finalizando aplicação. Obrigado por utilizar nosso Software.')
        break

    # Se a opção selecionada estiver entre 1 e 5, executa as ações correspondentes
    if OpcaoPrimeiroMenu in [1, 2, 3, 4, 5]:
        # Determina qual opção foi selecionada e ajusta o texto correspondente
        if OpcaoPrimeiroMenu == 1:
            escrito = 'ESTUDANTES'
        elif OpcaoPrimeiroMenu == 2:
            escrito = 'PROFESSORES'
        elif OpcaoPrimeiroMenu == 3:
            escrito = 'DISCIPLINAS'
        elif OpcaoPrimeiroMenu == 4:
            escrito = 'TURMAS'
        elif OpcaoPrimeiroMenu == 5:
            escrito = 'MATRÍCULAS'

        # Loop para o menu secundário correspondente à opção selecionada
        while True:
            print(f'***** MENU DE {escrito} *****')
            OpcaoSegundoMenu = int(input('(1) Incluir'
                                       '\n(2) Listar'
                                       '\n(3) Atualizar'
                                       '\n(4) Excluir'
                                       '\n(9) Voltar ao menu principal: '))

            # Se escolher voltar (9), sai deste menu e volta ao menu principal
            if OpcaoSegundoMenu == 9:
                print('Voltando ao menu principal.')
                break

            # Opção para incluir um novo nome
            if OpcaoSegundoMenu == 1:
                NomeAluno = input('Qual o nome a ser adicionado? ')
                nome.append(NomeAluno)

            # Opção para listar todos os nomes adicionados
            elif OpcaoSegundoMenu == 2:
                print("-" * 15 + 'LISTANDO' + "-" * 15)
                if len(nome)==0:
                    print('não a estudantes cadastrados por favor cadastre um estudante')
                else:
                    for aluno in nome:
                        print(aluno)

            # Opção para atualizar um nome existente (não implementada)
            elif OpcaoSegundoMenu == 3:
                print("-" * 15 + 'ATUALIZANDO' + "-" * 15)
                # Implemente a lógica de atualização aqui

            # Opção para excluir um nome existente (não implementada)
            elif OpcaoSegundoMenu == 4:
                print("-" * 15 + 'EXCLUINDO' + "-" * 15)
                # Implemente a lógica de exclusão aqui

            # Se a opção não for válida, exibe mensagem de erro
            else:
                print('Opção inválida. Por favor, escolha uma opção válida.')

    # Se a opção do menu principal não for válida, exibe mensagem de erro
    else:
>>>>>>> 18fab86cc5a1f0b8219bea6d9448448ff61c5e57
        print('Opção inválida. Por favor, escolha uma opção válida.')