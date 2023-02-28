"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

frase = input("Digite uma frase: ")

fraseInvertida = ""
for i in range(len(frase) - 1, -1, -1):
    fraseInvertida += frase[i]

print(f"Frase invertida: {fraseInvertida}")

