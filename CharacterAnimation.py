from head import *

class CharacterAnimation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        self.moved_left = False
        self.no_move = True

        self.index_frame = 0 #that keeps track on the current index of the image list.
        self.current_frame = 0 #that keeps track on the current time or current frame since last the index switched.
        
        self.current_animation = "idle"

    def resetAnimationFrame(self):
        self.index_frame = 0
        self.current_frame = 0

    def animate(self):
        animation = ""
        if self.attacking:
            animation = "attack"
        elif self.jumping :
            animation = "jump"
        elif not self.no_move :
            if self.running :
                animation = "run"
            else :
                animation = "walk"
        else :
            animation = "idle"

        if self.current_animation != animation :
            self.resetAnimationFrame()
        self.current_animation = animation

        if self.current_animation == "attack" :
            self.attackAnimation()        
        elif self.current_animation == "jump" :
            self.jumpAnimation()
        elif self.current_animation == "run" :
            self.runAnimation()
        elif self.current_animation == "walk" :
            self.walkAnimation()
        elif self.current_animation == "idle" :
            self.idleAnimation()

    def jumpAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame,charSheet.get_height()/6*3,charSheet.get_width()/8,charSheet.get_height()/6))
        if self.moved_left :
                    self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame += 1
        if self.current_frame >= 12:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 8 :
                self.index_frame = 0  

    def runAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*4+charSheet.get_width()/8*self.index_frame,charSheet.get_height()/6*1,charSheet.get_width()/8,charSheet.get_height()/6))
        if self.moved_left :
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame += 1
        if self.current_frame >= 12:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 4 :
                self.index_frame = 0  

    def walkAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame,charSheet.get_height()/6*1,charSheet.get_width()/8,charSheet.get_height()/6))
        if self.moved_left :
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame += 1
        if self.current_frame >= 12:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 4 :
                self.index_frame = 0  

    def idleAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame,0,charSheet.get_width()/8,charSheet.get_height()/6))
        if self.moved_left :
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame += 1
        if self.current_frame >= 12:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 2 :
                self.index_frame = 0  

    def attackAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*2+charSheet.get_width()/8*self.index_frame,0,charSheet.get_width()/8,charSheet.get_height()/6))
        if self.moved_left :
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame += 1
        if self.current_frame >= 8:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 2 :
                self.index_frame = 0  
                self.attacking = False



