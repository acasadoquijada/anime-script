#!/bin/bash
#
# AnimeCript  script para ver anime
#
# ANIME => Guarda el anime a ver
# HIS => Se almace los 3 ultimos capitulos vistos del anime seleccionado, si los hay
# CAP => Guarda el capitulo a ver
# FECHA => Fecha en la que se visiona el anime
# INF => Informacion que se almacena en el registro ANIME + CAP + FECHA
# URL => Url con el anime y capitulo seleccionado
# -h => Muestra informacion y ayuda sobre el script
# -rm => Resetea el historial 

if [ $# -eq 1 ]
	then
	if [ "$1" == "-h" ]
		then
		echo -e "\nAnimeCript version 0.5\n"
		echo -e "Autor: Alejandro Casado Quijada\n"
		echo -e "Contacto: acasadoquijada@gmail.com\n"
		echo -e "SELECCION DE ANIME\n"
		echo "El nombre del anime debe ir en minusuculas y separado por guiones en el caso de que sea un nombre compuesto"
		echo "Ej: Shingeki no Kyojin => shingeki-no-kyojin"
		echo -e "\nSELECCION DE CAPITULO\n"
		echo -e "El capitulo a ver DEBE exisitir en la serie, si no, se producira un error\n"
		echo -e "BORRAR EL REGISTRO DE ACTIVIDAD\n"
		echo -e "Para borrar el historial ejecutar el script con la opcion -rm\n"
		exit 0
	elif [ "$1" == "-rm" ]
		then
		echo "Historial borrado"
		echo "" > registroactividad.txt
		exit 0
	else
		echo "Comando incorrecto"
		echo -e "Comandos soportados: -h, -rm"
		exit 0		

	fi
fi

ANIME=$(zenity --entry --title="Seleccionar anime" --text="¿Que anime te apetece ver hoy?")

if grep -q $ANIME registroactividad.txt; then
	HIS=$(grep $ANIME registroactividad.txt | tail -n -3)
	zenity --info --title="Registro sobre anime" --text="$HIS"
else
	zenity --info --title="Registro sobre anime" --text="\n\nAun no has visto nada de este anime"
fi


ULTCAP=$(grep $ANIME registroactividad.txt | tail -n -1)

CAP=$(zenity --entry --title="Seleccionar capitulo" --text="$ULTCAP\n¿Que capitulo te apece ver?")

FECHA=$(date '+%d/%m/%Y %H:%M:%S');
INF="$ANIME $CAP $FECHA"

echo $INF >> registroactividad.txt

URL=http://animeflv.net/ver/$ANIME-$CAP.html

if which xdg-open > /dev/null
then
  xdg-open $URL
elif which gnome-open > /dev/null
then
  gnome-open $URL
fi

