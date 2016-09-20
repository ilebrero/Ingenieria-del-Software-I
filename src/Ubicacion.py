import geopy, geopy.distance

_geolocator = geopy.geocoders.GoogleV3("AIzaSyAOPhtRuh0rMVylnRdMn_G529La1eMsybI", timeout=10)
_distance = geopy.distance.distance

import concurrent.futures
_executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

class Ubicacion:

  def __init__(self, direccion):
    # [TODO] user concurrent.futures
    self._location = _executor.submit(_geolocator.geocode, direccion + ", Buenos Aires, Argentina")
    self.direccion = direccion

  def __str__(self):
    return self.direccion

  def distancia_a(self, otra_ubicacion):
    return _distance(self._location.result().point, otra_ubicacion._location.result().point)
