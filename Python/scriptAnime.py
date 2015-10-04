#!/usr/bin/python
##############################################################################################
# AnimeCript  script para ver anime
#
# anime => Guarda el anime a ver
# historial => Se almace los 3 ultimos capitulos vistos del anime seleccionado, si los hay
# capitulo => Guarda el capitulo a ver
# fecha => Fecha en la que se visiona el anime
# hora => Hora en la que se visiona el anime
# url => Url con el anime y capitulo seleccionado
##############################################################################################

# --* coding: utf-8 -*-

import webbrowser
import time
import re
import sys

reload(sys) 
sys.setdefaultencoding("utf-8")

########################
# Funciones auxiliares #
########################


# Comprueba y corrige el formato del anime introducido.
# Ej: Dragon Ball => dragon-ball
def formato_anime(anime):

	anime_corregido = re.sub(' ', '-',anime)
	anime_corregido = anime_corregido.lower()
	return anime_corregido

# Obtenemos la hora y la fecha de visionado	
def obtener_hora_fecha():
	h = time.strftime("%H:%M")	
	f = time.strftime("%d/%m/%y")
	
	return f,h

# Buscamos si el usuario ha visto el anime indicado
def historial(anime):

	historial = []

	# Buscamos info
	file=open("registroactividad.txt","a+")
	for i in file.readlines():
		if i.find(anime) >= 0:
			historial.append(i)	# Saco la linea donde esta anime cap fecha
	file.close()

	if len(historial):
		print "\nRegistro de " + anime + "\n"
		for i in historial:
			print i
	else:
		print "Aun no has visto ningun capitulo de este anime"


#Guardamos el informacion sobre el capitulo visionado

def log(info):

	f = open("registroactividad.txt", "a")
	f.write(info)
	f.close()


#Pedimos el anime
anime = raw_input("Que anime quieres ver?: ")

#Le arreglamos el formato
anime = formato_anime(anime)

fecha,hora =  obtener_hora_fecha()

historial(anime)

capitulo = raw_input("Que capitulo?: ")

info = anime + " " + capitulo + " " + fecha + " " + hora + "\n"

#Guardamos la informacion en el registro
log(info)

parteurl = "http://animeflv.net/ver/"

url = parteurl + anime + "-" + capitulo + ".html"

webbrowser.open_new(url)	# Para abrir navegador


