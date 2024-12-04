def calcularPromedio(val1,val2,val3):
    calculo=val1+val2+val3
    promedio1=calculo/3
    return promedio1

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