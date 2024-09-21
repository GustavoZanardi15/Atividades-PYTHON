"""3) Manipulação de Parâmetros Mutáveis e Imutáveis com Funções Aninhadas

Compreender como a passagem de parâmetros mutáveis e imutáveis funciona em Python é crucial para a construção de programas robustos. No entanto, o comportamento pode ser ainda mais interessante quando adicionamos funções aninhadas e o uso de diferentes tipos de dados. Implemente as seguintes funções:

- modificar_dicionario: Esta função deve receber um dicionário como parâmetro. Dentro dela, deve existir uma função aninhada chamada alterar_chave que altera o valor de uma chave específica do dicionário. A função externa deve chamar a função aninhada para modificar o dicionário.
- modificar_tupla: Esta função deve receber uma tupla como parâmetro e tentar alterar o valor de um dos elementos da tupla.
Teste as funções para verificar o comportamento de parâmetros mutáveis e imutáveis quando usados em funções aninhadas.

Requisitos:

- A função modificar_dicionario deve ser capaz de modificar o dicionário original, mesmo usando uma função aninhada.
- A função modificar_tupla não deve conseguir alterar a tupla, mas deve lidar com o erro de forma adequada e mostrar uma mensagem informando que tuplas são imutáveis.
- Teste ambas as funções e explique o comportamento observado.

"""