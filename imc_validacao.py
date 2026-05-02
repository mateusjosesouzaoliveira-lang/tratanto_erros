#Crie uma função para calcular IMC com validação completa usando try/except e raise.

def calcular_imc_seguro(peso, altura):
    try:
        peso_float = float(peso)
        altura_float = float(altura)
        
        if peso_float <= 0:
            raise ValueError("Peso deve ser maior que zero!")
        if altura_float <= 0:
            raise ValueError("Altura deve ser maior que zero!")
        
        imc = peso_float / (altura_float ** 2)
        return imc
    except ValueError as erro:
        print(f"Erro de valor: {erro}")
        return None
    except TypeError:
        print("Erro: Peso e altura devem ser números!")
        return None
    except ZeroDivisionError:
        print("Erro: Altura não pode ser zero!")
        return None

#testando
print(f"IMC (70kg, 1.75m): {calcular_imc_seguro(70, 1.75):.2f}")
print(f"IMC (70kg, 0m): {calcular_imc_seguro(70, 0)}")
print(f"IMC ('abc', 1.75): {calcular_imc_seguro('abc', 1.75)}")

