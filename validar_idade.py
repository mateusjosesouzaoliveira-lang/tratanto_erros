#Crie uma função validar_idade que lança ValueError se a idade for negativa ou maior que 150.

def validar_idade(idade):
    if not isinstance(idade, int):
        raise TypeError("Idade deve ser um número inteiro!")
    if idade < 0:
        raise ValueError(f"Idade não pode ser negativo, recebido: {idade}")
    if idade > 150:
        raise ValueError(f"Idade não pode ser maior que 150, recebido: {idade}")
    return idade

print(f"Idade 25: {validar_idade(25)}")
print(f"Idade 0: {validar_idade(0)}")
print(f"Idade 150: {validar_idade(150)}")
