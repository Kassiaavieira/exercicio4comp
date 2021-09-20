import re
def fraselista():
    frase = input("Digite uma frase: ")
    return re.sub(r'(\w+)\:\s(\w+)', r'\g<2>: \g<1>', frase)



print(fraselista())