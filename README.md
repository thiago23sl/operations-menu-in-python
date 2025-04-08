# operations-menu-in-python
Estrutura Geral

Importação de Bibliotecas:

O código utiliza a biblioteca json para manipulação de arquivos JSON, permitindo salvar e carregar dados.
Listas de Armazenamento:

O sistema possui listas para armazenar informações sobre:
Alunos (informacoes_alunos)
Professores (informacoes_professores)
Disciplinas (informacoes_disciplinas)
Turmas (informacoes_turmas)
Matrículas (informacoes_matriculas)
Funções Principais:

Salvar e Carregar Dados:
salvar_dados_json(): Salva as informações em um arquivo JSON.
carregar_dados_json(): Carrega as informações do arquivo JSON ao iniciar o programa.
Menu Principal:

menu_principal(): Exibe um menu para o usuário escolher entre gerenciar alunos, professores, disciplinas, turmas, matrículas ou sair do programa.
Gerenciamento de Alunos e Professores:

menu_pessoas(tipo): Exibe um menu para gerenciar alunos ou professores, permitindo incluir, listar, atualizar ou excluir registros.
adicionar_pessoa(tipo): Adiciona um novo aluno ou professor, validando o CPF e o código.
listar_pessoas(tipo): Lista todos os alunos ou professores cadastrados.
atualizar_pessoa(tipo): Atualiza as informações de um aluno ou professor existente.
excluir_pessoa(tipo): Exclui um aluno ou professor com base no código.
Gerenciamento de Disciplinas:

menu_disciplinas(): Exibe um menu para gerenciar disciplinas.
adicionar_disciplina(): Adiciona uma nova disciplina.
listar_disciplinas(): Lista todas as disciplinas cadastradas.
atualizar_disciplina(): Atualiza informações de uma disciplina existente.
excluir_disciplina(): Exclui uma disciplina com base no código.
Gerenciamento de Turmas:

menu_turmas(): Exibe um menu para gerenciar turmas.
adicionar_turma(): Adiciona uma nova turma, verificando se o professor e a disciplina existem.
listar_turmas(): Lista todas as turmas cadastradas.
atualizar_turma(): Atualiza informações de uma turma existente.
excluir_turma(): Exclui uma turma com base no código.
Gerenciamento de Matrículas:

menu_matriculas(): Exibe um menu para gerenciar matrículas.
adicionar_matricula(): Adiciona uma nova matrícula, verificando se a turma e o aluno existem.
listar_matriculas(): Lista todas as matrículas cadastradas.
atualizar_matricula(): Atualiza uma matrícula existente.
excluir_matricula(): Exclui uma matrícula com base nos códigos da turma e do aluno.
Funcionalidades Específicas
Validação de CPF:

A função validar_cpf(cpf) verifica se o CPF informado é válido, garantindo que apenas CPFs corretos sejam cadastrados.
Persistência de Dados:

Os dados são salvos em um arquivo JSON, permitindo que as informações sejam mantidas entre as execuções do programa.
Interação com o Usuário:

O sistema é interativo, permitindo que o usuário escolha opções através de menus e forneça informações através de entradas de texto.