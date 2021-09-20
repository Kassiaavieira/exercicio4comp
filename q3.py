import re
def fraselista():
    frase = input("Digite uma frase: ")
    return re.sub(r'(\w)\b', r'\1s', frase)

print(fraselista())