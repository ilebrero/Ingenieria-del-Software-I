#from Bar import *

class Cartografo:
	
	def __init__(self):
		pass

	def marcar_en_mapa(self, unBar):
		_bares_marcados.append(unBar)

	def mostrar_mapa(self, center=None, zoom=10, imgformat="jpeg", maptype="roadmap"):

		url_google = "http://maps.google.com/maps/api/staticmap?" # base URL, append query params, separated by &

		str_size = "size=%ix%i" % (640, 640)  # tuple of ints, up to 640 by 640
		str_format = "format=" + imgformat
		str_maptype = "maptype=" + maptype  # roadmap, satellite, hybrid, terrain

		for i, bar_marcado in enumerate(_bares_marcados):
			 _markers.append("markers=color:blue|label:" + _labels[i] + "|" + bar_marcado.ubicacion + ", CABA, Argentina")

		str_markers = ""
		if self._markers != None:						#		for bar in self._bares_marcados:
			separator = "&"
			str_markers += separator.join(self._markers)
		
		str_sensor = "sensor=false" # must be given, deals with getting loction from mobile device
	
		str_options = [str_size, str_format, str_maptype, str_markers, str_sensor]

		main_separator = "&"
		url_options = main_separator.join(str_options)
		url = url_google + url_options
		return url

	_labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	_markers = []
	_bares_marcados = []