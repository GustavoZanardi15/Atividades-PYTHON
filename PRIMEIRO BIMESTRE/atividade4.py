"""1) Abstração com Funções e Dicionários

Abstrair diferentes operações de cálculo em funções reutilizáveis e usar mecanismos flexíveis como dicionários 
permite que os programas sejam mais dinâmicos e expansíveis. Implemente uma função chamada calculadora, que utiliza a 
abstração para realizar diferentes operações matemáticas (adição, subtração, multiplicação e divisão). 
A função deve receber como parâmetros:

- Uma string indicando a operação desejada ("adicionar", "subtrair", "multiplicar", "dividir");
- Dois números para realizar a operação.
Use um dicionário para mapear strings de operações a funções correspondentes. Caso o usuário passe uma operação inválida, 
a função deve retornar uma mensagem de erro.

Requisitos:

- Use funções separadas para cada operação.
- Use um dicionário para mapear as operações para as funções correspondentes.
- Caso a operação seja inválida, retorne "Operação inválida!".
"""



def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Divisão por zero inválida"  
    return a / b



acoes = {
    "adicionar": adicionar,  
    "subtrair": subtrair,
    "multiplicar": multiplicar,
    "dividir": dividir
}



def calculadora(acao, num1, num2):
    if acao in acoes:
        resultado = acoes[acao](num1, num2)
        return resultado
    else:
        return "Operação inválida"



print(calculadora("adicionar", 5, 3))   
print(calculadora("subtrair", 10, 4))   
print(calculadora("multiplicar", 7, 6)) 
print(calculadora("dividir", 8, 2))     
print(calculadora("dividir", 8, 0))     
print(calculadora("modulo", 10, 3))     
