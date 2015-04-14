#!/usr/bin/python
# -*- coding: utf-8 -*

__author__ ='Grupo16'
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import funciones
import twitter
import io
import json

app = Flask(__name__)
GoogleMaps(app)
    
contador = 500 #Se almacenaran 500 twits en el json
tema = 'Python' #Se buscara la palabra Python
twitter_api = funciones.oauth_login() #Autentificacion para el API de Twitter
search_results = twitter_api.search.tweets(q = tema, count = contador, geocode='36.516667,-6.283333,1000km')
#Se realiza la busqueda y en twitter con los parametros anteriores ademas de la geolocalizacion de cadiz
#para que actue como centro y se busquen los twits a una distancia alrededor de 1000km
funciones.save_json("twits",search_results) #Se guardan los resultados en un json

with open('twits.json') as data_file: #cargamos el json
	data = json.load(data_file)

lista = []

for estado in data["statuses"]: #Extraemos las coordenadas de los twits que las tengan en el json
	if estado["geo"]:
		coordenada = estado["coordinates"]
		xy=[coordenada.values()[1][1] , coordenada.values()[1][0]]
		lista.append(xy) #Añadimos estas coordenadas a una lista

@app.route("/")
def mapview():
	mymap = Map( #Se carga la informacion de google maps para mostrarlo por pantalla mediante flask
		identifier="view-side",
		lat = 36.516667,
		lng = -6.283333,
		markers = lista,
		style="height:800px;width:800px;margin:0;"
	)
	return render_template('template2.html', mymap=mymap) #Se devuelve el objeto mymap con la
	#informacion para crear el mapa de google maps y los puntos de los twits

if __name__ == "__main__":
    app.run(debug=True)

