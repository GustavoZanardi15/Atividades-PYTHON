"""Atividade 1: Manipulação de Tuplas
Uma loja de eletrônicos quer armazenar informações sobre seus produtos em tuplas. 
Cada tupla contém três elementos: o nome do produto, o preço e a quantidade em estoque.

Escreva um programa em Python que:

Crie uma tupla para três produtos diferentes.Exiba o nome do produto mais caro.
Calcule o valor total em estoque (preço * quantidade) para cada produto e exiba o resultado.
"""

produtos=(
        ('Monitor', 1500 ,10),
        ('Placa de video', 3000 ,5),
        ('Mouse', 250 ,50)   
)

produto_mais_caro = max(produtos, key=lambda  produto: produto[1])
print(f"O produto mais caro em estoque é {produto_mais_caro[0]}")



for produto in produtos:
    nome, valor, quantidade = produto
    valor_total = valor * quantidade
    print(f"O  valor total do {nome} é de R${valor_total:.2f}")