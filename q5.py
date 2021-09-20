import re
def fraselista():
    frase = input("Digite uma frase: ")
    return re.findall(r'[0-9]+\.[0-9]+', frase)



print(fraselista())