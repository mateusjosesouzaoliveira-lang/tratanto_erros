"""Crie uma função que acessa um item de uma lista pelo índice, 
tratando o erro caso o índice não exista."""

def acessar_item(lista, indice):
    try:
        item = lista[indice]
        return item
    except IndexError:
        print(f"Erro: Índice {indice} está fora do range da lista!")
        print(f"A lista tem {len(lista)} elementos (índices de 0 a {len(lista)-1})")
        return None
    except TypeError:
        print("Erro: O primeiro argumento dese ser uma lista e o segundo um número inteiro!")


minha_lista = [10, 20, 30, 40, 50]
print(f"Acessando índice 2: {acessar_item(minha_lista, 2)}")
print(f"Acessando índice 10: {acessar_item(minha_lista, 10)}")

    
