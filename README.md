# 📚 Sistema de Gerenciamento Acadêmico

Este projeto é um sistema de gerenciamento completo para instituições de ensino, desenvolvido em Python. Ele permite controlar alunos, professores, disciplinas, turmas e matrículas, com persistência de dados em arquivos JSON.

---

## 🔧 Estrutura Geral

### 📦 Importação de Bibliotecas

O sistema utiliza a biblioteca `json` para:
- Manipular arquivos JSON;
- Garantir a persistência dos dados entre as execuções.

### 📂 Listas de Armazenamento

As informações são organizadas nas seguintes listas:
- `informacoes_alunos`
- `informacoes_professores`
- `informacoes_disciplinas`
- `informacoes_turmas`
- `informacoes_matriculas`

---

## 💾 Manipulação de Dados

### 📝 Salvamento de Dados

- **Função:** `salvar_dados_json()`
- **Descrição:** Salva os dados em um arquivo JSON.

### 📥 Carregamento de Dados

- **Função:** `carregar_dados_json()`
- **Descrição:** Carrega os dados do arquivo JSON ao iniciar o programa.

---

## 🧭 Menu Principal

### 📌 Função: `menu_principal()`

Menu inicial do sistema que permite acessar as seções de:
- Alunos
- Professores
- Disciplinas
- Turmas
- Matrículas
- Encerramento do programa

---

## 👤 Gerenciamento de Alunos e Professores

### 📍 Menu: `menu_pessoas(tipo)`

Permite gerenciar registros de **alunos** e **professores**:

#### ➕ Adicionar
- **Função:** `adicionar_pessoa(tipo)`
- **Descrição:** Adiciona um novo aluno ou professor, validando código e CPF.

#### 📃 Listar
- **Função:** `listar_pessoas(tipo)`
- **Descrição:** Lista todos os registros cadastrados.

#### ✏️ Atualizar
- **Função:** `atualizar_pessoa(tipo)`
- **Descrição:** Atualiza as informações de um registro.

#### ❌ Excluir
- **Função:** `excluir_pessoa(tipo)`
- **Descrição:** Remove um registro com base no código.

---

## 📘 Gerenciamento de Disciplinas

### 📍 Menu: `menu_disciplinas()`

Operações disponíveis:
- `adicionar_disciplina()`: Cria uma nova disciplina.
- `listar_disciplinas()`: Lista todas as disciplinas.
- `atualizar_disciplina()`: Atualiza uma disciplina existente.
- `excluir_disciplina()`: Remove uma disciplina pelo código.

---

## 🏫 Gerenciamento de Turmas

### 📍 Menu: `menu_turmas()`

Recursos oferecidos:
- `adicionar_turma()`: Adiciona uma turma relacionando professor e disciplina.
- `listar_turmas()`: Lista todas as turmas existentes.
- `atualizar_turma()`: Edita uma turma já cadastrada.
- `excluir_turma()`: Exclui uma turma pelo código.

---

## 📑 Gerenciamento de Matrículas

### 📍 Menu: `menu_matriculas()`

Permite controlar as matrículas de alunos nas turmas:

- `adicionar_matricula()`: Realiza matrícula após verificar existência da turma e do aluno.
- `listar_matriculas()`: Mostra todas as matrículas.
- `atualizar_matricula()`: Altera dados de uma matrícula existente.
- `excluir_matricula()`: Remove a matrícula com base nos códigos da turma e do aluno.

---

## ✅ Funcionalidades Especiais

### 🔒 Validação de CPF

- **Função:** `validar_cpf(cpf)`
- **Descrição:** Valida a autenticidade do CPF com base no algoritmo oficial.

### 🗂️ Persistência de Dados

- Os dados são armazenados em arquivos JSON;
- Permite continuidade entre diferentes execuções do sistema.

---

## 👨‍💻 Interação com o Usuário

- Interface textual baseada em menus;
- Navegação simples e intuitiva;
- Mensagens explicativas e orientações em cada etapa.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Persistência:** Arquivos JSON
- **Execução:** Terminal (modo interativo)

---

## 📌 Requisitos

- Python 3 instalado
- Editor de código (VS Code, PyCharm, etc.)
- Terminal ou prompt de comando

---

## 📥 Execução

```bash
python nome_do_arquivo.py
