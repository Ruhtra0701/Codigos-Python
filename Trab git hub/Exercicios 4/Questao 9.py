numeros = [1, 3, 2, 3, 4, 3]
remover = 3
resultado = []
for n in numeros:
    if n != remover:
        resultado.append(n)
print("Lista sem o número", remover, ":", resultado)