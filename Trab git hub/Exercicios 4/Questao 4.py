lista =[]
positivos = 0
negativos = 0
zeros = 0

while True:
  entrada = input()
  if entrada.lower() == "fim":
    break
  numero = float(entrada)
  lista.append(numero)
  if (numero>0):
    positivos +=1
  elif (numero<0):
    negativos += 1
  else:
    zeros+=1

print(f"quantidade de numeros positivos:{positivos}")
print(f"quantidade de numeros negativos{negativos}")
print(f"quantidade de zeros:{zeros}")