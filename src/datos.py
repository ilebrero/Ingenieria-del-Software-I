from DirectorioDeBares import *
from Bar import *
from Caracteristica import *
from Calificacion import *
from RegistroDeCalificaciones import *
from Cartografo import *

wifi = Caracteristica("Wi-Fi")
aircon = Caracteristica("Aire Acondicionado")

directorio = DirectorioDeBares()

cartografo = Cartografo()

bar1 = Bar("Tienda del cafe", "Santa Fe y Callao", [wifi])
bar2 = Bar("Cafe Martinez", "Pueyrredon y Cordoba", [wifi, aircon])
bar3 = Bar("Starbucks", "Las Heras y Uriburu", [aircon])
bar4 = Bar("Tips", "Las Heras y Pueyrredon", [wifi])
bar5 = Bar("Muu lecheria", "Costa Rica y Armenia", [])
bar6 = Bar("La biela", "Junin y Guido", [wifi])

directorio.agregar(bar1)
directorio.agregar(bar2)
directorio.agregar(bar3)
directorio.agregar(bar4)
directorio.agregar(bar5)
directorio.agregar(bar6)

registro = RegistroDeCalificaciones()

registro.agregar(Calificacion(bar1, wifi, 4))
registro.agregar(Calificacion(bar1, wifi, 5))

registro.agregar(Calificacion(bar2, wifi, 2))
registro.agregar(Calificacion(bar2, wifi, 3))
registro.agregar(Calificacion(bar2, wifi, 1))

registro.agregar(Calificacion(bar4, wifi, 4))
registro.agregar(Calificacion(bar4, wifi, 4))
registro.agregar(Calificacion(bar4, wifi, 2))
