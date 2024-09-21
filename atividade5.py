"""2) Passagem de Parâmetros e Funções de Alta Ordem

Funções de alta ordem são aquelas que recebem outras funções como parâmetros ou as retornam como resultado. 
Esse conceito pode ser útil na criação de funções genéricas e reutilizáveis. Implemente uma função chamada 
aplicar_operacao que recebe dois números e uma função como parâmetros. A função fornecida será aplicada aos dois números 
passados. Crie também uma função chamada gerar_operacao que, com base em uma string de operação ("soma", "multiplicacao"),
retorne a função apropriada.

Requisitos:

- A função aplicar_operacao deve receber uma função como parâmetro e aplicá-la aos dois números.
- A função gerar_operacao deve retornar a função correta com base na operação passada.
- Teste com operações de soma e multiplicação.
"""

def aplicar_operacao(num1 , num2, operacao):
    return operacao(num1, num2)

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def gerar_operacao(tipo_operacao):
    tipo_operacao = tipo_operacao.lower()
    if tipo_operacao == "soma":
        return soma
    elif tipo_operacao == "multiplicacao":
         return multiplicacao
    else:
        raise ValueError("Operação não encontrada")