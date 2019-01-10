#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
from pygame.constants import K_q
from time import clock
import time
from juego_final import *





from random import randint

#  Tamaño de la pantalla
WIDTH = 980
HEIGHT = 450

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
#Variablea
MposX =100
MposY =280
enemX =900
enemY =300
enem2X=10
enem2Y=200
barrilX=100
barrilY=0

bananaX = randint(50, 850)
bananaY = randint(180, 310)

cont=4
puntaje=0
vidas=3

#contenem=3

direc=True
i=0

bajada =False
salto = False

def Initialize ():

    global screen, clock, xixf, Rxixf, enemi, enemf, bananai, barril
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Donkey Kong")
    clock = pygame.time.Clock()

    xixf={}
    Rxixf={}
    enemi={}
    enemf={}
    bananai={}
    barril ={}

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
    enemi[1]=(560,177,72,35)
    #enemi[2]=(360,11,43,43)

    bananai[0]=(0,4,44,59)
    barril[0]=(120,60,50,53)
    

    return


def LoadContent (): #carga el contenido

    global fondo, donkey, donkey_inv, enemigos, banana, enemigos_inv, Tiempo, barrile, segundos

    pygame.mixer.music.load('audios/audio_fondo.mp3')
    pygame.mixer.music.play(5)

    fondo = imagen("imagenes/fondodonkey.png")
    enemigos = imagen("imagenes/enemigos.png",True)
    banana = imagen("imagenes/objetos.png",True)
    barrile = imagen("imagenes/barril.png", True)
    donkey = imagen("imagenes/donkey.png", True)
    donkey_inv = pygame.transform.flip(donkey, True, False);
    enemigos_inv = pygame.transform.flip(enemigos, True, False);
    segundos=0

    #fondo = pygame.transform.scale(fondo, (1000, 510))
           

    return



def Updates():
    teclado()
    sprite()

    return
def game_over():
    pygame.init()

    pygame.display.set_caption("GAME OVER!!")
    screen = pygame.display.set_mode((1000, 515))
    screen.fill(NEGRO)
    gm = pygame.image.load("imagenes/fondo_over.jpg")
    screen.blit(gm, (0, 0))
    gm=pygame.image.load("imagenes/gameover.png")
    screen.blit(gm, (230,100))
    flecha=pygame.image.load("imagenes/flecha.png")
    screen.blit(flecha,(0,0))
    fuente_register = pygame.font.Font(None, 50)
    gmtext = fuente_register.render("PUNTAJE TOTAL:", True, ROJO)
    screen.blit(gmtext, (300, 300))
    puntaje_total = fuente_register.render(str(puntaje)+ "pts" , True, ROJO)
    screen.blit(puntaje_total, (600, 300))
    while True:
            for evento in pygame.event.get():
                if evento.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type==KEYDOWN:
                    if evento.key==pygame.K_ESCAPE:
                       sys.exit(0)
                    if evento.key==pygame.K_b:
                        print(puntaje)

                        archivo = open("puntajes.txt", "w")
                        archivo.close()
                        archivo = open("puntajes.txt", "a")
                        archivo.write("Jugador1: "+ str(puntaje)+ " puntos")
                        archivo.close()
                        archivo = open("puntajes.txt")
                        print(archivo.read())
                        mostrar_puntajes()

            pygame.display.update()

#def txt():
 #   mostrar_puntajes()

def Draw():
    global salto, bajada, MposX, MposY, enemX, enemY, bananaX, bananaY, enem2X, enem2Y, vidas, barrilX, barrilY, puntaje

    screen.blit(fondo, (0, 0))

    manual=pygame.image.load("imagenes/manual.jpg")
    screen.blit(manual,(0,0))
    segundos = pygame.time.get_ticks()/1000
    segundos = str(segundos)
    fuente = pygame.font.Font(None, 50)
    contador = fuente.render(segundos, 0, (VERDE))
    screen.blit(contador, (450, 5))
    puntos(puntaje)
    intentos(vidas)

    if vidas==0:
        pygame.mixer.music.stop()
        sonido_endmono = pygame.mixer.Sound("audios/end_mono.wav")
        sonido_endmono.play()
        sonido_gameover = pygame.mixer.Sound("audios/gameover.wav")
        sonido_gameover.play()
        # sys.exit(0)
        game_over()


    screen.blit(banana, (bananaX, bananaY), (bananai[0]))

    


    if MposX != enemX or MposX != enem2X or MposX != barrilX :
        screen.blit(enemigos, (enemX, enemY), (enemi[0]))
        screen.blit(enemigos_inv, (enem2X, enem2Y), (enemi[1]))
        screen.blit(barrile, (barrilX, barrilY), (barril[0]))
        enemX-=2
        enem2X+=4
        barrilX+=4
        barrilY+=3
    

    if enemX<0:
        enemX=900
        
    if  enem2X>950:
        enem2X = 10
        
    if  barrilY>350:
        barrilY =0
        
    if barrilX>=900:
        barrilX=0

    if MposX <0 :
        MposX=10

    if MposX >980:
        MposX=970

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

        if MposY <= 170:
            bajada = True

        if MposY >= 280:
            bajada = False
            salto = False


    if MposX >= bananaX-30 and MposX <= bananaX+30 and MposY >= bananaY-30 and MposY <= bananaY+30:
        bananaX = randint(20, 850)
        bananaY = randint(180, 310)
        puntaje +=1
        crunch = pygame.mixer.Sound("audios/crunch.wav")
        crunch.play()
        
        
    
    if (MposX >= enemX-30 and MposX <= enemX+30 and MposY >= enemY-32 and MposY <= enemY+22) or (MposX >= enem2X-30 and MposX <= enem2X+30 and MposY >= enem2Y-20 and MposY <= enem2Y+20) or (MposX >= enem2X-30 and MposX <= enem2X+30 and MposY >= enem2Y-20 and MposY <= enem2Y+20) or (MposX >= barrilX-30 and MposX <= barrilX+30 and MposY >= barrilY-20 and MposY <= barrilY+20):
        MposX = 110
        enemX = 900        
        vidas-=1
        colision = pygame.image.load("Imagenes/explosion.png")
        screen.blit(colision, (MposY, MposY))
        soundcol = pygame.mixer.Sound("audios/colision.wav")
        soundcol.play()
        #salto = pygame.mixer.Sound("audios/salto.wav")
        #salto.play()


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

    if teclado[K_m]:
        pygame.mixer.music.stop()
        #iconoff=pygame.image.load("imagenes/soundoff.png")
        #screen.blit(iconoff,(100,100))
    if teclado[K_x]:
        salir_del_programa()
    if teclado[K_RIGHT]:
        MposX+=3
        cont+=1
        direc=True
   # if teclado[K_x]:
    #    sys.exit(0)

    elif teclado[K_LEFT]:
        MposX-=3
        cont+=1
        direc=False

    else :
         cont=4

    #Cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    return 
 

def puntos(marcador):
    fuente = pygame.font.Font(None, 50)
    mensaje = fuente.render("Puntos: "+ str(marcador), True, (VERDE))
    screen.blit(mensaje,(100,0))
    return

def intentos(vidas):
    fuente = pygame.font.Font(None, 50)
    mensaje2 = fuente.render("Vidas: "+ str(vidas), True, (VERDE))
    screen.blit(mensaje2, (800, 0))
    if vidas==3:

        v3=pygame.image.load("imagenes/3v.jpg")
        screen.blit(v3,(820,40))
    if vidas==2:
        v2 = pygame.image.load("imagenes/2v.jpg")
        screen.blit(v2, (820, 40))
    if vidas==1:
        v1 = pygame.image.load("imagenes/1v.jpg")
        screen.blit(v1, (820, 40))

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
    
        
