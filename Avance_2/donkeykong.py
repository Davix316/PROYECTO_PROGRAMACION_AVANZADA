#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
from pygame.constants import K_q
from time import clock


#from Tkconstants import FALSE
from random import randint

#  Tamaño de la pantalla
WIDTH = 980
HEIGHT = 450

#Variablea
MposX =100
MposY =318
enemX =900
enemY =340
bananaX = randint(50, 850)
bananaY = randint(180, 310)

cont=4
puntaje=0
#contenem=3

direc=True
i=0

bajada =False
salto = False

def Initialize ():

    global screen, clock, xixf, Rxixf, enemi, enemf, bananai
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Donkey Kong")
    clock = pygame.time.Clock()

    xixf={}
    Rxixf={}
    enemi={}
    enemf={}
    bananai={}

    xixf[0] = (135, 0, 46, 74)
    xixf[1] = (2, 101, 51, 89)
    xixf[2] = (72,103,65,89)
    xixf[3] = (153,112,77,82)
    xixf[4] = (243,114,78,79)
    xixf[5] = (0, 222, 89, 72)
    xixf[6] = (107,224,88,73)
    xixf[7] = (312, 227, 85, 66)
    xixf[8] = (0,320,70,65)
    xixf[9] = (174, 322, 60, 64)
    xixf[10] = (317, 310, 42, 74)
    #xixf[5] = (135, 0, 46, 74)

    Rxixf[0] = (236, 0, 49, 72)
    Rxixf[1] = (364, 104, 50, 90)
    Rxixf[2]=(280,104,67,88)
    Rxixf[3] = (191, 112, 77, 84)
    Rxixf[4]=(95,114,78,80)
    Rxixf[5] = (328, 222, 90, 75)
    Rxixf[6]=(224,223,86,70)
    Rxixf[7]=(20,228,85,66)
    Rxixf[8]=(347,321,69,61)
    Rxixf[9]=(187,324,60,64)
    Rxixf[10] = (55, 311, 46, 73)
    #Rxixf[5] = (53, 310, 48, 75)

    enemi[0]=(334,3,46,48)
    #enemi[1]=(257,10,46,44)
    #enemi[2]=(360,11,43,43)

    bananai[0]=(0,4,44,59)
    

    return

def LoadContent (): #carga el contenido

    global fondo, donkey, donkey_inv, enemigos, banana

    pygame.mixer.music.load('audios/donkey.mp3')
    pygame.mixer.music.play()
    fondo = imagen("imagenes/fondodonkey.png")
    enemigos = imagen("imagenes/enemigos.png",True)
    banana = imagen("imagenes/objetos.png",True)
    donkey = imagen("imagenes/donkey.png", True)
    donkey_inv = pygame.transform.flip(donkey, True, False);

    fondo = pygame.transform.scale(fondo, (1000, 510))

    return

def Updates():
    teclado()
    #Escenario
    sprite()
    # Enemigo()
    # Coliciones()

    return

def Draw():
    global salto, bajada

    screen.blit(fondo, (0, 0))

    #Movimiento
    global MposX, MposY, enemX, enemY, bananaX, bananaY, puntaje


    screen.blit(banana, (bananaX, bananaY), (bananai[0]))

    if MposX != enemX:
        screen.blit(enemigos, (enemX, enemY), (enemi[0]))
        enemX-=2

    if enemX<0 :
        #screen.blit(enemigos, (enemX, enemY), (enemi[0]))
        enemX=900
         

    if direc == True and salto == False:
        screen.blit(donkey, (MposX, MposY), (xixf[i]))

    if direc == False and salto == False:
        screen.blit(donkey_inv, (MposX, MposY), (Rxixf[i]))

        # salto normal y Parabolico
    if salto == True:

        if direc == True:
            screen.blit(donkey, (MposX, MposY), (xixf[4]))
        if direc == False:
            screen.blit(donkey_inv, (MposX, MposY), (Rxixf[4]))

        if bajada == False:
            MposY -= 5

        if bajada == True:
            MposY += 5

        if MposY <= 186:
            bajada = True

        if MposY >= 318:
            bajada = False
            salto = False

    if MposX >= bananaX-30 and MposX <= bananaX+30 and MposY >= bananaY-30 and MposY <= bananaY+30:
        bananaX = randint(20, 850)
        bananaY = randint(180, 310)
        puntaje+=1
    
    if MposX >= enemX-30 and MposX <= enemX+30 and MposY==enemY-22:
        MposX = 100


    pygame.display.flip()

    return

def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error:
                raise SystemExit
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image


# Teclado
def teclado():

    global MposX
    global cont, direc, salto

    teclado = pygame.key.get_pressed() #Informacion del teclado y teclas presionadas


    if teclado[K_q]:
        salto=True

    if teclado[K_RIGHT]:
        MposX+=2
        cont+=1
        direc=True

    elif teclado[K_LEFT]:
        MposX-=2
        cont+=1
        direc=False

    else :
         cont=4

    #Cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    return 
 


#Sprite
def sprite():
 
    global cont
    
    p=4
   
    global i
       
    if cont==p:
        i=0
   
    if cont==p*2:
        i=1
   
    if cont==p*3:
        i=2
   
    if cont==p*4:
        i=3
   
    if cont==p*5:
        i=4

    if cont==p*6:
        i=5

    if cont==p*7:
        i=6

    if cont==p*8:
        i=7

    if cont==p*9:
        i=8

    if cont==p*10:
        i=9

    if cont == p*11:
        i=10
        cont=0
        
    return


#Funcion principal    
def main():

    Initialize()
    LoadContent()

    while True:
       
        time = clock.tick(60)#cada 60 milisegundos pausa

        Updates()
        Draw()

   
    return


if __name__ == '__main__':
    main()

        
