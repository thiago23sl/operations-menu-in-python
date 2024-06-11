#thiago silva lima
#Analise e desenvolvimento de sistemas 

# Inicializa uma lista vazia para armazenar informações dos alunos
informacoes_alunos = []

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

            # Opção para incluir um aluno
            if OpcaoSegundoMenu == 1:
                NomeAluno = input('Qual o nome do aluno a ser adicionado? ')
                codigo_Aluno = int(input('Qual o código desse aluno? '))
                Cpf_aluno = input('Qual o CPF dele? ')

                informacoes_Aluno = {"nome": NomeAluno, "codigo": codigo_Aluno, "cpf": Cpf_aluno}
                informacoes_alunos.append(informacoes_Aluno)
                print('Aluno adicionado com sucesso.')

            # Opção para listar todos os alunos adicionados
            elif OpcaoSegundoMenu == 2:
                print("-" * 15 + 'LISTANDO' + "-" * 15)
                if len(informacoes_alunos) == 0:
                    print('Nenhum aluno cadastrado. Por favor, cadastre um aluno.')
                else:
                    for aluno in informacoes_alunos:
                        print(f"Nome: {aluno['nome']}, Código: {aluno['codigo']}, CPF: {aluno['cpf']}")

            # Opção para atualizar um aluno existente
            elif OpcaoSegundoMenu == 3:
                print("-" * 15 + 'ATUALIZANDO' + "-" * 15)
                Codigo_Editar_Aluno = int(input('Qual o código do aluno a ser editado? '))

                aluno_encontrado = None
                for aluno in informacoes_alunos:
                    if aluno['codigo'] == Codigo_Editar_Aluno:
                        aluno_encontrado = aluno
                        break
                
                if aluno_encontrado:
                    Novo_NomeAluno = input('Qual o novo nome do aluno? ')
                    Novo_Cpf_aluno = input('Qual o novo CPF do aluno? ')

                    aluno_encontrado['nome'] = Novo_NomeAluno
                    aluno_encontrado['cpf'] = Novo_Cpf_aluno

                    print('Aluno atualizado com sucesso.')
                else:
                    print('Aluno não encontrado com este código.')

            # Opção para excluir um aluno existente
            elif OpcaoSegundoMenu == 4:
                print("-" * 15 + 'EXCLUINDO' + "-" * 15)
                Codigo_Excluir_Aluno = int(input('Qual código do aluno você deseja excluir? '))

                for aluno in informacoes_alunos:
                    if aluno['codigo'] == Codigo_Excluir_Aluno:
                        informacoes_alunos.remove(aluno)
                        print(f'Aluno com código {Codigo_Excluir_Aluno} removido com sucesso.')
                        break
                else:
                    print('Aluno não encontrado com este código.')

            else:
                print('Opção inválida. Por favor, escolha uma opção válida.')

    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')