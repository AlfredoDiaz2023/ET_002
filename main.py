import numpy as np
from Funciones import *
from Asistente import *

arreglo = np.full((10,10),'---')
lista_asistente=[]
ciclo = True


def agregarAsistente(lista_asistente,numero_asiento):
    a = Asistente()
    a.rut = int(input("Ingrese Rut:"))
    a.numero_asiento = numero_asiento
    if numero_asiento>1 and numero_asiento<=20:
        valor=120000
    if numero_asiento>21 and numero_asiento<=50:
        valor=80000
    if numero_asiento>=51 and numero_asiento<=100:
        valor=50000
    lista_asistente.append(a)


def comprarEntrada(arreglo,lista_asistente):
    try:
                comprar=0
                compra=0
                mostrar(arreglo)
                numero_asiento = int(input("Numero de asiento:"))
                if numero_asiento>=1 and numero_asiento<=100:
                   disponible = comprobarAsiento(arreglo,numero_asiento)
                   if disponible == True:
                    agregarAsistente(lista_asistente,numero_asiento)
                    comprar(arreglo,numero_asiento)
                    compra = compra+1
                   else:
                        print("No esta disponible")
                else:
                   print("De 1 a 100 el NUmero de Asientos")
    except BaseException as error:
         print(f"Error:{error}")

def salir():
    print("Alfredo Diaz 06/07/2023")
    return False

llenar(arreglo)


def listarAsistentes(lista_asistente):
    for a in lista_asistente:
        print(f"Nombre:{a.nombre} Valor:{a.valor} Asiento:{a.num_asiento}")


def total(lista_asistente):
    platinum=0
    gold=0
    silver=0
    tot_platinum=0
    tot_gold=0
    tot_silver=0
    for a in lista_asistente:
        if int(a.valor)==120000:
            platinum=platinum+1
            tot_platinum=tot_platinum+120000
        if (a.valor)==80000:
            gold=gold+1
            tot_gold=tot_gold+80000
        if (a.valor)==50000:
            silver=silver+1
            tot_silver=tot_silver+50000
    print(f"Platinum: Cantidad:{platinum} Total:{tot_platinum}")
    print(f"Gold    : Cantidad:{gold} Total:{tot_gold}")
    print(f"Silver  : Cantidad:{silver} Total:{tot_silver}")

while ciclo:
    print(" Productora Creativos.cl")
    print("1) Comprar Entrada")
    print("2) Ubicaciones Disponibles")
    print("3) Ver Listado de Asistentes")
    print("4) Ganancias Totales")
    print("5) Salir")
    try:
        op=int(input("Seleccione (1-5):"))
        match op:
            case 1:
                comprarEntrada(arreglo,lista_asistente)
            case 2:
                mostrar(arreglo)
            case 3:
                listarAsistentes(lista_asistente)
            case 4:
                total(lista_asistente)
            case 5:
                ciclo = salir()
    except BaseException as error:
        print(f"Error:{error}")