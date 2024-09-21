"""3) Manipulação de Parâmetros Mutáveis e Imutáveis com Funções Aninhadas

Compreender como a passagem de parâmetros mutáveis e imutáveis funciona em Python é crucial para a construção de programas robustos. No entanto, 
o comportamento pode ser ainda mais interessante quando adicionamos funções aninhadas e o uso de diferentes tipos de dados. Implemente as seguintes funções:

- modificar_dicionario: Esta função deve receber um dicionário como parâmetro. Dentro dela, deve existir uma função aninhada chamada alterar_chave que altera o 
valor de uma chave específica do dicionário. A função externa deve chamar a função aninhada para modificar o dicionário.

- modificar_tupla: Esta função deve receber uma tupla como parâmetro e tentar alterar o valor de um dos elementos da tupla.
Teste as funções para verificar o comportamento de parâmetros mutáveis e imutáveis quando usados em funções aninhadas.

Requisitos:

- A função modificar_dicionario deve ser capaz de modificar o dicionário original, mesmo usando uma função aninhada.
- A função modificar_tupla não deve conseguir alterar a tupla, mas deve lidar com o erro de forma adequada e mostrar uma mensagem informando que tuplas são imutáveis.
- Teste ambas as funções e explique o comportamento observado.

"""


def modificar_dicionario(dic):
    def alterar_chave(chave, novo_valor):
        if chave in dic:
            print(f"Alterando {chave} de {dic[chave]} para {novo_valor}")
            dic[chave] = novo_valor
        else:
            print(f"A chave {chave} não existe no dicionário")


    alterar_chave = ('idade',30)
    return dic

def modificar_tupla(tupla):
    try:
       print(f"Tetando alterar o primeiro elemento da tupla de {tupla[0]} para 100.")
       tupla[0]=100
    except TypeError as e:
        print("Erro:",e)
        print("As tuplas são imutáveis e não podem ser alteradas")
    return tupla




if __name__ == "__main__":


    print("++++ Teste de modificação de dicionário ++++")

meu_dic = {
            'nome': 'Gustavo',
            'idade': 19,
            'cidade': 'Colorado'
        }

print(f"Dicionário original {meu_dic}" )

dicionario_modificado = modificar_dicionario(meu_dic)
print("Dicionário após a modificação ", dicionario_modificado)
print("++++ Fim do teste do dicionário ++++")

print("---- Teste da Tupla ----")

minha_tupla = (12 , 43, 2, 43)
print("Minha tupla original", minha_tupla)



tupla_modificada = modificar_tupla(minha_tupla)
print("Minha tupla alterada", minha_tupla)