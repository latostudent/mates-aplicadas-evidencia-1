# Resolución de problemas

# Importación de librerias
import math
valorPi = math.pi
import time

# Ciclo para poder regresar al menu y elegir una opcion diferente
while (True):
# Entrada para elegir el problema:
# Se le pide al usuario que ingrese un numero para determinar 
# que tipo de calculo se debe ejecutar
    print("Elige el número que corresponda al problema que desea resolver:")
    print("[1] Calcular el volumen de una esfera")
    print("[2] Obtener promedio de notas")
    print("[3] Calcular salario y bonificación")
    print("[4] Salir")
    print("Ingrese el número y presione enter:")
    eleccion = input()

    # Problema 1: Calcular el volumen de una esfera
    # Se ejecuta el problema 1 si se ingresa el número 1
    if eleccion == "1":
        #entrada Problema 1
        print("Ha elegido calcular el volumen de una esfera")
        print("Ingrese el radio de su esfera:")
        radio = float(input())
    #proceso problema 1
        volumen = (4*valorPi*(radio**3))/3
    #salida problema 1
        print("El volumen de la esfera es: ", volumen)
        print(".........")
        print("cargando.........")
        time.sleep(2) # espera en segundos
    # Problema 2: Obtener promedio de notas
    # Se ejecuta el problema 2 si se ingresa el número 2
    elif eleccion == "2":
    #entrada problema 2
        print("Ha elegido calcular su promedio de notas")
        print("Ingrese su nota de la evidencia 1:")
        nota1 = float(input())
        print("Ingrese su nota de la evidencia 2:")
        nota2 = float(input())
        print("Ingrese su nota de la evidencia 3:")
        nota3 = float(input())
        print("Ingrese su nota de la evidencia 4:")
        nota4 = float(input())
    #proceso problema 2
        promedio = (nota1+nota2+nota3+nota4)/4
    #salida problema 2
        print("Su promedio de notas este ciclo es:", promedio)
        print(".........")
        print("cargando.........")
        time.sleep(2) # espera en segundos
    # Problema 3: Calcular salario y bonificación
    # Se ejecuta el problema 3 si se ingresa el número 3
    elif eleccion == "3":
        #entrada problema 2
        print("Ha elegido calcular su salario bruto, salario neto y su bonificación")
        print("Ingrese la tarifa por hora de su contrato laboral:")
        tarifahora = float(input())
        print("Ingrese el número de horas que usted trabajo el mes pasado:")
        cantidadhoras = float(input())
    #proceso problema 2
        porcentajeAporte = 10
        porcentajeBonificacion = 10
        salariobrutoSinBonif = tarifahora*cantidadhoras
        montobonificacion = (salariobrutoSinBonif*porcentajeBonificacion)/100
        salariobrutoConBonif = salariobrutoSinBonif+montobonificacion
        montoaporte = (salariobrutoConBonif*porcentajeAporte)/100
        salarioneto = salariobrutoConBonif-montoaporte
    #salida problema 3
        print("Salario bruto sin bonificaciones:", salariobrutoSinBonif)
        print("Total bonificación del mes:", montobonificacion)
        print("Salario bruto con bonificación", salariobrutoConBonif)
        print("Deducción, aporte AFP:", montoaporte)
        print("salario neto", salarioneto)
        print(".........")
        print("cargando.........")
        time.sleep(2) # espera en segundos
    elif eleccion == "4":
        print("Gracias por usar nuestro programa, hasta luego.")
        break
    #si se ingresa una opcion invalida del menu, se le indica el error al usuario
    else:
        print("Ha ingresado una opción invalida, por favor intente nuevamente")
        print(".........")
        print("cargando.........")
        time.sleep(2) # espera en segundos
