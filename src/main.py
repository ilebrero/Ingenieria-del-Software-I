from Filtracion import *
from datos import *
from Cartografo import *
import sys

def imprimir(bar):
  opcion_valida = 0

  while not opcion_valida:
    print("\n" + bar.mostrar_con_calificacion(registro) + "\n")
    print("¿Desea ver la ubicación del bar en un mapa?")
    print("1. Si")
    print("2. Volver al menu principal")

    opcion = int(input("Ingrese un número: "))

    if opcion == 1:
      cartografo.marcar_en_mapa(bar)
      cartografo.mostrar_mapa()
      opcion_valida = 1
    elif opcion == 2:
      print("\n")
      opcion_valida = 1

def imprimir_nombres(bares):
  nombre_valido = 0

  while not nombre_valido:
    print("\nBares disponibles: ")
    for bar in bares.listar():
      print("- " + bar.nombre)
    print("\n¿Desea ver el detalle de algún bar? (Ingrese 0 para volver al menú principal)")

    nombre_de_bar = str(input("Ingrese el nombre: "))

    if not nombre_de_bar == "0":
      for bar in bares.listar():
        if bar.nombre == nombre_de_bar:
          imprimir(bar)
          nombre_valido = 1

      if not nombre_valido:
        print("\nSeleccione un nombre válido")
    else:
      print("\n")
      nombre_valido = 1

def opciones_filtrar(bares):
  print("Seleccione una opción de filtro: ")
  print("1. Por calificación")
  print("2. Por ubicación")
  opcion = int(input("Ingrese el número: "))

  if opcion == 1:
    print("Características disponibles:")
    cs = list(Caracteristica.todas())
    for i, c in enumerate(cs):
      print("{}. {}".format(i+1, c))
    opcion_caracteristica = int(input("Seleccione la característica: "))
    opcion_puntaje = float(input("Ingrese puntaje mínimo. Debe ser un valor entre 0 y 5: "))
    filtro = FiltracionCalificacion(bares, registro, cs[opcion_caracteristica-1], opcion_puntaje)

  elif opcion == 2:
    direccion = input("Ingrese dirección: ")
    try:
        radio = int(input("Ingrese radio de distancia [400]: ")) #reformular
    except ValueError:
        radio = 400
    if not (0 <= radio):
      raise Exception("El radio debe ser mayor a cero")
    #radio => 0
    filtro = FiltracionDireccion(bares, registro, direccion, radio)

  print("Seleccione siguiente acción:")
  print("1. Añadir un filtro")
  print("2. Ver resultados")
  opcion2 = int(input("Ingrese el número: "))

  if opcion2 == 1:
    opciones_filtrar(filtro)

  elif opcion2 == 2:
    imprimir_nombres(filtro)

def menu():
  print("Seleccione una opción: ")
  print("1. Listar todos los bares")
  print("2. Filtrar bares")
  opcion = int(input("Ingrese el número: "))
  
  if opcion == 1:
    imprimir_nombres(directorio)
  elif opcion == 2:
    opciones_filtrar(directorio)

def main():
  try:
    while True:
      menu()
  except (EOFError, KeyboardInterrupt):
    pass

if __name__ == '__main__':
  main()
