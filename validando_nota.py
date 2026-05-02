#Crie uma função validar_nota que lança exceções se:
#A nota não for um número (TypeError)
#A nota for menor que 0 ou maior que 10 (ValueError)

def validar_nota(nota):
    if not isinstance(nota, (int, float)):
        raise TypeError(f"A nota deveser um número, {type(nota).__name__}")
    if nota < 0:
        raise ValueError(f"A nota não pode ser negativa, recebido: {nota}")
    if nota > 10:
        raise ValueError(f"A nota não pode ser maior que 10, recebido: {nota}")
    


# Testando
print(f"Nota 8.5: {validar_nota(8.5)}")
print(f"Nota 0: {validar_nota(0)}")
print(f"Nota 10: {validar_nota(10)}")