#PROGRAMA PARA CONVERTIR MONEDAS
#VERSION 1.0

opcion = 0

while(opcion != 3):
    print(
    """
    =======================================
            CONVERTIDOR DE MONEDAS
    =======================================
    OPCIÓN 1 : convertir de soles a dolares
    OPCIÓN 2 : convertir de dolares a soles
    OPCIÓN 3 : salir del programa
    =======================================
    """)
    opcion = int(input("ingrese la opción que desee : "))
    if(opcion == 1):
        montoOrigen = float(input("ingrese monto en soles : "))
        montoDestino = montoOrigen / 3.8
        print("El monto en dolares es " + str(montoDestino))
    elif(opcion == 2):
        montoOrigen = float(input("ingrese monto en dolares : "))
        montoDestino = montoOrigen * 3.8
        print("El monto en soles es : " + str(montoDestino))
    elif(opcion == 3):
        print("ADIOS!!!!")
    else:
        print("debe marcar una opción valida ...")