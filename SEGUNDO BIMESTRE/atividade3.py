"""Imagine que você está desenvolvendo um sistema para monitorar animais em um zoológico. Defina os seguintes fatos:

- Tigre, Leão e Urso são carnívoros.
- Girafa, Elefante e Zebra são herbívoros.
Implemente as regras:

- Se um animal é carnívoro, ele come carne.
- Se um animal é herbívoro, ele come plantas.
- Um animal é selvagem se ele for carnívoro ou herbívoro.
Consultas:

1 - Verifique se existe algum animal que come plantas.
2 - Liste todos os animais que são selvagens.
3 - Verifique se todos os carnívoros são selvagens.

Dicas:
Use quantificadores existenciais (para verificar se algum animal é herbívoro) e universais 
(para checar se todos os carnívoros são selvagens).
"""
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, selvagem, Ele_come')


+Ele_come('Tigre', 'carne')
+Ele_come('Leão', 'carne')
+Ele_come('Urso', 'carne')
+Ele_come('Girafa', 'plantas')
+Ele_come('Elefante', 'plantas')
+Ele_come('Zebra', 'plantas')

Ele_come(X, 'carne') <= (X == 'Tigre')
Ele_come(X, 'carne') <= (X == 'Leão')
Ele_come(X, 'carne') <= (X == 'Urso')

Ele_come(X, 'plantas') <= (X == 'Girafa')
Ele_come(X, 'plantas') <= (X == 'Elefante')
Ele_come(X, 'plantas') <= (X == 'Zebra')


selvagem(X) <= Ele_come(X, 'carne')
selvagem(X) <= Ele_come(X, 'plantas')


print('\nAnimais que comem plantas:')
print(Ele_come(X, 'plantas'))

print('\nAnimais selvagens:')
print(selvagem(X))

carnivoros = Ele_come(X, 'carne')
todos_carnivoros_selvagens = all(selvagem(c[0]) for c in carnivoros.data)

print('\nTodos os carnívoros são selvagens?')
print(todos_carnivoros_selvagens)