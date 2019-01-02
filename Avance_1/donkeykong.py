#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Librerias
import sys, pygame
from pygame.locals import *


# Variables
WIDTH = 980
HEIGHT = 450
MposX =300
cont=6
direc=True
i=0
xixf={}#xinicial y xfinal para las posiciones
Rxixf={}#Posiciones inversas 


def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error.message:
                raise SystemExit
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

#Funcion para el movimiento con teclado
def teclado():
    teclado = pygame.key.get_pressed()
     
    global MposX
    global cont, direc
   
    if teclado[K_RIGHT]:
        MposX+=2
        cont+=1
        direc=True
    elif teclado[K_LEFT]:
        MposX-=2
        cont+=1
        direc=False
    elif teclado[K_q]:
        MposX-=2
       
    return 
 


#Sprite
def sprite():
 
    global cont
 
    xixf[0]=(135,0,46,74)
   # xixf[1]=(0,102,53,90)
   # xixf[2]=(72,105,69,90)
   # xixf[3]=(153,112,20,41)
   # xixf[4]=(241,115,75,81)
    xixf[1]=(0,219,90,73)
   # xixf[6]=(108,224,86,72)
    xixf[2]=(211,223,91,73)
   # xixf[8]=(0,320,70,65)
    xixf[3]=(91,320,65,68)
    xixf[4]=(135,0,46,74)

    Rxixf[0]=(236,0,49,72)
    Rxixf[1]=(98,114,76,80)
   # Rxixf[2]=(0,320,70,65)
    Rxixf[2]=(20,228,86,68)
   # Rxixf[4]=(108,224,86,72)
    Rxixf[3]=(187,320,60,66)
   # Rxixf[6]=(241,115,75,81)
   # Rxixf[7]=(153,112,20,41)
   # Rxixf[8]=(72,105,69,90)
   # Rxixf[9]=(0,102,53,90)
    Rxixf[4]=(53,310,48,75)   

    p=5 #Velocidad del movimiento del personaje
   
    global i
       
    if cont==p:
        i=0
   
    if cont==p*2:
        i=1
   
    if cont==p*3:
        i=2
   
    if cont==p*4:
        i=3
   
    if  cont==p*5:
        i=4
        cont=0
        
    return

    
def main():
    pygame.init()    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Donkey Kong")
   
 
    fondo = imagen("imagenes/fondod.png")
   
         
    donkey = imagen("imagenes/donkey.png",True)  
    donkey_inv=pygame.transform.flip(donkey,True,False);#Imagen de personaje invertida

    clock = pygame.time.Clock()


    # bucle principal del juego
    while True:
       
        time = clock.tick(60)
       
        sprite()
        teclado()
       
        fondo = pygame.transform.scale(fondo, (1000, 510)) 
        screen.blit(fondo, (0, 0))
       
        if direc==True:
            screen.blit(donkey, ( MposX, 318),(xixf[i]))
   
        if direc==False:
            screen.blit(donkey_inv, ( MposX, 318),(Rxixf[i]))
   
        pygame.display.flip()


         # Cerrar la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
   
    return 0


if __name__ == '__main__':
    main()

        
