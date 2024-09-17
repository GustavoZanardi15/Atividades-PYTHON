"""Atividade 1: Manipulação de Tuplas
Uma loja de eletrônicos quer armazenar informações sobre seus produtos em tuplas. 
Cada tupla contém três elementos: o nome do produto, o preço e a quantidade em estoque.

Escreva um programa em Python que:

Crie uma tupla para três produtos diferentes.Exiba o nome do produto mais caro.
Calcule o valor total em estoque (preço * quantidade) para cada produto e exiba o resultado.
"""

produtos = (
            ("Mouse", 250 , 50),
            ("Monitor", 2500.00 , 10),
            ("Cadeira Gamer", 5000.00, 5)
            )

produto_mais_caro = max(produtos, key=lambda produto : produto[1])
print(f"O produto mais caro é o {produto_mais_caro[0]}")


for nome, preco, quantidade in produtos:
    soma_dos_preco = preco * quantidade
    print(f"O valor total do produto, {nome} é R${soma_dos_preco:.2f}")

