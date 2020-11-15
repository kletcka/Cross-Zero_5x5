import pygame
import os
class Field(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_adress = os.path.join('Images', 'None.png')
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.my_image = pygame.transform.scale(self.my_image, (120, 120))
        self.stage = None
        self.rect = pygame.Rect(self.x, self.y, 120, 120)
        self.hi = {
            'g':[None, None],
            'v':[None, None],
            'r':[None, None],
            'l':[None, None],
        }
    def change(self, how):
        self.stage = how
        self.image_adress = os.path.join('Images', f'{str(how)}.png')
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.my_image = pygame.transform.scale(self.my_image, (120, 120))
    def crew(self, how, vect, ind):
        self.hi[vect][ind] = how
    def check(self):
        ret = None
        for i in ['g', 'v', 'l', 'r']:
                if dict(self.hi)[i] == [True, True] and self.stage == True:
                    ret = True
                    break
                elif  dict(self.hi)[i] == [False, False] and self.stage == False:
                    ret = False
                    break
                else:
                    pass
        return ret
    def draw(self, screen):
        screen.blit(self.my_image,(self.x, self.y))