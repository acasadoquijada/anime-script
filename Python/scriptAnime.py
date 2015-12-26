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
from datetime import date, datetime
import re
import sqlite3 as lite

########################
# Funciones auxiliares #
########################

 
def registro(anime,capitulo):

	con = lite.connect('registro.db')
	
	with con:	
		cur = con.cursor()
			
		cur.execute("CREATE TABLE IF NOT EXISTS "+ anime +"(capitulo INT NOT NULL,fecha TIMESTAMP NOT NULL)")
	
		now = datetime.now()
	
		cur.execute("INSERT INTO " + anime +" VALUES(?,?)", (capitulo,now))
	
	
# Comprueba y corrige el formato del anime introducido.
# Ej: Dragon Ball => dragon-ball
def formato_anime(anime):

	anime_corregido = re.sub(' ', '-',anime)
	anime_corregido = anime_corregido.lower()
	return anime_corregido


#Guardamos el informacion sobre el capitulo visionado

def historial(anime):

	con = lite.connect('registro.db')

	with con:

		cur = con.cursor()

		cur.execute("CREATE TABLE IF NOT EXISTS "+ anime +"(capitulo INT NOT NULL,fecha TIMESTAMP NOT NULL)")	

		info = cur.execute("SELECT * FROM " + anime + " ORDER BY fecha DESC LIMIT 5")

		print("Ultimos capítulos visionados de " + anime)

		for i in info:
			print(i)

if __name__ == "__main__":

	#Pedimos el anime
	anime = input("¿Que anime quieres ver?: ")

	while(anime.isdigit()):
		print("Introduce un nombre valido")
		anime = input("¿Que anime quieres ver?: ")
		
	#Le arreglamos el formato
	anime = formato_anime(anime)
	
	historial(anime)

	capitulo = input("¿Que capítulo?: ")

	#Guardamos la informacion en el registro
	registro(anime,capitulo)

	parteurl = "http://animeflv.net/ver/"

	url = parteurl + anime + "-" + capitulo + ".html"

	webbrowser.open_new(url)	# Para abrir navegador

