from Character import *

class Player(Character):
    def __init__(self):
        super().__init__()  

    def controls(self,event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                self.jump()
        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_SPACE:
                self.cancel_jump()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.stopattacking :
                self.attacking = True
                self.stopattacking = False
        if event.type == pygame.MOUSEBUTTONUP:
            self.stopattacking = True

    def movements(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LSHIFT] :
            self.running = True
        else :
            self.running = False
                
        if pressed_keys[K_q] :
            self.moved_left = True
            self.no_move = False
        elif pressed_keys[K_d] :
            self.moved_left = False
            self.no_move = False
        else : 
            self.no_move = True
 
