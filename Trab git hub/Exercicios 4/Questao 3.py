lista =[]
for i in range(5):
  numeros = int(input())
  lista.append(numeros)
if lista:
  numeromaior=max(lista)
  numeromenor=min(lista)
print(numeromaior)
print(numeromenor)