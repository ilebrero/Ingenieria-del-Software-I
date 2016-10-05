import geopy, geopy.distance

_geolocator = geopy.geocoders.GoogleV3("AIzaSyAOPhtRuh0rMVylnRdMn_G529La1eMsybI", timeout=10)
_distance = geopy.distance.distance

import concurrent.futures
_executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

class CalculadorDeDistancias:
  def __init__(self):
    self.geolocalizador = Geolocalizador()

  def distancia_entre(self, direccion_desde, direccion_hasta):
    location_desde = _executor.submit(self.geolocalizador.traducir_direccion_a_coordenadas, direccion_desde)
    location_hasta = _executor.submit(self.geolocalizador.traducir_direccion_a_coordenadas, direccion_hasta)
    return _distance(location_desde.result(), location_hasta.result()).meters

class Geolocalizador:
  _memo = dict()

  def traducir_direccion_a_coordenadas(self, direccion):
    c = self._memo.get(direccion)
    if not c:
      c = _geolocator.geocode(str(direccion) + ", Buenos Aires, Argentina").point
    self._memo[direccion] = c
    return c
