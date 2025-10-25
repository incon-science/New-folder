from Character import *
from Platform import *
from Text import *
from Player import *
from Camera import *
from Tentacule_new import *


camera = Camera()

for i in range(0,1):
    for j in range(0,i+1):
        PL = Platform((- i*300 + j*600, 300 + i*300))
        all_sprites.add(PL)
        platforms.add(PL)




# Créer deux tentacules dans des directions opposées
T1 = Tentacule((-500, 230), "east")  # Tentacule vers la droite
all_sprites.add(T1)

P1 = Player()
all_sprites.add(P1)

T2 = Tentacule((500, 250), "west")  # Tentacule vers la gauche
all_sprites.add(T2)

T3 = Tentacule((-500, 250), "east")  # Tentacule vers la gauche
all_sprites.add(T3)
T4 = Tentacule((500, 240), "west")  # Tentacule vers la gauche
all_sprites.add(T4)
T5 = Tentacule((500, 220), "west")  # Tentacule vers la gauche
all_sprites.add(T5)

text = Text("Viens à moi",(255,255,255),10,(WIDTH/2,HEIGHT-10),font='Lucida Console', bg_color=(0,0,0), padding=2, bg_alpha=255)


while 1:
    if P1.pos.y - camera.pos.y > HEIGHT-50 :
        P1.respawn(camera)

    P1.checkCollisions()


    for event in pygame.event.get():
        P1.controls(event)

    #fond noir
    display_surf.fill((50,50,50))
    display_surf.blit(bgImg, (0, 0))

    #update camera
    camera.update(P1)
    
    display_surf.blit(eyeImg, (WIDTH/2-150,0))
    #deplacer les sprites 
    for entity in all_sprites:
        entity.move()
        entity.display(display_surf, camera)

    display_surf.blit(text.surf, text.rect)


    #resize and blit surf on screen
    screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

    #show fps
    show_fps = Text(str(int(FramePerSec.get_fps())),(255,255,255),20,(20,15))
    show_fps.display(screen)

    pygame.display.update()
    FramePerSec.tick(FPS)