from Filtracion import *
from datos import *
import sys

def imprimir(bares):
  for bar in bares.listar():
    print(bar.str_con_calificacion(registro))

def opciones_filtrar():
  print("Seleccione una opción de filtro: ")
  print("1. Por WI-FI")
  print("2. Por ubicación")
  opcion = int(input("Ingrese el número: "))

  if opcion == 1:
    opcion_filtrado = 8
    while not (0 <= opcion_filtrado <= 5):
      opcion_filtrado = float(input("Ingrese cantidad de estrellas mínima. Debe ser un valor entre 0 y 5: "))
    filtro = FiltracionCalificacion(directorio, registro, wifi, opcion_filtrado)
    imprimir(filtro)

  elif opcion == 2:
    ubicacion = input("Ingrese ubicación: ")
    radio = int(input("Ingrese la cantidad de metros en la que quiere filtrar bares: ")) #reformular
    if not (0 <= radio):
      raise Exception("El radio debe ser mayor a cero")
    #radio => 0
    filtro = FiltracionUbicacion(directorio, registro, ubicacion, radio)
    imprimir(filtro)

  opciones_calificar(filtro)

def opciones_calificar(bares):
  opcion_valida = 0

  while not opcion_valida:
    print("¿Desea calificar algún bar?")
    print("1. Si")
    print("2. Volver al menú principal")
    opcion = int(input("Ingrese el número: "))

    if opcion == 1:
      opciones_bares(bares)
      opcion_valida = 1
    elif opcion == 2:
      opcion_valida = 1
    else:
      print("\nSeleccione una opción válida")

def opciones_bares(bares):
  nombre_valido = 0

  while not nombre_valido:
    print("\nNombres disponibles: ")
    for bar in bares.listar():
      print(" -" + bar.nombre)
    print("\nIngrese 0 para volver al menú principal")

    nombre_de_bar = str(input("Ingrese el nombre: "))

    if not nombre_de_bar == "0":
      for bar in bares.listar():
        if bar.nombre == nombre_de_bar:
          opciones_calificar_atributo(bar)
          nombre_valido = 1

      if not nombre_valido:
        print("\nSeleccione un nombre válido")
    else:
      nombre_valido = 1
  
def opciones_calificar_atributo(bar):
  atributo_valido = 0

  while not atributo_valido:
    print("\nAtributos disponibles: ")
    for atributo in bar.atributos:
      print(" -" + atributo.nombre)
    print("\nIngrese 0 para volver al menú principal")

    atributo_a_calificar = str(input("Ingrese el atributo que desea calificar: "))

    if not atributo_a_calificar == "0":
      for atributo in bar.atributos:
        if atributo.nombre == atributo_a_calificar:
          obtener_puntaje(bar, atributo)
          atributo_valido = 1
      
      if not atributo_valido:
        print("Seleccione un atributo existente")
    else:
      atributo_valido = 1

def obtener_puntaje(bar, atributo):
  puntaje_valido = 0

  while not puntaje_valido:
    puntaje = int(input("Ingrese un puntaje(0 a 5): "))
    
    if 0 <= puntaje <= 5:
      calificacion = Calificacion(bar, atributo, puntaje)
      registro.agregar(calificacion)
      puntaje_valido = 1
    else:
      print("Ingrese un puntaje válido")

def menu():
  print("Seleccione una opción: ")
  print("1. Listar todos los bares")
  print("2. Filtrar bares")
  opcion = int(input("Ingrese el número: "))

  if opcion == 1:
    imprimir(directorio)
    opciones_calificar(directorio)
  elif opcion == 2:
    opciones_filtrar()


def main():
  try:
    while True:
      menu()
  except (EOFError, KeyboardInterrupt):
    pass

if __name__ == '__main__':
  main()
