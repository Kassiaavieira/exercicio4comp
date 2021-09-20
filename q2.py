import re
def fraselista():
    frase = input("Digite uma frase: ")
    return re.sub(r'a', 'o', frase)


print(fraselista())