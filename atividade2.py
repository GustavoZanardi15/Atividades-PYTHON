"""Atividade 2: Uso de Dicionários para Armazenar e Consultar Informações
Você é encarregado de criar um sistema simples de gerenciamento de informações de 
alunos usando dicionários. O sistema deve:

Armazenar o nome de três alunos e suas notas em um dicionário, onde o nome é a chave e a 
nota é o valor.Permitir que o usuário insira o nome de um aluno para consultar a nota.
Exibir a média das notas dos alunos armazenados."""


notas_alunos = {
                "Gustavo": 80,
                "Renan": 70,
                "Alisson": 90
               }

aluno = input(f"Insira o nome do aluno que deseja saber a nota:")

if aluno in notas_alunos:
    print(f"A nota do aluno {aluno} é: {notas_alunos[aluno]}")
else:
    print(f"Aluno não encontrado")


alunos = sum(notas_alunos.values())
quant_alunos = len(notas_alunos)
media_alunos = alunos / quant_alunos
print(f"A média dos alunos é {media_alunos}")
    