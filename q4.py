import re
def fraselista():
    frase = input("Digite uma frase: ")
    return re.sub(r'[0-9]+', lambda x: str(int(x.group()) + 1), frase)



print(fraselista())