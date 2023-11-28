# aula4 Python Turma 21 - 28/11/2023
# programa para retornar uma lista de dados a partir de um dicionário

# Apresentação
print('\n\t\t\t -- Cadastramento de Estudantes --\n')

# Entrada de dados
nome = input("Digite o nome do(a) estudante: ")
curso = input("Digite o curso do(a) estudante: ")
nota = float(input("Digite a nota (entre 0 e 100): "))
matricula = input("Situação da Matrícula? (Aberta/Trancada): ")

# Dicionário com os valores inseridos pelo usuário
dados_estudante = {'nome': nome, 'nota': nota, 'matricula': matricula, "curso": curso}

# Saída
print('\nCadastrado efetuado com sucesso', '\nEstudante: ', (dados_estudante['nome']),'\nCurso: ', (dados_estudante['curso']),
'\nNota: ', (dados_estudante['nota']), '\nSituação da Matrícula: ', (dados_estudante['matricula']))