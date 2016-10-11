from DirectorioDeBares import *
from Bar import *
from Caracteristica import *
from Calificacion import *
from RegistroDeCalificaciones import *
from Cartografo import *

wifi = Caracteristica("Wi-Fi")
aircon = Caracteristica("Aire Acondicionado")
precios = Caracteristica("Precios")

directorio = DirectorioDeBares()

cartografo = Cartografo()

bar1 = Bar("Tienda del cafe", "Santa Fe y Callao", [wifi])
bar2 = Bar("Cafe Martinez", "Av. Pueyrredon y Cordoba", [wifi, aircon, precios])
bar3 = Bar("Starbucks", "Las Heras y Uriburu", [aircon, precios, Caracteristica("enchufes")])
bar4 = Bar("Tips", "Las Heras y Av. Pueyrredon", [wifi])
bar5 = Bar("Muu lecheria", "Costa Rica y Armenia", [])
bar6 = Bar("La biela", "Junin y Guido", [wifi])
bar7 = Bar("Pani", "Junin y Vicente Lopez", [wifi, precios])
bar8 = Bar("Milli", "Av. Pueyrredon y French", [wifi, aircon,precios])

directorio.agregar(bar1)
directorio.agregar(bar2)
directorio.agregar(bar3)
directorio.agregar(bar4)
directorio.agregar(bar5)
directorio.agregar(bar6)
directorio.agregar(bar7)
directorio.agregar(bar8)

registro = RegistroDeCalificaciones()

registro.agregar(Calificacion(bar1, wifi, 4))
registro.agregar(Calificacion(bar1, wifi, 5))

registro.agregar(Calificacion(bar2, wifi, 2))
registro.agregar(Calificacion(bar2, wifi, 3))
registro.agregar(Calificacion(bar2, wifi, 1))

registro.agregar(Calificacion(bar4, wifi, 4))
registro.agregar(Calificacion(bar4, wifi, 4))
registro.agregar(Calificacion(bar4, wifi, 2))

registro.agregar(Calificacion(bar2, precios, 1))
registro.agregar(Calificacion(bar2, precios, 2))
registro.agregar(Calificacion(bar2, precios, 2))

registro.agregar(Calificacion(bar2, aircon, 4))
registro.agregar(Calificacion(bar2, aircon, 5))
registro.agregar(Calificacion(bar2, aircon, 4))

registro.agregar(Calificacion(bar8, aircon, 2))
registro.agregar(Calificacion(bar8, aircon, 4))
registro.agregar(Calificacion(bar8, aircon, 3))

registro.agregar(Calificacion(bar8, precios, 5))
registro.agregar(Calificacion(bar8, precios, 4))
registro.agregar(Calificacion(bar8, precios, 3))

registro.agregar(Calificacion(bar8, wifi, 5))
registro.agregar(Calificacion(bar8, wifi, 5))
registro.agregar(Calificacion(bar8, wifi, 3))

registro.agregar(Calificacion(bar7, wifi, 4))
registro.agregar(Calificacion(bar7, wifi, 4))
registro.agregar(Calificacion(bar7, wifi, 3))

registro.agregar(Calificacion(bar7, precios, 3))
registro.agregar(Calificacion(bar7, precios, 4))
registro.agregar(Calificacion(bar7, precios, 3))

registro.agregar(Calificacion(bar3, precios, 5))
registro.agregar(Calificacion(bar3, precios, 5))
registro.agregar(Calificacion(bar3, precios, 3))

registro.agregar(Calificacion(bar3, Caracteristica("enchufes"), 3))
registro.agregar(Calificacion(bar3, Caracteristica("enchufes"), 4))
