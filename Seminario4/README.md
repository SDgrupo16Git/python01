#Seminario 4
03 Tercera entrega.

Para esta entrega deberemos haber trabajado ya con el API de Twitter, y haber estado atentos en el Seminario sobre Flask y Jinja2. Los grupos deberán entregar el repositorio donde tenga un programa en Python, que revise las direcciones (latitud y longitud) de los tweets que cumplan una determinada opción, como que sea el más actual, que corresponda a alguna afición (equipo de fútbol, políticas..) y desplegar esas direcciones en un mapa utilizando la extensión de Flask para Google Maps.

Para ejecutar el programa, deberá escribir desde la linea de comandos
user@equipo:/$python main.py

El programa generará un fichero json en el que se almacenarán 500 tuits recibidos por la plataforma Twitter a una distancia no superior a 1000 km de Cádiz. Entre estos tuits, buscará la palabra 'cadiz' y obtendrá la geolocalización de los tuits que contengan dicha palabra. 

El resultado se mostrará en su navegador si accede a la dirección "127.0.0.1:5000"

