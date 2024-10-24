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

pyDatalog.create_terms('X,Y, selvagem,Ele_come')

+Ele_come('')