print("Digite uma nota de 1 a 10 por favor:")
nota = int(input())
if(nota>=9):
  print("Voce tirou A")
elif(nota>=7):
  print("Voce tirou B")
elif(nota >= 5):
  print("Voce tirou C")
elif(nota<5):
  print("Voce foi reprovado")