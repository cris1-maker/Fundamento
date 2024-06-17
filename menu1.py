nombre=[]
asiento=12
def anularVuelo():
    nombre.clear()
def comprarPasaje ():
    
    print("Ingreso de datos")
    nombrePasajero=input("Ingrese nombre completo: ")
    nombre.append(nombrePasajero)
    while True:
        rutpasajero=int(input("Ingrese rut (sin guion): "))
        if rutpasajero > 1000000 and rutpasajero < 26000000:
            print("Rut guardado exitosamente.")
            nombre.append(rutpasajero)
            break
        else:
            print("Rut invalido.")
    while True:
        telefonoPasajero=int(input("Ingrese numero telefonico (con el digito 9 incluido): "))
        if telefonoPasajero > 100000000 and telefonoPasajero < 999999999:
            print("Numero telefonico guardado exitosamente.")
            nombre.append(telefonoPasajero)
            break
        else:
            print("Numero de telefono invalido")
def modificarDatosPasajero():
    while True:
        salir=input("Desea volver atras? (s/n): ")
        if salir=="s":
            break
        else:
            solAsiento=int(input("Ingrese su asiento: "))
            if solAsiento==asiento:
                solRut=int(input("Ingrese rut para verificar: "))
                if solRut==rutPasajero:
                    while True:
                        try:
                            print("1-Cambiar nombre")
                            print("2-Cambiar telefono")
                            print("3-Atras")
                            seleccion=int(input("Ingrese opcion: "))
                            if seleccion==1:
                                nuevoNombre=input("Ingrese un nuevo nombre: ")
                                nombrePasajero=nuevoNombre
                                print("Nombre actualizado.")
                            else:
                                if seleccion==2:
                                    while True: 
                                        try:
                                            nuevoTelefono=int(input("Ingrese nuevo numero: "))
                                            if nuevoTelefono > 100000000 and nuevoTelefono < 999999999:
                                                nuevoTelefono=telefonoPasajero
                                                print("Telefono actualizado")
                                                break
                                            else:
                                                print("Numero de telefono invalido")
                                        except:
                                            print("Ingrese solo numeros")
                                else:
                                    if seleccion==3:
                                        break
                        except:
                            print("Ingrese solo numeros.")
            else:
                print("Rut no enrrolado,vuelva a intentarlo")
while True:
    try:
        print("1-Ver asientos disponibles")
        print("2-Comprar asiento")
        print("3-Anular vuelo")
        print("4-Modificar datos pasajero")
        print("5-Salir")
        opcion=int(input("Ingrese opcion: "))
        if opcion==1:
            print
        else:
            if opcion==2:
                comprarPasaje()
                print(nombre)
            else:
                if opcion==3:
                    anularVuelo()
                    print(nombre)
                else:
                    if opcion==4:
                        modificarDatosPasajero()
                    else:
                        if opcion==5:
                            print("Gracias por su visita.")
                            break
                        else:
                            print("Ingrese opcion valida.")    
    



    except ValueError:
        print("Ingrese un numero.")