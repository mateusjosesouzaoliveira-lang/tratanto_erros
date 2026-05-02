#Calcular Média com Tratamento Completo

def calcular_media_completo(notas):
    print("Iniciando cálculo...")
    try:
        if len(notas) == 0:
            raise ValueError("Lista de notas vazia!")
        media = sum(notas) / len(notas)
    except ValueError as erro:
        print(f"Erro: {erro}")
        return None
    except TypeError:
        print("Erro: As notas devem ser uma lista!")
        return None
    else:
        print("Cálculo realizado com sucesso!")
        return media
    finally:
        print("Processo finalizado!")

# Testar
print("--- Notas válidas ---")
resultado1 = calcular_media_completo([8.5, 7.0, 9.0])
print(f"Média: {resultado1}")
print()
print("--- Lista vazia ---")
resultado2 = calcular_media_completo([])
print(f"Média: {resultado2}")

