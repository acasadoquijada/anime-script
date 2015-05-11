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

import webbrowser
import time

anime = raw_input("Que anime quieres ver?: ")

fecha = time.strftime("%d/%m/%y")
hora = time.strftime("%H:%M")

historial = []

#Para buscar informacion del anime en el registro
file=open("registroactividad.txt","a+")
for i in file.readlines():
	if i.find(anime) >= 0:
		historial.append(i)	# Saco la linea donde esta anime	cap	fecha
file.close()

if len(historial):
	print "\nRegistro de " + anime + "\n"
	for i in historial:
		print i
else:
	print "Aun no has visto ningun capitulo de este anime"

capitulo = raw_input("Que capitulo?: ")

#Guardamos la informacion en el registro
f = open("registroactividad.txt", "a")
f.write(anime + " " + capitulo + " " + fecha + " " + hora + "\n")
f.close()

parteurl = "http://animeflv.net/ver/"

url = parteurl + anime + "-" + capitulo + ".html"
#print url
webbrowser.open_new(url)	# Para abrir navegador
