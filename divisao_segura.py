"""
Crie uma função dividir_seguro que recebe dois números e retorna a divisão, 
tratando o erro de divisão por zero.
"""

def dividir_seguro(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
        return None
    except TypeError:
        print("Erro: Os valores devem ser números!")
        return None

#testando
print(f"10 / 2 = {dividir_seguro(10, 2)}")
print(f"10 / 0 = {dividir_seguro(10, 0)}")
print(f"10 / 'abc' = {dividir_seguro(10, 'abc')}")


    
    