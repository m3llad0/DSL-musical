"""

DSL musical
Diego Mellado Oliveros

Notas musicales a considerar:   
A = La
B = Si
C = Do
D = Re
E = Mi
F = Fa
G = Sol
"""

from threading import Thread
import pygame as pgame
import time
import re


#Leer las notas
def readSong(data):
    song =[]

    #Definir el archivo que se va abrir
    with open(data, 'r') as frame:
        #Leer linea por linea las notas
       for line in frame:
           #Agregarlas a una lista
           song.append(line.strip('\n'))

    return song

print("""
************PIANO************""")

def playNotes(path, duration):
    #definir la duracion
    time.sleep(duration)
    pgame.mixer.Sound(path).play()
    time.sleep(duration)


def main():

    #Crear el objeto de mixer de pygame
    pgame.mixer.init()
    pgame.init()
    
    #Iniciar la lista con las notas
    song = readSong('song.txt')

    #Iniciar los canales al mismo numero de elementos en la cancion
    pgame.mixer.set_num_channels(len(song))

    path = 'Sounds/'

    cont = 1

    th = {}

    for note in song:
        #Se hace la busqueda para el encabezado usando regex
        if re.findall('^#', note):
            print(note)
        #Busqueda de las notas usando regex
        elif re.findall('([A-G](#*|-*)[0-9]|R)(W|H|Q|E|S|T|F)', note):
            #Se almacena el intervalo de tiempo
            tempo = note[-1]
            #Se retira la duracion de la nota
            note = note.strip(tempo)
            #Se inicializa la duracion en cero
            duration = 0
            #Se establece la duracion dependiendo del intervalo
            if tempo == 'W':
                duration = 3.2
            elif tempo == 'H':
                duration = 1.6
            elif tempo == 'Q':
                duration == 0.8
            elif tempo == 'E':
                duration == 0.4
            elif tempo == 'S':
                duration = 0.2
            elif tempo == 'T':
                duration == 0.1
            elif tempo == 'F':
                duration == 0.05
            print(note)
            #Se reproduce la nota musical usando los archivos de la carpeta sounds
            th[note] = Thread(target = playNotes, args = (path+'{}.wav'.format(note), duration))
            th[note].start()
            th[note].join()
            if cont%7==0:
                time.sleep(1)
            cont += 1
        # elif re.findall('R(W|H|Q|E|S|T|F)'):

        else:
            print('error')




main()