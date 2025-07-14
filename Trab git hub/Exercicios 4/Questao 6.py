palavras = ["casa", "bicicleta", "sol", "programacao"]
maior = palavras[0]
for palavra in palavras:
    if len(palavra) > len(maior):
        maior = palavra
print("Palavra mais longa:", maior)