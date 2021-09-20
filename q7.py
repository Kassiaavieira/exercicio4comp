import re
def fraselista():
    frase = input("Digite uma frase: ")
    return re.findall(r'\/\*.*\*\/', frase)



print(fraselista())