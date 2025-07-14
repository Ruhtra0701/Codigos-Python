def main():
  numero = valida_num()
  escreva_miau(numero)
def valida_num():
  while True:
    n = int(input("Qual o valor de N? "))
    if(n>0):
      return n
def escreva_miau(vezes):
  for _ in range(vezes):
    print("miau")
main()