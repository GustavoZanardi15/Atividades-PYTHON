def modificar_dicionario(dic):
    def alterar_chave(chave, novo_valor):
        if chave in dic:
            print(f"Alterando '{chave}' de {dic[chave]} para {novo_valor}")
            dic[chave] = novo_valor
        else:
            print(f"A chave '{chave}' não existe no dicionário.")

    # Chamada correta da função alterar_chave
    alterar_chave('idade', 30)
    return dic

def modificar_tupla(tupla):
    try:
        print(f"Tentando alterar o primeiro elemento da tupla de {tupla[0]} para 100.")
        tupla[0] = 100  # Isso causará um erro
    except TypeError as e:
        print("Erro:", e)
        print("As tuplas são imutáveis e não podem ser alteradas.")
    return tupla

if __name__ == "__main__":
    print("++++ Teste de modificação de dicionário ++++")
    
    meu_dic = {
        'nome': 'Gustavo',
        'idade': 19,
        'cidade': 'Colorado'
    }
    print(f"Dicionário original: {meu_dic}")
    
    dicionario_modificado = modificar_dicionario(meu_dic)
    print(f"Dicionário após a modificação: {dicionario_modificado}")
    print("++++ Fim do teste do dicionário ++++")
    
    print("\n---- Teste da Tupla ----")
    
    minha_tupla = (12, 43, 2, 43)
    print(f"Minha tupla original: {minha_tupla}")
    
    tupla_modificada = modificar_tupla(minha_tupla)
    print(f"Minha tupla após tentativa de modificação: {tupla_modificada}")
