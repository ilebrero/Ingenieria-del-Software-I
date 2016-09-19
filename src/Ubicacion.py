class Ubicacion:
  import geopy, geopy.distance
  geolocator = geopy.geocoders.GoogleV3("AIzaSyAOPhtRuh0rMVylnRdMn_G529La1eMsybI", timeout = 5)
  distance = geopy.distance.distance

  def __init__(self, direccion):
    self._location = self.geolocator.geocode(direccion + ", Buenos Aires, Argentina")
    self.direccion = direccion

  def __str__(self):
    return self.direccion

  def distancia_a(self, otra_ubicacion):
    return self.distance(self._location.point, otra_ubicacion._location.point)
