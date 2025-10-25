from head import *
from scipy.interpolate import interp1d
import math

class Camera():
    def __init__(self):
        self.pos = vec(round(-WIDTH/2),round(-HEIGHT/2))
        self.pos_aim = self.pos

        self.offset_moving = 0

    def update(self,player):
        self.pos_aim = vec(player.pos.x - WIDTH/2,player.pos.y - HEIGHT/2)

        if player.moved_left :
            self.pos_aim.x -= self.offset_moving
        else :
            self.pos_aim.x += self.offset_moving

        self.updateCameraCenterSmooth()

    def updateCameraCenterSmooth(self):
        dif_x = self.pos_aim.x - self.pos.x
        offset_x = self.calculOffsetXCubique(dif_x)
        self.pos.x += offset_x

        dif_y = self.pos_aim.y - self.pos.y
        offset_y = self.calculOffsetYCubique(dif_y)
        self.pos.y += offset_y

    def calculOffsetXCubique(self,diff_x):

        x = diff_x / (WIDTH/2) *4
        rez = x*x*x

        return int(rez)

    def calculOffsetYCubique(self,diff_y):

        y = diff_y / (HEIGHT/2) *4
        rez = y*y*y

        return int(rez)

    def calculOffsetX(self,diff_x):

        X = [-WIDTH/2, -self.offset_moving,0,self.offset_moving, WIDTH/2] # random x values
        Y = [-100, -1,0,1, 100] # random y values

        # Finding the interpolation
        y_interp = interp1d(X, Y, kind='slinear')

        rez = y_interp(diff_x)

        return math.floor(rez)

    def calculOffsetY(self,diff_y):

        X = [-HEIGHT/2, 0, HEIGHT/2] # random x values
        Y = [-25, 0, 25] # random y values

        # Finding the interpolation
        y_interp = interp1d(X, Y, kind='slinear')

        rez = y_interp(diff_y)

        return math.floor(rez)