"""Crie um sistema de predicados que represente a relação entre pessoas e suas nacionalidades. Defina os seguintes fatos:

- João é brasileiro.

- Anna é americana.

- Carlos é espanhol.

- Maria é brasileira.

Implemente as seguintes regras:

- Um brasileiro fala português.
- Um americano fala inglês.
- Um espanhol fala espanhol.
Faça consultas para:

1 - Saber quem fala português.
2 - Verificar se Carlos fala espanhol.
3 - Listar todas as pessoas e suas respectivas línguas.
Dicas:
Utilize predicados para definir nacionalidades e línguas.
Crie as regras para inferir as línguas baseadas nas nacionalidades.
"""

from pyDatalog import pyDatalog

pyDatalog.create_terms('X , Y , nacionalidade , idioma')

+nacionalidade('João', 'brasileiro')
+nacionalidade('Anna', 'americana')
+nacionalidade('Carlos', 'espanhol')
+nacionalidade('Maria', 'brasileiro')


idioma(X,'portugês')<= nacionalidade(X,'brasileiro')
idioma(X,'inglês')<= nacionalidade(X,'americana')
idioma(X,'espanhol')<= nacionalidade(X,'espanhol')



print("Quem fala português?:")
print(idioma(X,'portugês'))

print("Carlos fala espanhol?")
print(idioma('Carlos','espanhol'))

print(idioma(X,Y))


