"""Você está desenvolvendo um sistema que gerencia equipes de um projeto. Existem três equipes: 
Desenvolvimento, Marketing e Design. Crie os seguintes fatos:

- Alice e Bob estão na equipe de Desenvolvimento.
- Carol e David estão na equipe de Marketing.
- Eve está na equipe de Design.
Implemente as regras:

- Se uma pessoa está na equipe de Desenvolvimento ou Design, então ela trabalha com tecnologia.
- Se uma pessoa está na equipe de Marketing, então ela trabalha com comunicação.
Consultas:

1 - Liste todas as pessoas que trabalham com tecnologia.
2 - Verifique se Carol trabalha com comunicação.
3 - Liste todas as pessoas e o tipo de trabalho que realizam (tecnologia ou comunicação)."""

from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, equipe, trabalha_com')

+equipe('Alice','Desenvolvimento')
+equipe('Bob','Desenvolvimento')
+equipe('Carol','Marketing')
+equipe('David','Marketing')
+equipe('Eve','Design')


trabalha_com(X,'tecnologia')<=  equipe(X,'Desenvolvimento')
trabalha_com(X,'tecnologia')<= equipe(X,'Design')
trabalha_com(X,'comunicacao')<= equipe(X,'Marketing')


print("\nPessoas que trabalham com Tecnologia:")
print(trabalha_com(X,'tecnologia'))

print('\nCarol trabalha com comunicação?')
print(trabalha_com('Carol',Y))

print("\nLista de todas as pessoas e o tipo de trabalho que realizam:")
print(trabalha_com(X, Y))