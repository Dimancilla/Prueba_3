import funciones
import os
import time
import json
funciones

def mantenedor():
    opcMenu = -1
    while opcMenu != 0:
        print("\nMenú:")
        print("***********************************")
        print("*          BIBLIOTECA             *")
        print("***********************************")
        opcMenu = int(input("1] Agregar Autor\n2] Actualizar Autor\n3] Eliminar Autor\n4] Listar Autores\n0] Salir\n***********************************\nElija opción: "))
        os.system("cls")
        if opcMenu == 1:
            agregar_autor()
            os.system("cls")
        elif opcMenu == 2:
            actualizar_autor()
            os.system("cls")
        elif opcMenu == 3:
            eliminar_autor()
            os.system("cls")
        elif opcMenu == 4:
            listar_autores()
            input("ENTER PARA CONTINUAR")
            os.system("cls")
        elif opcMenu == 0:
            print("Saliste exitosamente")
            time.sleep(3)
            os.system("cls")
            break
        else:
            print("Opción inválida,intente de nuevo.")
            time.sleep(3)
            os.system("cls")

def main_menu():
    opcMenu = -1
    while opcMenu != 0:
        print("\nMenú:")
        print("***********************************")
        print("*          MUNDOLIBRO             *")
        print("***********************************")
        opcMenu = int(input("1] Mantenedor de autores\n2] Reportes \n0] Salir\n***********************************\nElija opción: "))
        os.system("cls")
        if opcMenu == 1:
            mantenedor()
            os.system("cls")
        elif opcMenu == 2:
            reporte_autores()
            os.system("cls")
        elif opcMenu == 0:
            print("Saliste exitosamente")
            time.sleep(3)
            os.system("cls")
            break
        else:
            print("Opción inválida,intente de nuevo.")
            time.sleep(3)
            os.system("cls")

main_menu()

    

