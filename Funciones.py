import numpy as np
def llenar(arreglo):
    x=0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if len(str(x))<3:
                arreglo[f][c]='0'+str(x)
            else:
                arreglo[f][c] = str(x)


def mostrar(arreglo):
    for f in range(10):
        fila = ''
        for c in range(10):
            if c == 3:
               fila = fila +'|'+arreglo[f][c]
            else:
                fila = fila + '|' + arreglo[f][c]
        print(fila)

def comprar(arreglo,numero_asiento):
    x =0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(numero_asiento):
                arreglo[f][c]='XXX'
def comprobarAsiento(arreglo,numero_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(numero_asiento):
                if arreglo[f][c]=='XXX':
                    return False
    return True



