import re
def fraselista():
    frase = input("Digite uma frase: ")
    return len(re.findall(r'a', frase)) % 2 != 0



print(fraselista())