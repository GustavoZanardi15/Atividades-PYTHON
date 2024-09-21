"""Atividade 1: Manipulação de Tuplas
Uma loja de eletrônicos quer armazenar informações sobre seus produtos em tuplas. 
Cada tupla contém três elementos: o nome do produto, o preço e a quantidade em estoque.

Escreva um programa em Python que:

Crie uma tupla para três produtos diferentes.Exiba o nome do produto mais caro.
Calcule o valor total em estoque (preço * quantidade) para cada produto e exiba o resultado.
"""

produtos=(
            ('Monito', 1.500, 10),
            ('Placa de video', 3.000, 5),
            ('Mouse', 250, 50)   
        )

produto_mais_caro = max(produtos, key=lambda  produto:produto[0])
print(f"O produto mais caro em estoque é {produto_mais_caro[0]}")



