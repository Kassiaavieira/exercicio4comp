import re
def fraselista():
    frase = input("Digite uma frase: ")
    return len(re.findall(r'\(', frase)) == len(re.findall(r'\)', frase))



print(fraselista())