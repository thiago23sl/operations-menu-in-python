#thiago silva lima
#Analise e desenvolvimento de sistemas 

# Inicializa uma lista vazia para armazenar nomes
informacoes = []

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

            # Opção para incluir um  nome, código e cpf
            if OpcaoSegundoMenu == 1:
                
                #saber o nome do aluno
                NomeAluno = input('Qual o nome a ser adicionado? ')
                #saber o código
                codigo_Aluno= int(input('qual o código desse aluno?'))
                #saber o cpf
                Cpf_aluno = int(input('Agora o CPF dele por favor'))

                informacoes_Alunos= {"nome_aluno":NomeAluno, "codigo_aluno":codigo_Aluno, "cpf_aluno":Cpf_aluno}
                informacoes.append(informacoes_Alunos)        
   
            # Opção para listar todos os nomes adicionados
            elif OpcaoSegundoMenu == 2:
                print("-" * 15 + 'LISTANDO' + "-" * 15)
                if len(informacoes)==0:
                    print('não a estudantes cadastrados por favor cadastre um estudante')
                else:
                    print(f'As informações  é {informacoes[0]}')

            # Opção para atualizar um nome existente (não implementada)
            elif OpcaoSegundoMenu == 3:
                print("-" * 15 + 'ATUALIZANDO' + "-" * 15)
                          # Implemente a lógica de atualização aqui
                
                Codigo_Editar_Aluno = int(input('qual o o código a ser editado?'))
                aluno_encontrado = None
                for aluno in informacoes:
                    if aluno[codigo_Aluno] == Codigo_Editar_Aluno:  # Verifica se o código corresponde
                        aluno_encontrado = aluno
                        break
                    
                if Codigo_Editar_Aluno:
                    informacoes.remove(Codigo_Editar_Aluno)
                   #saber o nome do aluno
                Novo_NomeAluno = input('Qual o nome nome a ser adicionado? ')
                #saber o código
                Novo_codigo_Aluno= int(input('qual o novo código desse aluno?'))
                #saber o cpf
                Novo_Cpf_aluno = int(input('Agora o novo CPF dele por favor'))

                Novo_informacoes_Alunos= {Novo_NomeAluno, Novo_codigo_Aluno, Novo_Cpf_aluno}
                informacoes.append(Novo_informacoes_Alunos)                  

            # Opção para excluir um nome existente (não implementada)
            # Opção para excluir um aluno existente
            elif OpcaoSegundoMenu == 4:
                print("-" * 15 + 'EXCLUINDO' + "-" * 15)
                Deletar_Aluno = int(input('Qual código do aluno você deseja excluir? '))

                # Verifica se o aluno com o código fornecido está na lista
                aluno_encontrado = None
                for aluno in informacoes:
                    if aluno[1] == Deletar_Aluno:  # Verifica se o código corresponde
                        aluno_encontrado = aluno
                        break
                    
                if aluno_encontrado:
                    informacoes.remove(aluno_encontrado)
                    print(f'Aluno do código {Deletar_Aluno}removido com sucesso.')
                else:
                    print('Aluno não encontrado com este código.')

                        # Se a opção não for válida, exibe mensagem de erro
            else:
                print('Opção inválida. Por favor, escolha uma opção válida.')
    # Se a opção do menu principal não for válida, exibe mensagem de erro
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')