def calcularPromedio(val1,val2,val3):
    calculo=val1+val2+val3
    promedio1=calculo/3
    return promedio1
<<<<<<< HEAD
def consultarMulta(numero): 
    if numero == 1:
        return 10 / 100 * 100
    elif numero == 2:
        return 15 / 100 * 100
    elif numero == 3:
        return 20 / 100 * 100
    elif numero == 4:
        return 30 / 100 * 100
    else:
        return -1 
=======

def consultarMulta(tipo1,tipo2,tipo3,tipo4,tipo5,tipo6):
    calculo= tipo1 + tipo2 
    porcentaje= calculo / 100
    return porcentaje

def calcularSubtotal(precioProducto: float, cantidad: int, porcentajeDescuento: float) -> float:
    # Calcular el subtotal sin descuento
    subtotalSinDescuento = precioProducto * cantidad

    # Calcular el valor del descuento
    descuento = (subtotalSinDescuento * porcentajeDescuento) / 100

    # Calcular el subtotal con descuento aplicado
    subtotal = subtotalSinDescuento - descuento

    return subtotal
>>>>>>> fb9531d206423de35f13620e6b268deaf94f5236
