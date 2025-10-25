from CharacterAnimation import *

class Character(CharacterAnimation):
    def __init__(self):
        super().__init__() 
        self.surf = charSheet.subsurface((0,0,charSheet.get_width()/8,charSheet.get_height()/6))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((0, 0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.jumping = False
        self.running = False

        self.attacking = False
        self.stopattacking = True

    def display(self, surface, camera):
        surface.blit(self.surf, (self.rect.x - camera.pos.x, self.rect.y - camera.pos.y))

    def move(self):
        self.acc = vec(0,0.5)
    
        self.movements()

        if self.running :
            ACC = 0.5
            FRIC = -0.12
        else :
            ACC = 0.25
            FRIC = -0.12
        
        if not self.no_move :
            if self.moved_left :
                self.acc.x = -ACC
            else :
                self.acc.x = ACC
                 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
             
        self.rect.midbottom = self.pos

        self.animate()
 
    def jump(self): 
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -8
 
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def checkCollisions(self):
        hits = pygame.sprite.spritecollide(self ,platforms, False)
        if self.vel.y > 0:        
            if hits:
                if self.pos.y < hits[0].rect.bottom:               
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False

    def respawn(self,camera):
        self.pos = vec((0,0))
        self.vel = vec(0,0)
        self.jumping = False

        camera.pos = vec(round(-WIDTH/2),round(-HEIGHT/2))
        camera.pos_aim = camera.pos
