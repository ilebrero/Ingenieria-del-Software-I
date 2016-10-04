import geopy, geopy.distance

_geolocator = geopy.geocoders.GoogleV3("AIzaSyAOPhtRuh0rMVylnRdMn_G529La1eMsybI", timeout=10)
_distance = geopy.distance.distance

import concurrent.futures
_executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

#TODO: mover archivos por separado
#TODO: Ver como printear el mapa
class Ubicacion:

  def __init__(self, direccion):
    self.direccion = direccion

  def __str__(self):
    return self.direccion

class CalculadorDeDistancias:
	def __init__(self):
		self.geolocator = Geolocalizador()

	def distancia_entre(self, direccion_desde, direccion_hasta):
		location_desde = _executor.submit(self.geolocator.traducir_direccion_a_coordenadas, direccion_desde)
		location_hasta = _executor.submit(self.geolocator.traducir_direccion_a_coordenadas, direccion_hasta)
		return _distance(location_desde.result(), location_hasta.result()).meters

class Geolocalizador:
	#TODO: memoizar direccion

	def traducir_direccion_a_coordenadas(self, direccion):
		return _geolocator.geocode(str(direccion) + ", Buenos Aires, Argentina").point

	
	
