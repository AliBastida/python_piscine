import sys

frase = ""
for word in sys.argv[1:]: #word es el iterador en la lista
    frase = frase + word + " "
print (frase.swapcase()[::-1][1:])

"""
def rev_alpha(argumentos): #argumentos = lista
    frase = ""
    for word in argumentos: #word es el iterador en la lista
        frase = frase + word + " "
    print (frase.swapcase()[::-1][1:])

rev_alpha(sys.argv[1:])
"""