from head import *

class Platform(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.surf = platformImg
        self.rect = self.surf.get_rect(center = pos)

    def display(self, surface, camera):
        surface.blit(self.surf, (self.rect.x - camera.pos.x, self.rect.y - camera.pos.y - 25))

    def move(self):
        pass

class PlatformBasik(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center = pos)

    def display(self, surface, camera):
        surface.blit(self.surf, (self.rect.x - camera.pos.x, self.rect.y - camera.pos.y))

    def move(self):
        pass