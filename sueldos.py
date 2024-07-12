from os import system
system("cls")

import csv

from random import randint



trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
salario = []

sueldos = []


lista1 = []
lista2 = []
lista3 = []




def random():
    for i in range(10):
        num = randint(350000,2500000)
        salario.append(num)

def asignar():
    for i in range(10):
        sueldos.append({'nombre':trabajadores[i], 'sueldo':salario[i]})
        
    print("\n-- Sueldos creados aleatoriamente --")

def clasificar():

    try:
        for i in range(10):
            if sueldos[i]['sueldo'] < 800000:
                sueldos[i] = [sueldos[i]]
                lista1.append(sueldos[i])
                        
            elif sueldos[i]['sueldo'] >= 800000 and sueldos[i]['sueldo'] <= 2000000:
                sueldos[i] = [sueldos[i]]
                lista2.append(sueldos[i])
                        
            elif sueldos[i]['sueldo'] > 2000000:
                sueldos[i] = [sueldos[i]]
                lista3.append(sueldos[i])
        
    except:
        print("No se han registrado los sueldos")
            
            
    print("-"*40)
    print()   
    print(f"Sueldos menores a $800.000\nTOTAL: {len(lista1)}")
    for i in lista1:
        for j in i:
            print(f"{j['nombre']}\t${j['sueldo']}")

    print("-"*40)
    print()
    print(f"Sueldos entre $800.000 y $2.000.0000\nTOTAL: {len(lista2)}")
    for i in lista2:
        for j in i:
            print(f"{j['nombre']}\t${j['sueldo']}")

    print("-"*40)
    print()
    print(f"Sueldos superiores a $2.000.000\nTOTAL: {len(lista3)}")
    for i in lista3:
        for j in i:
            print(f"{j['nombre']}\t${j['sueldo']}")
    print()
    print("-"*40)
        
def estadisticas():
    lista1.reverse()
    
    salario.sort()

    print("-"*40)
    save = []
    
    for i in lista3:
        print(f"Sueldo mas mayor:\n{i[0]['nombre']}\t${i[0]['sueldo']}")
        break
    
    print("-"*40)
    for i in lista1:
        print(f"Sueldo mas menor:\n{i[0]['nombre']}\t${i[0]['sueldo']}")
        break
    print("-"*40)
    suma = 0
    for i in range(10):
        suma += salario[i]
        promedio = suma / len(salario)
    print(f"El promedio de todos los sueldos es: ${round(promedio)}")

def reporte():
    pass
        

def main():
    x = True
    while x == True:
        
        print("\n1. Asignar sueldos aleatorios",
              "\n2. Clasificar sueldos",
              "\n3. Ver estadisticas",
              "\n4. Reporte sueldos",
              "\n5. Salir del programa")

        op = input("\nIngrese su opcion: ")

        if op == "1":
            asignar()
        elif op == "2":
            clasificar()
        elif op == "3":
            estadisticas()
        elif op == "4":
            reporte()
        elif op == "5":
            print("Saliendo del programa... Desarrollado por Nelson Cofré RUT 21.449.682-8")
        else:
            print("Opcion incorrecta. Intentelo nuevamente")

random()
main()

