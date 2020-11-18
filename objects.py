import pygame
import os


class Field(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.image_adress = os.path.join('Images', 'None.png')
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.my_image = pygame.transform.scale(
            self.my_image, (self.scale, self.scale))
        self.stage = None
        self.rect = pygame.Rect(self.x, self.y, self.scale, self.scale)
        self.hi = {
            'g': [None]*4,
            'v': [None]*4,
            'r': [None]*4,
            'l': [None]*4,
        }

    def change(self, how):
        self.stage = how
        self.image_adress = os.path.join('Images', f'{str(how)}.png')
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.my_image = pygame.transform.scale(
            self.my_image, (self.scale, self.scale))

    def crew(self, how, vect, ind):
        self.hi[vect][ind] = how

    def check(self):
        ret = None
        for i in ['g', 'v', 'l', 'r']:
            if dict(self.hi)[i] == [True]*4 and self.stage == True:
                ret = True
                break
            elif dict(self.hi)[i] == [False, False, True, True] and self.stage == False:
                ret = False
                break
            else:
                pass
        return ret

    def draw(self, screen):
        screen.blit(self.my_image, (self.x, self.y))
