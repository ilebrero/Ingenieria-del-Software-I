from Bar import *
from Direccion import *
from subprocess import Popen

_labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Cartografo:

  def __init__(self):
      self._bares_marcados = []

  def marcar_en_mapa(self, unBar):
    self._bares_marcados.append(unBar)

  def mostrar_mapa(self):
    markers = []

    url_google = "http://maps.google.com/maps/api/staticmap?"

    str_size = "size=%ix%i" % (640, 640)
    str_format = "format=jpeg"
    str_maptype = "maptype=roadmap"

    for i, bar_marcado in enumerate(self._bares_marcados):
       markers.append("markers=color:blue|label:" + _labels[i] + "|" + str(bar_marcado.direccion) + ", Capital Federal, Argentina")
       print(_labels[i] + " " + bar_marcado.nombre)

    str_markers = "&".join(markers)
    
    str_sensor = "sensor=false"
  
    str_options = [str_size, str_format, str_maptype, str_markers, str_sensor]

    url_options = "&".join(str_options)
    url = url_google + url_options
    url = url.replace(" ", "+")
    Popen('curl -s "{}" | display'.format(url), shell=True)
