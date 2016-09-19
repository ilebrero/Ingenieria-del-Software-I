from DirectorioDeBares import *
from Bar import *
from Atributo import *
from Calificacion import *
from RegistroDeCalificaciones import *
from Filtracion import *
import sys

wifi = Atributo("Wi-Fi")
atributos = [wifi]

directorio = DirectorioDeBares()

bar1 = Bar("Tienda del cafe", "Santa Fe y Callao", atributos)
bar2 = Bar("Cafe Martinez", "Pueyrredon y Cordoba", atributos)
bar3 = Bar("Starbucks", "Las Heras y Uriburu", [])
directorio.agregar(bar1)
directorio.agregar(bar2)
directorio.agregar(bar3)

registro = RegistroDeCalificaciones()
registro.agregar(Calificacion(bar1, wifi, 4))
registro.agregar(Calificacion(bar1, wifi, 5))

def imprimir(bares):
  for bar in bares.listar():
    print("Bar:")
    print(bar)
    try:
      print("Puntaje Wi-Fi: " + str(registro.obtener_promedio(bar, wifi)))
    except:
      pass
    print("")

def opciones_filtrar():
  print("Seleccione una opción de filtro: ")
  print("1. Por WI-FI")
  print("2. Por ubicación")
  opcion = int(input("Ingrese el número: "))

  if opcion == 1:
    opcion_filtrado = 8
    while not (0 <= opcion_filtrado <= 5):
      opcion_filtrado = int(input("Ingrese cantidad de estrellas mínima. Debe ser un valor entre 0 y 5: "))
    filtro = FiltracionCalificacion(directorio, registro, wifi, opcion_filtrado)
    for bar in filtro.listar():
      print("Bar:")
      print(bar)
      try:
        print("Puntaje Wi-Fi: " + str(registro.obtener_promedio(bar, wifi)))
      except:
        pass
      print("")

  elif opcion == 2:
    opcion_filtrado = input("Ingrese ubicación: ")
    pass

  
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
  menu()

if __name__ == '__main__':
  main()
