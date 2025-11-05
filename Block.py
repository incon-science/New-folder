from head import *

class Block(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.surf = pygame.Surface((16,16))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = pos)

    def display(self, surface, camera):
        surface.blit(self.surf, (self.rect.x - camera.pos.x, self.rect.y - camera.pos.y))

    def move(self):
        pass