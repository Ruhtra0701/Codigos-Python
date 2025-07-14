quantidade = int(input("Quantos números você quer somar? "))
soma = 0

for _ in range(quantidade):
    numero = float(input("Digite um número: "))
    soma += numero

print("Soma total:", soma)