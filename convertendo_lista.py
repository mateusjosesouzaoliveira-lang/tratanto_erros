#Crie uma função que converte lista de textos para números, tratando valores inválidos.

def converter_lista(llista_textos):
    numeros = []
    for texto in llista_textos:
        try:
            numero = float(texto)
            numeros.append(numero)
        except (ValueError, TypeError):
            print(f"Valor '{texto}' ignorado (não é um número válido)")


lista = ["10", "20.5" , "abc" ,"30", "xyz" , "40.2"]
resultado = converter_lista(lista)
print(f"Lista original: {lista}")
print(f"Números convertidos: {resultado}")
