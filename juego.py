import pygame
from random import randint
pygame.init()
sonido_fondo = pygame.mixer.Sound("sonidos/fondo.mp3")
sonido_golpe=pygame.mixer.Sound("sonidos/golpe.mp3")
sonido_gameover=pygame.mixer.Sound("sonidos/gameover.mp3")
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Mi juego")
ball = pygame.image.load("imagenes/ball.png")
ball = pygame.transform.scale(ball, (20, 20))
ballrect = ball.get_rect()
# La velocidad se calcular con un valor pseudialeatorio entre 3,6
speed = [randint(10,18),randint(4,8)]
ballrect.move_ip(0,0)
bate = pygame.image.load("imagenes/bate.png")
baterect = bate.get_rect()
baterect.move_ip(240,450)
# Esta es la fuente que usaremos para el texto que aparecerá en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)
# Bucle principal
jugando = True
while jugando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-15,0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(15,0)
    
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0: 
        speed[1] = -speed[1]
        pygame.mixer.Sound.play(sonido_golpe)
    # Si la pelota toca el border inferior, has perdido ("Game Over")
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125,125,125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        pygame.mixer.Sound.play(sonido_gameover)
        ventana.blit(texto, [texto_x, texto_y])
    

    else:
        pygame.mixer.Sound.play(sonido_fondo)
        fondo = pygame.image.load("imagenes/espacio.jpg")
        
        ventana.blit(fondo,(0,0))
        ventana.blit(ball, ballrect)
        # Dibujo el bate
        ventana.blit(bate, baterect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
