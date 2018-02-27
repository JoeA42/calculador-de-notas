# se importa la libreria os
import os
# se asgina la variable restart1 para el primer loop
restart1=True
# se abre el primer loop
while restart1!="n":
    # se toma el dato de la prueba y se crea un documento de texto con su nombre
    prueba = input("Prueba: ")
    documento = prueba+'.txt'
    datos = os.open(documento, os.O_RDWR|os.O_CREAT)
    # se abre este documento
    registro = open(documento,'r')
    # se asigna la variable restart2 para el segundo loop
    restart2=True
    # se abre el segundo loop
    while restart2!="n":
        # se toman los datos del estudiante
        nombre = input("Nombre de estudiante: ")
        puntosTotales = int(input("Puntos totales de prueba: "))
        puntosObtenidos = int(input("Puntos obtenidos: "))
        # se calcula la nota
        nota = (puntosObtenidos/puntosTotales)*100
        # se escriben los datos en el documento
        registro = open(documento,'a')
        registro.write("Estudiante: " + nombre +" - Nota obtenida: "+str(nota)+ '\n')
        # se imprime mensaje con nombre, nota y se indica que se han guardado los datos
        print ("Estudiante: " + nombre +" - Nota obtenida: "+str(nota) + " -DATOS GUARDADOS-")
        # se cierra el documento
        registro.close()
        # se toma un dato para cerrar el primer loop
        restart2 = input("Desea ingresar otro ESTUDIANTE? ('s' para continuar 'n' para salir)")
    # se toma un dato para cerrar el segundo loop
    restart1 = input("Desea ingresar otra PRUEBA? ('s' para continuar 'n' para salir)")
# se cierra el documento
os.close( datos )
