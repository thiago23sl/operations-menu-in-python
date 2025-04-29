import json
import re
import os

# Caminho da pasta onde serão salvos os arquivos
PASTA_DADOS = 'operations-menu-in-python'

# ================== Funções auxiliares ==================

def caminho_arquivo(nome_arquivo):
    """Gera o caminho completo do arquivo dentro da pasta de dados."""
    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)
    return os.path.join(PASTA_DADOS, nome_arquivo)

def carregar_dados(arquivo):
    caminho = caminho_arquivo(arquivo)
    if not os.path.exists(caminho):
        with open(caminho, 'w') as f:
            json.dump([], f)
    with open(caminho, 'r') as f:
        return json.load(f)

def salvar_dados(arquivo, dados):
    caminho = caminho_arquivo(arquivo)
    with open(caminho, 'w') as f:
        json.dump(dados, f, indent=4)

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    return len(cpf) == 11 and cpf.isdigit()

def menu_principal():
    print("\n=== Sistema Acadêmico ===")
    print("1. Gerenciar Alunos")
    print("2. Gerenciar Professores")
    print("3. Gerenciar Cursos")
    print("4. Gerenciar Turmas")
    print("5. Gerenciar Matrículas")
    print("0. Sair")

def submenu(titulo):
    print(f"\n--- {titulo} ---")
    print("1. Adicionar")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("0. Voltar")

# ================== Alunos ==================

def adicionar_aluno():
    alunos = carregar_dados('alunos.json')
    nome = input("Nome do aluno: ")
    cpf = input("CPF do aluno (somente números): ")

    if not validar_cpf(cpf):
        print("CPF inválido!")
        return

    for aluno in alunos:
        if aluno['cpf'] == cpf:
            print("Já existe um aluno com este CPF!")
            return

    alunos.append({'nome': nome, 'cpf': cpf})
    salvar_dados('alunos.json', alunos)
    print("Aluno adicionado com sucesso!")

def listar_alunos():
    alunos = carregar_dados('alunos.json')
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']}")

def atualizar_aluno():
    alunos = carregar_dados('alunos.json')
    cpf = input("Digite o CPF do aluno a ser atualizado: ")

    for aluno in alunos:
        if aluno['cpf'] == cpf:
            novo_nome = input("Digite o novo nome: ")
            aluno['nome'] = novo_nome
            salvar_dados('alunos.json', alunos)
            print("Aluno atualizado com sucesso!")
            return

    print("Aluno não encontrado.")

def excluir_aluno():
    alunos = carregar_dados('alunos.json')
    cpf = input("Digite o CPF do aluno a ser excluído: ")

    novos_alunos = [aluno for aluno in alunos if aluno['cpf'] != cpf]
    if len(novos_alunos) == len(alunos):
        print("Aluno não encontrado.")
    else:
        salvar_dados('alunos.json', novos_alunos)
        print("Aluno excluído com sucesso!")

# ================== Professores ==================

def adicionar_professor():
    professores = carregar_dados('professores.json')
    nome = input("Nome do professor: ")
    cpf = input("CPF do professor (somente números): ")

    if not validar_cpf(cpf):
        print("CPF inválido!")
        return

    for professor in professores:
        if professor['cpf'] == cpf:
            print("Já existe um professor com este CPF!")
            return

    professores.append({'nome': nome, 'cpf': cpf})
    salvar_dados('professores.json', professores)
    print("Professor adicionado com sucesso!")

def listar_professores():
    professores = carregar_dados('professores.json')
    if not professores:
        print("Nenhum professor cadastrado.")
    else:
        for professor in professores:
            print(f"Nome: {professor['nome']} | CPF: {professor['cpf']}")

def atualizar_professor():
    professores = carregar_dados('professores.json')
    cpf = input("Digite o CPF do professor a ser atualizado: ")

    for professor in professores:
        if professor['cpf'] == cpf:
            novo_nome = input("Digite o novo nome: ")
            professor['nome'] = novo_nome
            salvar_dados('professores.json', professores)
            print("Professor atualizado com sucesso!")
            return

    print("Professor não encontrado.")

def excluir_professor():
    professores = carregar_dados('professores.json')
    cpf = input("Digite o CPF do professor a ser excluído: ")

    novos_professores = [professor for professor in professores if professor['cpf'] != cpf]
    if len(novos_professores) == len(professores):
        print("Professor não encontrado.")
    else:
        salvar_dados('professores.json', novos_professores)
        print("Professor excluído com sucesso!")

# ================== Cursos ==================

def adicionar_curso():
    cursos = carregar_dados('cursos.json')
    nome = input("Nome do curso: ")
    descricao = input("Descrição do curso: ")

    cursos.append({'nome': nome, 'descricao': descricao})
    salvar_dados('cursos.json', cursos)
    print("Curso adicionado com sucesso!")

def listar_cursos():
    cursos = carregar_dados('cursos.json')
    if not cursos:
        print("Nenhum curso cadastrado.")
    else:
        for curso in cursos:
            print(f"Nome: {curso['nome']} | Descrição: {curso['descricao']}")

def atualizar_curso():
    cursos = carregar_dados('cursos.json')
    nome = input("Digite o nome do curso a ser atualizado: ")

    for curso in cursos:
        if curso['nome'].lower() == nome.lower():
            novo_nome = input("Novo nome: ")
            nova_descricao = input("Nova descrição: ")
            curso['nome'] = novo_nome
            curso['descricao'] = nova_descricao
            salvar_dados('cursos.json', cursos)
            print("Curso atualizado com sucesso!")
            return

    print("Curso não encontrado.")

def excluir_curso():
    cursos = carregar_dados('cursos.json')
    nome = input("Digite o nome do curso a ser excluído: ")

    novos_cursos = [curso for curso in cursos if curso['nome'].lower() != nome.lower()]
    if len(novos_cursos) == len(cursos):
        print("Curso não encontrado.")
    else:
        salvar_dados('cursos.json', novos_cursos)
        print("Curso excluído com sucesso!")

# ================== Turmas ==================

def adicionar_turma():
    turmas = carregar_dados('turmas.json')
    cursos = carregar_dados('cursos.json')
    professores = carregar_dados('professores.json')

    nome_turma = input("Nome da turma: ")
    curso_nome = input("Nome do curso relacionado: ")

    curso_encontrado = next((curso for curso in cursos if curso['nome'].lower() == curso_nome.lower()), None)
    if not curso_encontrado:
        print("Curso não encontrado!")
        return

    professor_cpf = input("CPF do professor: ")

    professor_encontrado = next((prof for prof in professores if prof['cpf'] == professor_cpf), None)
    if not professor_encontrado:
        print("Professor não encontrado!")
        return

    turmas.append({
        'nome_turma': nome_turma,
        'curso': curso_encontrado['nome'],
        'professor': professor_encontrado['nome'],
        'professor_cpf': professor_cpf
    })

    salvar_dados('turmas.json', turmas)
    print("Turma adicionada com sucesso!")

def listar_turmas():
    turmas = carregar_dados('turmas.json')
    if not turmas:
        print("Nenhuma turma cadastrada.")
    else:
        for turma in turmas:
            print(f"Turma: {turma['nome_turma']} | Curso: {turma['curso']} | Professor: {turma['professor']}")

def atualizar_turma():
    turmas = carregar_dados('turmas.json')
    nome_turma = input("Digite o nome da turma a ser atualizada: ")

    for turma in turmas:
        if turma['nome_turma'].lower() == nome_turma.lower():
            novo_nome = input("Novo nome da turma: ")
            turma['nome_turma'] = novo_nome
            salvar_dados('turmas.json', turmas)
            print("Turma atualizada com sucesso!")
            return

    print("Turma não encontrada.")

def excluir_turma():
    turmas = carregar_dados('turmas.json')
    nome_turma = input("Digite o nome da turma a ser excluída: ")

    novas_turmas = [turma for turma in turmas if turma['nome_turma'].lower() != nome_turma.lower()]
    if len(novas_turmas) == len(turmas):
        print("Turma não encontrada.")
    else:
        salvar_dados('turmas.json', novas_turmas)
        print("Turma excluída com sucesso!")

# ================== Matrículas ==================

def adicionar_matricula():
    matriculas = carregar_dados('matriculas.json')
    alunos = carregar_dados('alunos.json')
    turmas = carregar_dados('turmas.json')

    cpf_aluno = input("CPF do aluno para matrícula: ")

    aluno = next((a for a in alunos if a['cpf'] == cpf_aluno), None)
    if not aluno:
        print("Aluno não encontrado!")
        return

    nome_turma = input("Nome da turma para matrícula: ")

    turma = next((t for t in turmas if t['nome_turma'].lower() == nome_turma.lower()), None)
    if not turma:
        print("Turma não encontrada!")
        return

    matriculas.append({'cpf_aluno': cpf_aluno, 'nome_turma': nome_turma})
    salvar_dados('matriculas.json', matriculas)
    print("Matrícula realizada com sucesso!")

def listar_matriculas():
    matriculas = carregar_dados('matriculas.json')
    if not matriculas:
        print("Nenhuma matrícula realizada.")
    else:
        for matricula in matriculas:
            print(f"CPF do Aluno: {matricula['cpf_aluno']} | Turma: {matricula['nome_turma']}")

def excluir_matricula():
    matriculas = carregar_dados('matriculas.json')
    cpf_aluno = input("Digite o CPF do aluno para cancelar matrícula: ")

    novas_matriculas = [m for m in matriculas if m['cpf_aluno'] != cpf_aluno]
    if len(novas_matriculas) == len(matriculas):
        print("Matrícula não encontrada.")
    else:
        salvar_dados('matriculas.json', novas_matriculas)
        print("Matrícula cancelada com sucesso!")

# ================== Execução principal ==================

def gerenciar_modulo(nome, adicionar, listar, atualizar, excluir):
    while True:
        submenu(nome)
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            atualizar()
        elif opcao == '4':
            excluir()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

def main():
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            gerenciar_modulo("Gerenciar Alunos", adicionar_aluno, listar_alunos, atualizar_aluno, excluir_aluno)
        elif opcao == '2':
            gerenciar_modulo("Gerenciar Professores", adicionar_professor, listar_professores, atualizar_professor, excluir_professor)
        elif opcao == '3':
            gerenciar_modulo("Gerenciar Cursos", adicionar_curso, listar_cursos, atualizar_curso, excluir_curso)
        elif opcao == '4':
            gerenciar_modulo("Gerenciar Turmas", adicionar_turma, listar_turmas, atualizar_turma, excluir_turma)
        elif opcao == '5':
            gerenciar_modulo("Gerenciar Matrículas", adicionar_matricula, listar_matriculas, excluir_matricula, excluir_matricula)
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
