
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
    
if OpcaoPrimeiroMenu == 1 or 2 or 3 or 4 or 5:
    OpcaoSegundoMenu = int(input(f'*****MENU DE {escrito}*****'
                                '\n(1)Incluir'
                                '\n(2)Listar'
                                '\n(3)Atualizar'
                                '\n(4)Excluir'
                                '\n(9)voltar ao menu principal: '))
if OpcaoSegundoMenu == 1:
   print("-" * 15+"INCLUINDO"+"-" * 15)      
elif OpcaoSegundoMenu == 2:
    print("-" * 15+'LISTANDO'+"-" * 15)
elif OpcaoSegundoMenu == 3:
    print("-" * 15+'ATUALIZANDO'+"-" * 15)
elif OpcaoSegundoMenu == 4:
    print("-" * 15+'EXCUINDO'+"-" * 15)

print('espere um pouco estamos finalizando')
print('Finalizando aplicação, obrigado por utilizar nosso Software')

