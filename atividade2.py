"""Atividade 2: Uso de Dicionários para Armazenar e Consultar Informações
Você é encarregado de criar um sistema simples de gerenciamento de informações de 
alunos usando dicionários. O sistema deve:

Armazenar o nome de três alunos e suas notas em um dicionário, onde o nome é a chave e a 
nota é o valor.Permitir que o usuário insira o nome de um aluno para consultar a nota.
Exibir a média das notas dos alunos armazenados."""


nota_alunos = {
               "gustavo" : 100,
               "alisson" : 78,
               "renan" : 80 
               }

aluno = input(f"Informe o nome do aluno que deseja ver a nota:").strip().lower()
if aluno in nota_alunos:
    print(f"A nota do aluno {aluno.capitalize()} é {nota_alunos[aluno]}")
else: 
    print(f"Aluno não encontrado no banco de dados")


    