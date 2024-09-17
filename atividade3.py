"""Atividade 3: Criando uma Classe para Gerenciar Alunos
Você deve criar um sistema de gerenciamento de alunos utilizando uma classe em Python.
 A classe Aluno deve armazenar informações sobre o nome do aluno, a idade e as notas em três disciplinas. 
 Além disso, a classe deve ter métodos para:

Calcular a média das notas.Determinar se o aluno foi aprovado ou reprovado (considerando média 7.0 como aprovação).
Exibir um resumo com o nome, idade, média e status de aprovação do aluno.
Passos:

1. Defina a classe Aluno com os atributos nome, idade e notas (uma lista com três notas).
2. Crie um método calcular_media que retorna a média das notas do aluno.
3. Crie um método verificar_aprovacao que retorna True se a média for maior ou igual a 7.0 e False caso contrário.
4. Crie um método exibir_resumo que exibe todas as informações do aluno, incluindo a média e o status de aprovação.
"""

class Aluno:
    def __init__(self, nome, idade , notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
      return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
       
       media = self.calcular_media()

       if media >= 70:
          return True
       else:
          return False
       
    def exibir_resumo(self):
       
       media = self.calcular_media()
       aprovado =  "Aprovado" if self.verificar_aprovacao else "Reprovado"
       print(f"O aluno {self.nome} de {self.idade} anos, com as notas {self.notas}, tem uma média de {media:.2f}, e o seu status de aprovação {aprovado}")
    

aluno1 = Aluno(nome="Gustavo Ulian Zanardi",idade=20 ,notas=[80, 62 , 94])
aluno1.exibir_resumo()