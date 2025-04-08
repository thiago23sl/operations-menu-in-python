#thiago silva lima
#Analise e desenvolvimento de sistemas 

import json

# Listas para armazenar informações
informacoes_alunos = []
informacoes_professores = []
informacoes_disciplinas = []
informacoes_turmas = []
informacoes_matriculas = []

# Função para salvar os dados em um arquivo JSON
def salvar_dados_json():
    with open('dados.json', 'w') as arquivo_json:
        json.dump({
            "alunos": informacoes_alunos,
            "professores": informacoes_professores,
            "disciplinas": informacoes_disciplinas,
            "turmas": informacoes_turmas,
            "matriculas": informacoes_matriculas
        }, arquivo_json)
    print('Dados salvos com sucesso em "dados.json".')

# Função para carregar os dados do arquivo JSON ao iniciar o programa
def carregar_dados_json():
    global informacoes_alunos, informacoes_professores, informacoes_disciplinas, informacoes_turmas, informacoes_matriculas
    try:
        with open('dados.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)
            informacoes_alunos = dados.get('alunos', [])
            informacoes_professores = dados.get('professores', [])
            informacoes_disciplinas = dados.get('disciplinas', [])
            informacoes_turmas = dados.get('turmas', [])
            informacoes_matriculas = dados.get('matriculas', [])
        print('Dados carregados com sucesso de "dados.json".')
    except FileNotFoundError:
        print('Nenhum dado anterior encontrado. Iniciando com listas vazias.')


# Função para exibir o menu principal e interagir com o usuário
def menu_principal():
    while True:
        print("-" * 15 + 'MENU PRINCIPAL' + "-" * 15)
        opcao_menu = input('(1) Gerenciar alunos.'
                         '\n(2) Gerenciar professores.'
                         '\n(3) Gerenciar disciplinas.'
                         '\n(4) Gerenciar turmas.'
                         '\n(5) Gerenciar matrículas.'
                         '\n(9) Sair'
                         '\nInforme a opção desejada: ') 
        if opcao_menu == '1':
            menu_pessoas('aluno')
        elif opcao_menu == '2':
            menu_pessoas('professor')
        elif opcao_menu == '3':
            menu_disciplinas()
        elif opcao_menu == '4':
            menu_turmas()
        elif opcao_menu == '5':
            menu_matriculas()
        elif opcao_menu == '9':
            print('Finalizando aplicação. Obrigado por utilizar nosso software.')
            salvar_dados_json()
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

# Função para exibir o menu de gerenciamento de alunos ou professores
def menu_pessoas(tipo):
    while True:
        print("-" * 15 + f'MENU DE {tipo.upper()}' + "-" * 15)
        opcao_menu = input('(1) Incluir'
                           '\n(2) Listar'
                           '\n(3) Atualizar'
                           '\n(4) Excluir'
                           '\n(9) Voltar ao menu principal'
                           '\nInforme a opção desejada: ')

        if opcao_menu == '1':
            adicionar_pessoa(tipo)
        elif opcao_menu == '2':
            listar_pessoas(tipo)
        elif opcao_menu == '3':
            atualizar_pessoa(tipo)
        elif opcao_menu == '4':
            excluir_pessoa(tipo)
        elif opcao_menu == '9':
            print('Voltando ao menu principal.')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

# Função para validar o CPF
def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    # Verifica os nove primeiros dígitos do CPF
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[9]):
        return False
    # Verifica os dez primeiros dígitos do CPF
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[10]):
        return False
    return True

# Função para adicionar um novo aluno ou professor
def adicionar_pessoa(tipo):
    print("-" * 15 + f'ADICIONANDO {tipo.upper()}' + "-" * 15)
    while True:
        nome = input(f'Qual o nome do {tipo.lower()} a ser adicionado? ')
        codigo = int(input(f'Qual o código desse {tipo.lower()}? '))
        cpf = input(f'Qual o CPF dele? ')

        # Verifica se o código já está em uso por outra pessoa
        if any(pessoa['codigo'] == codigo for pessoa in informacoes_alunos + informacoes_professores):
            print(f"Já existe um {tipo.lower()} com o código {codigo}. Por favor, escolha outro código.")
            continue
        
        # Verifica se o CPF é válido
        if not validar_cpf(cpf):
            print("CPF inválido. Por favor, insira um CPF válido.")
            continue

        # Adiciona as informações à lista correspondente
        informacoes_pessoa = {"nome": nome, "codigo": codigo, "cpf": cpf}
        if tipo == 'aluno':
            informacoes_alunos.append(informacoes_pessoa)
        else:
            informacoes_professores.append(informacoes_pessoa)
        print(f'{tipo.capitalize()} adicionado com sucesso.')
        break

# Função para listar todos os alunos ou professores cadastrados
def listar_pessoas(tipo):
    print("-" * 15 + f'LISTANDO {tipo.upper()}' + "-" * 15)
    informacoes = informacoes_alunos if tipo == 'aluno' else informacoes_professores
    if len(informacoes) == 0:
        print(f'Nenhum {tipo.lower()} cadastrado. Por favor, cadastre um {tipo.lower()}.')
    else:
        for pessoa in informacoes:
            print(f"Nome: {pessoa['nome']}, Código: {pessoa['codigo']}, CPF: {pessoa['cpf']}")

# Função para atualizar informações de um aluno ou professor existente
def atualizar_pessoa(tipo):
    print("-" * 15 + f'ATUALIZANDO {tipo.upper()}' + "-" * 15)
    codigo_editar = int(input(f'Qual o código do {tipo.lower()} a ser editado? '))

    pessoa_encontrada = None
    informacoes = informacoes_alunos if tipo == 'aluno' else informacoes_professores
    for pessoa in informacoes:
        if pessoa['codigo'] == codigo_editar:
            pessoa_encontrada = pessoa
            break
    
    if not pessoa_encontrada:
        print(f'{tipo.capitalize()} não encontrado com este código.')
        return
    
    while True:
        novo_codigo = int(input(f'Qual o novo código do {tipo.lower()}? '))
        if any(pessoa['codigo'] == novo_codigo for pessoa in informacoes if pessoa['codigo'] != codigo_editar):
            print(f"Já existe um {tipo.lower()} com o código {novo_codigo}. Por favor, escolha outro código.")
            continue
        else:
            pessoa_encontrada['codigo'] = novo_codigo
            break
        
    while True:
        novo_cpf = input(f'Qual o novo CPF do {tipo.lower()}? ')
        if not validar_cpf(novo_cpf):
            print("CPF inválido. Por favor, insira um CPF válido.")
            continue
        if any(pessoa['cpf'] == novo_cpf for pessoa in informacoes if pessoa['codigo'] != codigo_editar):
            print(f"CPF {novo_cpf} já está associado a outro {tipo.lower()}. Por favor, insira outro CPF.")
            continue
        else:
            pessoa_encontrada['cpf'] = novo_cpf
            break

    novo_nome = input(f'Qual o novo nome do {tipo.lower()}? ')
    pessoa_encontrada['nome'] = novo_nome

    print(f'{tipo.capitalize()} atualizado com sucesso.')

# Função para excluir um aluno ou professor da lista com base no código
def excluir_pessoa(tipo):
    print("-" * 15 + f'EXCLUINDO {tipo.upper()}' + "-" * 15)
    codigo_excluir = int(input(f'Qual código do {tipo.lower()} você deseja excluir? '))

    informacoes = informacoes_alunos if tipo == 'aluno' else informacoes_professores
    for pessoa in informacoes:
        if pessoa['codigo'] == codigo_excluir:
            informacoes.remove(pessoa)
            print(f'{tipo.capitalize()} com código {codigo_excluir} removido com sucesso.')
            break
    else:
        print(f'{tipo.capitalize()} não encontrado com este código.')

# Função para exibir o menu de gerenciamento de disciplinas
def menu_disciplinas():
    while True:
        print("-" * 15 + 'MENU DE DISCIPLINAS' + "-" * 15)
        opcao_menu = input('(1) Incluir'
                           '\n(2) Listar'
                           '\n(3) Atualizar'
                           '\n(4) Excluir'
                           '\n(9) Voltar ao menu principal'
                           '\nInforme a opção desejada: ')

        if opcao_menu == '1':
            adicionar_disciplina()
        elif opcao_menu == '2':
            listar_disciplinas()
        elif opcao_menu == '3':
            atualizar_disciplina()
        elif opcao_menu == '4':
            excluir_disciplina()
        elif opcao_menu == '9':
            print('Voltando ao menu principal.')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
            
# Função para adicionar uma nova disciplina
def adicionar_disciplina():
    print("-" * 15 + 'ADICIONANDO DISCIPLINA' + "-" * 15)
    while True:
        codigo = int(input('Qual o código da disciplina? '))
        nome = input('Qual o nome da disciplina? ')

        # Verifica se o código já está em uso por outra disciplina
        if any(disciplina['codigo'] == codigo for disciplina in informacoes_disciplinas):
            print(f"Já existe uma disciplina com o código {codigo}. Por favor, escolha outro código.")
            continue

        # Adiciona as informações à lista de disciplinas
        informacoes_disciplinas.append({"codigo": codigo, "nome": nome})
        print('Disciplina adicionada com sucesso.')
        break

# Função para listar todas as disciplinas cadastradas
def listar_disciplinas():
    print("-" * 15 + 'LISTANDO DISCIPLINAS' + "-" * 15)
    if len(informacoes_disciplinas) == 0:
        print('Nenhuma disciplina cadastrada.')
    else:
        for disciplina in informacoes_disciplinas:
            print(f"Código: {disciplina['codigo']}, Nome: {disciplina['nome']}")

# Função para atualizar informações de uma disciplina existente
def atualizar_disciplina():
    print("-" * 15 + 'ATUALIZANDO DISCIPLINA' + "-" * 15)
    codigo_editar = int(input('Qual o código da disciplina a ser editada? '))

    disciplina_encontrada = None
    for disciplina in informacoes_disciplinas:
        if disciplina['codigo'] == codigo_editar:
            disciplina_encontrada = disciplina
            break
    
    if not disciplina_encontrada:
        print('Disciplina não encontrada com este código.')
        return
    
    novo_nome = input('Qual o novo nome da disciplina? ')
    disciplina_encontrada['nome'] = novo_nome

    print('Disciplina atualizada com sucesso.')

# Função para excluir uma disciplina da lista com base no código
def excluir_disciplina():
    print("-" * 15 + 'EXCLUINDO DISCIPLINA' + "-" * 15)
    codigo_excluir = int(input('Qual o código da disciplina que você deseja excluir? '))

    for disciplina in informacoes_disciplinas:
        if disciplina['codigo'] == codigo_excluir:
            informacoes_disciplinas.remove(disciplina)
            print(f'Disciplina com código {codigo_excluir} removida com sucesso.')
            break
    else:
        print('Disciplina não encontrada com este código.')

def menu_turmas():
    while True:
        print("-" * 15 + 'MENU DE TURMAS' + "-" * 15)
        opcao_menu = input('(1) Incluir'
                           '\n(2) Listar'
                           '\n(3) Atualizar'
                           '\n(4) Excluir'
                           '\n(9) Voltar ao menu principal'
                           '\nInforme a opção desejada: ')

        if opcao_menu == '1':
            adicionar_turma()
        elif opcao_menu == '2':
            listar_turmas()
        elif opcao_menu == '3':
            atualizar_turma()
        elif opcao_menu == '4':
            excluir_turma()
        elif opcao_menu == '9':
            print('Voltando ao menu principal.')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

def adicionar_turma():
    print("-" * 15 + 'ADICIONANDO TURMA' + "-" * 15)
    while True:
        codigo = int(input('Qual o código da turma? '))
        codigo_professor = int(input('Qual o código do professor responsável? '))
        codigo_disciplina = int(input('Qual o código da disciplina relacionada? '))

        # Verifica se o código da turma já está em uso
        if any(turma['codigo'] == codigo for turma in informacoes_turmas):
            print(f"Já existe uma turma com o código {codigo}. Por favor, escolha outro código.")
            continue

        # Verifica se o professor e a disciplina existem
        professor_encontrado = next((pessoa for pessoa in informacoes_professores if pessoa['codigo'] == codigo_professor), None)
        disciplina_encontrada = next((disciplina for disciplina in informacoes_disciplinas if disciplina['codigo'] == codigo_disciplina), None)
        
        if not professor_encontrado:
            print(f"Professor com código {codigo_professor} não encontrado.")
            return
        
        if not disciplina_encontrada:
            print(f"Disciplina com código {codigo_disciplina} não encontrada.")
            return

        # Adiciona as informações à lista de turmas
        informacoes_turmas.append({
            "codigo": codigo,
            "codigo_professor": codigo_professor,
            "codigo_disciplina": codigo_disciplina
        })
        print('Turma adicionada com sucesso.')
        break


# Função para listar todas as turmas cadastradas
def listar_turmas():
    print("-" * 15 + 'LISTANDO TURMAS' + "-" * 15)
    if len(informacoes_turmas) == 0:
        print('Nenhuma turma cadastrada.')
    else:
        for turma in informacoes_turmas:
            print(f"Código: {turma['codigo']}, Professor: {turma['codigo_professor']}, Disciplina: {turma['codigo_disciplina']}")

# Função para atualizar informações de uma turma existente
def atualizar_turma():
    print("-" * 15 + 'ATUALIZANDO TURMA' + "-" * 15)
    codigo_editar = int(input('Qual o código da turma a ser editada? '))

    turma_encontrada = None
    for turma in informacoes_turmas:
        if turma['codigo'] == codigo_editar:
            turma_encontrada = turma
            break
    
    if not turma_encontrada:
        print('Turma não encontrada com este código.')
        return

    novo_codigo_professor = int(input('Qual o novo código do professor responsável? '))
    novo_codigo_disciplina = int(input('Qual o novo código da disciplina relacionada? '))

    # Verifica se o novo professor e disciplina existem
    professor_existe = any(pessoa['codigo'] == novo_codigo_professor for pessoa in informacoes_professores)
    disciplina_existe = any(disciplina['codigo'] == novo_codigo_disciplina for disciplina in informacoes_disciplinas)
        
    if not professor_existe:
        print(f"Professor com código {novo_codigo_professor} não encontrado.")
        return
    
    if not disciplina_existe:
        print(f"Disciplina com código {novo_codigo_disciplina} não encontrada.")
        return

    turma_encontrada['codigo_professor'] = novo_codigo_professor
    turma_encontrada['codigo_disciplina'] = novo_codigo_disciplina

    print('Turma atualizada com sucesso.')

# Função para excluir uma turma da lista com base no código
def excluir_turma():
    print("-" * 15 + 'EXCLUINDO TURMA' + "-" * 15)
    codigo_excluir = int(input('Qual o código da turma que você deseja excluir? '))

    for turma in informacoes_turmas:
        if turma['codigo'] == codigo_excluir:
            informacoes_turmas.remove(turma)
            print(f'Turma com código {codigo_excluir} removida com sucesso.')
            break
    else:
        print('Turma não encontrada com este código.')
# Função para exibir o menu de gerenciamento de matrículas
def menu_matriculas():
    while True:
        print("-" * 15 + 'MENU DE MATRÍCULAS' + "-" * 15)
        opcao_menu = input('(1) Incluir'
                           '\n(2) Listar'
                           '\n(3) Atualizar'
                           '\n(4) Excluir'
                           '\n(9) Voltar ao menu principal'
                           '\nInforme a opção desejada: ')

        if opcao_menu == '1':
            adicionar_matricula()
        elif opcao_menu == '2':
            listar_matriculas()
        elif opcao_menu == '3':
            atualizar_matricula()
        elif opcao_menu == '4':
            excluir_matricula()
        elif opcao_menu == '9':
            print('Voltando ao menu principal.')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

# Função para adicionar uma nova matrícula
def adicionar_matricula():
    print("-" * 15 + 'ADICIONANDO MATRÍCULA' + "-" * 15)
    while True:
        codigo_turma = int(input('Qual o código da turma? '))
        codigo_aluno = int(input('Qual o código do aluno? '))

        # Verifica se a matrícula já existe
        if any(matricula['codigo_turma'] == codigo_turma and matricula['codigo_aluno'] == codigo_aluno for matricula in informacoes_matriculas):
            print(f"Já existe uma matrícula para o aluno {codigo_aluno} nesta turma {codigo_turma}.")
            continue

        # Verifica se a turma e o aluno existem
        turma_existe = any(turma['codigo'] == codigo_turma for turma in informacoes_turmas)
        aluno_existe = any(pessoa['codigo'] == codigo_aluno for pessoa in informacoes_alunos)
        
        if not turma_existe:
            print(f"Turma com código {codigo_turma} não encontrada.")
            continue
        
        if not aluno_existe:
            print(f"Aluno com código {codigo_aluno} não encontrado.")
            continue

        # Adiciona as informações à lista de matrículas
        informacoes_matriculas.append({
            "codigo_turma": codigo_turma,
            "codigo_aluno": codigo_aluno
        })
        print('Matrícula adicionada com sucesso.')
        break

# Função para listar todas as matrículas cadastradas
def listar_matriculas():
    print("-" * 15 + 'LISTANDO MATRÍCULAS' + "-" * 15)
    if len(informacoes_matriculas) == 0:
        print('Nenhuma matrícula cadastrada.')
    else:
        for matricula in informacoes_matriculas:
            print(f"Código da Turma: {matricula['codigo_turma']}, Código do Aluno: {matricula['codigo_aluno']}")

# Função para atualizar uma matrícula com base nos códigos da turma e do aluno
def atualizar_matricula():
    print("-" * 15 + 'ATUALIZANDO MATRÍCULA' + "-" * 15)
    codigo_turma_antigo = int(input('Qual o código da turma da matrícula a ser atualizada? '))
    codigo_aluno_antigo = int(input('Qual o código do aluno da matrícula a ser atualizada? '))

    matricula_encontrada = None
    for matricula in informacoes_matriculas:
        if matricula['codigo_turma'] == codigo_turma_antigo and matricula['codigo_aluno'] == codigo_aluno_antigo:
            matricula_encontrada = matricula
            break
    
    if not matricula_encontrada:
        print('Matrícula não encontrada com estes códigos.')
        return

    novo_codigo_turma = int(input('Qual o novo código da turma? '))
    novo_codigo_aluno = int(input('Qual o novo código do aluno? '))

    # Verifica se a nova matrícula já existe
    if any(matricula['codigo_turma'] == novo_codigo_turma and matricula['codigo_aluno'] == novo_codigo_aluno for matricula in informacoes_matriculas if matricula != matricula_encontrada):
        print(f"Já existe uma matrícula para o aluno {novo_codigo_aluno} nesta turma {novo_codigo_turma}.")
        return

    # Verifica se a turma e o aluno existem
    turma_existe = any(turma['codigo'] == novo_codigo_turma for turma in informacoes_turmas)
    aluno_existe = any(pessoa['codigo'] == novo_codigo_aluno for pessoa in informacoes_alunos)
        
    if not turma_existe:
        print(f"Turma com código {novo_codigo_turma} não encontrada.")
        return
        
    if not aluno_existe:
        print(f"Aluno com código {novo_codigo_aluno} não encontrado.")
        return

    # Atualiza os códigos da turma e do aluno na matrícula encontrada
    matricula_encontrada['codigo_turma'] = novo_codigo_turma
    matricula_encontrada['codigo_aluno'] = novo_codigo_aluno

    print('Matrícula atualizada com sucesso.')

# Função para excluir uma matrícula da lista com base no código da turma e do aluno
def excluir_matricula():
    print("-" * 15 + 'EXCLUINDO MATRÍCULA' + "-" * 15)
    codigo_turma = int(input('Qual o código da turma da matrícula que você deseja excluir? '))
    codigo_aluno = int(input('Qual o código do aluno da matrícula que você deseja excluir? '))

    for matricula in informacoes_matriculas:
        if matricula['codigo_turma'] == codigo_turma and matricula['codigo_aluno'] == codigo_aluno:
            informacoes_matriculas.remove(matricula)
            print(f'Matrícula do aluno {codigo_aluno} na turma {codigo_turma} removida com sucesso.')
            break
    else:
        print('Matrícula não encontrada com estes códigos.')


# Carregar dados existentes ao iniciar o programa
carregar_dados_json()
# Iniciar o programa principal
menu_principal()
