import json
import time 
import menu

def agregar_autor():
    with open("biblioteca.json", mode="r") as archivoBiblioteca:
        leerJson = json.load(archivoBiblioteca)
        agregarJson = {
            "AutorID": input("Ingrese Id de autor"),
            "Nombre" : input("Ingrese nombre"),
            "nacionalidad" : input("Ingrese nacionalidad")
        }
        nuevaLista = leerJson[:]
        nuevaLista.append(agregarJson)
    with open("biblioteca.json", mode="r") as archivoBiblioteca:
        json.dump(nuevaLista, archivoBiblioteca, ident=4)
        print("Producto agregado exitosamente")
        time.sleep(3)

def actualizar_autor():
    with open("biblioteca.json", mode="r") as archivoBiblioteca:
        leerJson = json.load(archivoBiblioteca)
        id = input("Ingrese ID de autor a actualizar")
        productoActualizado = False
        for producto in leerJson:
            if producto["AutorID"] == id:
                producto["AutorID"] = input("Ingrese nevo ID")
                producto["Nombre"] = input("Ingrese nuevo Nombre")
                producto["Nacionalidad"] = input("INgrese nueva nacionalidad")
                productoActualizado = True
                break
            if productoActualizado:
                archivoBiblioteca.seek(0)
                json.dump(leerJson, archivoBiblioteca, ident=4)
                archivoBiblioteca.truncate()
                print(f"Autor {producto}")
                time.sleep(3)

def eliminar_autor():
    with open("biblioteca.json", mode="r") as archivoBiblioteca:
        leerJson = json.load(archivoBiblioteca)
        id = input("Ingrese ID de autor a eliminar")
        Autor = leerJson["AutorId"]
        autorEliminado = False
    for Autores in Autor:
        if Autores["id"] == id:
            Autores.remove(Autor)
            autorEliminado = True
            break
        if autorEliminado:
            archivoBiblioteca.seek(0)
            json.dump(leerJson, archivoBiblioteca, ident=4)
            archivoBiblioteca.truncate
            print("Autor eliminado correctamente")
            time.sleep(3)
        else:
            print("Autor no encontrado")
            time.sleep(3)

def listar_autores():
    with open("biblioteca.json", mode="r") as archivoBiblioteca:
        leerJson = json.load(archivoBiblioteca)
        for autor in leerJson["Autor"]:
            print(f"IDautor: {autor["AutorID"]} | Nombre: {autor["Nombre"]} | Nacionalidad: {autor["Nacionalidad"]} ")

def reporte_autores():
    with open("reportes.json", mode="w") as archivoBiblioteca:
        leerJson = json.load(archivoBiblioteca)
        lista_reportes = []
        for autor in leerJson["Autor"]:
            reporte = [f"IDautor: {autor["AutorID"]}"]
            lista_reportes.append(reporte)
            for libros in leerJson["Prestamo:"]:
                reporte_2 = [f"IDautor: {libros["PrestamoID"]}"]

reporte_autores()

    