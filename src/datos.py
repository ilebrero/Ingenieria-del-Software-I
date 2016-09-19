

wifi = Atributo("Wi-Fi")
atributos = [wifi]

directorio = DirectorioDeBares()

bar1 = Bar("Tienda del cafe", "Santa Fe y Callao", atributos)
bar2 = Bar("Cafe Martinez", "Pueyrredon y Cordoba", atributos)
bar3 = Bar("Starbucks", "Las Heras y Uriburu", [])
bar4 = Bar("Tips", "Las Heras y Pueyrredon", atributos)
bar5 = Bar("Muu lecheria", "Soler y Paraguay", [])
bar6 = Bar("La biela", "Junin y Guido", atributos)

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
