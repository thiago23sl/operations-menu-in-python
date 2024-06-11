# primeiro menu basico  para eu ir em determinados menus
OpcaoPrimeiroMenu = 0
nome= []

while OpcaoPrimeiroMenu != 9:
    print('AGUARDE ENQUANTO O MENU É INCIADO')
    print("-" * 15+'MENU PRINCIPAL'+"-" * 15)
    OpcaoPrimeiroMenu = int(input('(1) Gerenciar estudantes.' 
                     '\n(2) Gerenciar professores.'
                     '\n(3) Gerenciar diciplinas'
                     '\n(4) Gerenciar turmas'
                     '\n(5) Gerenciar matricula'
                     '\n(9) Sair'
                     '\nInforme a opção desejada a seguir:'))
    if OpcaoPrimeiroMenu == 1:
        escrito= 'ESTUDANTES'
    elif OpcaoPrimeiroMenu == 2:
        escrito= 'PROFESSORES'
    elif OpcaoPrimeiroMenu == 3:
        escrito= 'DICIPLINAS'
    elif OpcaoPrimeiroMenu == 4:
        escrito= 'TURMAS'
    elif OpcaoPrimeiroMenu == 5:
        escrito= 'MATRICULAS'
    elif OpcaoPrimeiroMenu == 9:
        break
    else:
        print('o numero digitado não corresponde ao numeros na lista voltaremos você ao menu inicial para que solicite novamento com os numero corretos')
        continue
    if OpcaoPrimeiroMenu == 1 or 2 or 3 or 4 or 5:

# esse while é o segundo menu onde to fazendo esse incluir etc
        menus = 0
        while menus!= 9:
            menus = int(input(f'*****MENU DE {escrito}*****'
                              '\n(1)Incluir'
                              '\n(2)Listar'
                              '\n(3)Atualizar'
                              '\n(4)Excluir'
                              '\n(9)voltar ao menu principal: '))
            if menus == 1:
                NomeAluno= str(input('Qual o nome a ser adicionado?'))
                nome.append(NomeAluno)
            elif menus == 2:
                print("-" * 15+'LISTANDO'+"-" * 15)
                print(nome)
            elif menus == 3:
                print("-" * 15+'ATUALIZANDO'+"-" * 15)
                
            elif menus == 4:
                print("-" * 15+'EXCUINDO'+"-" * 15)
                
            elif menus == 9:
                 print ('voltando ao inicio do menu ')
                 continue 
            else:
                print('o numero digitado não corresponde ao numeros na lista voltaremos você ao menu inicial para que solicite novamento com os numero corretos')
print('espere um pouco estamos finalizando')
print('Finalizando aplicação, obrigado por utilizar nosso Software')

