import pygame
import sys, pygame
from pygame.locals import *
from pygame.constants import K_q
from time import clock
from donkeykong import *



reloj = pygame.time.Clock()
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)


class Menu:
    "Representa un menú con opciones para un juego"

    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.Font(None, 40)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False


    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                # Invoca a la función asociada a la opción.
                titulo, funcion = self.opciones[self.seleccionado]
                print("Selecciona la opción '%s'." % (titulo))
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]


    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        total = self.total
        indice = 0
        altura_de_opcion = 65
        x = 200# posicion de la letras en x
        y = 280 # posicion de las letras en y

        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = (255, 0, 0)
            else:
                color = (0, 0, 0)

            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)

def pantalla_instrucciones():
    pygame.init()
    fuente = pygame.font.Font(None, 50)
    texto = fuente.render("SELECCIONE EL PERSONAJE ", True, NEGRO)
    # Coloca la imagen del texto sobre la pantalla en 250 x 250
    screen.blit(texto, [270, 50])
    fuente_instrucciones = pygame.font.Font(None, 25)
    texto0 = fuente_instrucciones.render("INSTRUCCIONES", True, NEGRO)
    texto1 = fuente_instrucciones.render("El juego consiste en atrapar ", True, NEGRO)
    texto2 = fuente_instrucciones.render("la mayor cantidad de bananas  ", True, NEGRO)
    texto3 = fuente_instrucciones.render("posibles.", True, NEGRO)
    texto4 = fuente_instrucciones.render("El juego termina cuando haya  ", True, NEGRO)
    texto5 = fuente_instrucciones.render("chocado 3 veces con el ratón o   ", True, NEGRO)
    texto6 = fuente_instrucciones.render("barriles que aparece en la pantalla. ", True, NEGRO)
    texto7 = fuente_instrucciones.render("Utilice letra 'Q' para saltar ", True, NEGRO)
    texto8 = fuente_instrucciones.render("desplace con las teclas direccionales ", True, NEGRO)
    texto9 = fuente_instrucciones.render("hacia adelante y hacia atras ", True, NEGRO)
    texto10 = fuente_instrucciones.render("Digite 'Y' para empezar ", True, NEGRO)
    texto11 = fuente_instrucciones.render(" la letra 'M' pausa sonido", True, NEGRO)
    texto12 = fuente_instrucciones.render("JUGAR = Y", True, NEGRO)
    screen.blit(texto0, [700, 150])
    screen.blit(texto1, [700, 170])
    screen.blit(texto2, [700, 190])
    screen.blit(texto3, [700, 210])
    screen.blit(texto4, [700, 230])
    screen.blit(texto5, [700, 250])
    screen.blit(texto6, [700, 270])
    screen.blit(texto7, [700, 290])
    screen.blit(texto8, [700, 310])
    screen.blit(texto9, [700, 330])
    screen.blit(texto10, [710, 350])
    screen.blit(texto11, [710, 370])
    screen.blit(texto12, [730, 390])
    jugadores = [
        "Donkey Kong= Y"
    ]
    personaje3 = pygame.image.load("Imagenes/monote.png")
    screen.blit(personaje3, (100, 100))
    letra = pygame.font.Font(None, 30)
    nombreP3 = letra.render(jugadores[0], True, ROJO)
    screen.blit(nombreP3, [470, 100])

    ######
    pygame.mixer.music.load("audios/audio_fondo.mp3")
    pygame.mixer.music.play(5)
    empezar = True
    while  empezar:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:

                    if event.key==pygame.K_y:
                        print (jugadores[0])
                        nombre_jugador2 = letra.render(jugadores[0], True, ROJO)
                        screen.blit(nombre_jugador2, [5, 5])
                        ##llamado del juego
                        if __name__ == '__main__':
                           main()
                    if event.key==pygame.K_r:
                        mostrar_puntajes()
                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                        quit()



        pygame.display.update()
        reloj.tick(1)


def comenzar_nuevo_juego():

    pygame.init()
    print(" Función que muestra un nuevo juego.")
    print("NUEVA VENTANA DEBE ABRIRSE")
    screen= pygame.display.set_mode((1010, 650))
    pygame.display.set_caption("JUGANDO AHORAAA.!!")

    screen.fill(BLANCO)
    fondo_menu2=pygame.image.load("Imagenes/fondo_personajes.jpg").convert()
    screen.blit(fondo_menu2, (0,0))
    fondo_instrucciones=pygame.image.load("Imagenes/menu_juego.jpg")
    screen.blit(fondo_instrucciones,(675,100))


    #Personajes
    pantalla_instrucciones()


    while True:
            for evento in pygame.event.get():
                if evento.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type==KEYDOWN:
                    if evento.key==pygame.K_x:
                        salir_del_programa()
                    if evento.key==pygame.K_r:
                        mostrar_puntajes()


            pygame.display.update()

def mostrar_puntajes():
    pygame.init()
    print(" Función que muestra muntajes maximos")
    print("puntajes en un archivo txt")
    pygame.display.set_caption("PUNTAJES!!")
    screen = pygame.display.set_mode((1000, 500))
    screen.fill(BLANCO)
    fondo_puntajes = pygame.image.load("Imagenes/fondo_verde.jpg").convert_alpha()
    icon_puntajes = pygame.image.load("Imagenes/icono_puntajes.png").convert_alpha()
    salir=pygame.image.load("Imagenes/exit.png")
    screen.blit(fondo_puntajes, (0, 0))
    screen.blit(icon_puntajes, (450, 20))
    screen.blit(salir, (0, 0))
    text = pygame.font.Font(None, 30)
    pygame.mixer.music.load("audios/open.mp3")
    pygame.mixer.music.play(1)
    with open("puntajes.txt") as f:
        instructText = text.render(f.read(), True, AZUL)
        screen.blit(instructText, [350, 200])


    while True:
            for evento in pygame.event.get():
                if evento.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type==KEYDOWN:
                    if evento.key==pygame.K_x:
                        salir_del_programa()
            pygame.display.update()



def salir_del_programa():
    import sys
    print(" Gracias por utilizar este programa.")
    sys.exit(0)

###############



############
if __name__ == '__main__':


    salir = False
    opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("Puntajes", mostrar_puntajes),
        ("Salir", salir_del_programa)
    ]

    ##########3

    ######

    pygame.font.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((850, 600))
    pygame.display.set_caption("JUEGO DONKEY-KONG")
    fondo = pygame.image.load("Imagenes/intro.jpg").convert()
    mapa_menu = pygame.image.load("Imagenes/menu1_juego.jpg").convert()
    imagen_opciones=pygame.image.load("Imagenes/opc.png")
    pygame.display.set_icon(pygame.image.load("Imagenes/icono.jpg").convert_alpha())# icono del juego
    relojmenu = pygame.time.Clock()
    pygame.mixer.music.load('audios/music_intro.mp3')## audio de intro y seleccionos de opciones
    pygame.mixer.music.play(2)#numero de veces que se repite la cancion de intro
    menu = Menu(opciones)
    ###var globales


    ### fin var global

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        screen.blit(fondo, (0, 0))
        screen.blit(mapa_menu, (130, 200))
        screen.blit(imagen_opciones,(125,250))
        menu.actualizar()
        menu.imprimir(screen)



        pygame.display.flip()
        pygame.time.delay(10)
        ###


