from Character import *
from Platform import *
from Text import *
from Player import *
from Camera import *


camera = Camera()

for i in range(0,3):
    for j in range(0,i+1):
        PL = PlatformBasik((- i*300 + j*600, 300 + i*300), (200,20))
        all_sprites.add(PL)
        platforms.add(PL)





P1 = Player()
all_sprites.add(P1)



while 1:
    if P1.pos.y - camera.pos.y > HEIGHT-50 :
        P1.respawn(camera)

    P1.checkCollisions()


    for event in pygame.event.get():
        P1.controls(event)

    #fond noir
    display_surf.fill((50,50,50))

    #update camera
    camera.update(P1)
    
    #deplacer les sprites 
    for entity in all_sprites:
        entity.move()
        entity.display(display_surf, camera)



    #resize and blit surf on screen
    screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

    #show fps
    show_fps = Text(str(int(FramePerSec.get_fps())),(255,255,255),20,(20,15))
    show_fps.display(screen)

    pygame.display.update()
    FramePerSec.tick(FPS)