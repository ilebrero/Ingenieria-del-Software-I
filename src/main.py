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
    filtro = FiltracionUbicacion(directorio, registro, ubicacion)
    imprimir(filtro)

  
def menu():
  print("Seleccione una opción: ")
  print("1. Listar todos los bares")
  print("2. Filtrar bares")
  opcion = int(input("Ingrese el número: "))

  if opcion == 1:
    imprimir(directorio)
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
