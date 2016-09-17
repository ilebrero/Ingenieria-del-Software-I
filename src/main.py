from DirectorioDeBares import *
from Bar import *
from Atributo import *
from Calificacion import *
from RegistroDeCalificaciones import *
from Filtracion import *

wifi = Atributo("Wi-Fi")
atributos = [wifi]

directorio = DirectorioDeBares()

directorio.agregar(Bar("Cafe Martinez", "Pueyrredon y Cordoba", atributos))
directorio.agregar(Bar("Starbucks", "Las Heras y Uriburu", []))

bar1 = Bar("Tienda del cafe", "Santa Fe y Callao", atributos)
directorio.agregar(bar1)

registro = RegistroDeCalificaciones()
registro.agregar(Calificacion(bar1, wifi, 4))
registro.agregar(Calificacion(bar1, wifi, 5))

def main():
  for bar in directorio.listar():
    print("Bar:")
    print(bar)
    try:
      print("Puntaje Wi-Fi: " + str(registro.obtener_promedio(bar, wifi)))
    except:
      pass
    print("")

  print("Bares con buen Wi-Fi:")

  filtro = FiltracionCalificacion(directorio, registro, wifi, 4)
  for bar in filtro.listar():
    print("Bar:")
    print(bar)
    try:
      print("Puntaje Wi-Fi: " + str(registro.obtener_promedio(bar, wifi)))
    except:
      pass
    print("")


if __name__ == '__main__':
  main()
