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
    direccion = input("Ingrese dirección: ")
    try:
        radio = int(input("Ingrese radio de distancia [400]: ")) #reformular
    except ValueError:
        radio = 400
    if not (0 <= radio):
      raise Exception("El radio debe ser mayor a cero")
    #radio => 0
    filtro = FiltracionDireccion(directorio, registro, direccion, radio)
    imprimir(filtro)

  opciones_calificar(filtro)

def opciones_calificar(bares):
    opciones_bares(bares)

def opciones_bares(bares):
  nombre_valido = 0

  while not nombre_valido:
    print("\nNombres disponibles: ")
    for bar in bares.listar():
      print("- " + bar.nombre)
    print("\nIngrese 0 para volver al menú principal")

    nombre_de_bar = str(input("Ingrese el nombre: "))

    if not nombre_de_bar == "0":
      for bar in bares.listar():
        if bar.nombre == nombre_de_bar:
          opciones_calificar_caracteristica(bar)
          nombre_valido = 1

      if not nombre_valido:
        print("\nSeleccione un nombre válido")
    else:
      nombre_valido = 1
  
def opciones_calificar_caracteristica(bar):
  caracteristica_valido = 0

  while not caracteristica_valido:
    print("\ncaracteristicas disponibles: ")
    for caracteristica in bar.caracteristicas:
      print("- " + caracteristica.nombre)
    print("\nIngrese 0 para volver al menú principal")

    caracteristica_a_calificar = str(input("Ingrese la característica que desea calificar: "))

    if not caracteristica_a_calificar == "0":
      for caracteristica in bar.caracteristicas:
        if caracteristica.nombre == caracteristica_a_calificar:
          obtener_puntaje(bar, caracteristica)
          caracteristica_valido = 1
      
      if not caracteristica_valido:
        print("Seleccione una característica existente")
    else:
      caracteristica_valido = 1

def obtener_puntaje(bar, caracteristica):
  puntaje_valido = 0

  while not puntaje_valido:
    puntaje = int(input("Ingrese un puntaje(0 a 5): "))
    
    if 0 <= puntaje <= 5:
      calificacion = Calificacion(bar, caracteristica, puntaje)
      registro.agregar(calificacion)
      puntaje_valido = 1
    else:
      print("Ingrese un puntaje válido")

def menu():
  print("Seleccione una opción: ")
  print("1. Listar todos los bares")
  print("2. Filtrar bares")
  print("3. Calificar un bar")
  opcion = int(input("Ingrese el número: "))

  if opcion == 1:
    imprimir(directorio)
  elif opcion == 2:
    opciones_filtrar()
  elif opcion == 3:
    opciones_calificar(directorio)


def main():
  try:
    while True:
      menu()
  except (EOFError, KeyboardInterrupt):
    pass

if __name__ == '__main__':
  main()
