class Ubicacion:
  import geopy, geopy.distance
  geolocator = geopy.geocoders.Nominatim()
  distance = geopy.distance.distance

  def __init__(self, direccion):
    self.ubicacion = geolocator.geocode(direccion + ", Buenos Aires, Argentina")
    self.direccion = location.address 
    self.coordenadas = location.longitud, location.latitude

  def __str__(self):
    return self.direccion

  def distancia_a(self, ubicacion):
    return distance(self.ubicacion.point, self.ubicacion.point)
