import random
import time
import json
import pygame
import objects

pygame.init()

settings = dict()

with open('settings.json', 'r', encoding='utf-8') as read_file:
    settings = json.load(read_file)

HM = int(settings['set_numbers_of_cells'])
WI = int(settings['set_width_of_cells'])
WIDTH = HM*WI
HEIGHT = HM*WI
BACKFILL = (settings['colors']['back_color']['r'], settings['colors']
            ['back_color']['g'], settings['colors']['back_color']['b'])
TEXTFILL = (settings['colors']['text_color']['r'], settings['colors']
            ['text_color']['g'], settings['colors']['text_color']['b'])
NEXTN = settings['texts']['new']
ANSWERS = {True: settings['texts']['x_wins'], False:  settings['texts']
           ['o_wins'], None:  settings['texts']['no_wins']}


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


liste = {'lu': ('l', 2),
         'ld': ('l', 1),
         'ru': ('r', 2),
         'rd': ('r', 1),
         'u': ('v', 2),
         'd': ('v', 1),
         'l': ('g', 2),
         'r': ('g', 1),

         'lu1': ('l', 3),
         'ld1': ('l', 0),
         'ru1': ('r', 3),
         'rd1': ('r', 0),
         'u1': ('v', 3),
         'd1': ('v', 0),
         'l1': ('g', 3),
         'r1': ('g', 0),
         }


done = False
which = True
ans = None
mode = True
list_of_f = {}


def reset():
    global list_of_f
    list_of_f = {}
    for i in range(0, HM):
        for j in range(0, HM):
            list_of_f[i, j] = objects.Field(i*WI, j*WI, WI)


reset()

while not done:
    screen.fill(BACKFILL)
    clock.tick(60)
    if mode == True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                done = True
            if pygame.mouse.get_pressed()[0] == 1 and not pygame.key.get_pressed()[pygame.K_DOWN]:
                pos = pygame.mouse.get_pos()
                for i in list_of_f:
                    if list_of_f[i].rect.collidepoint(pos) and list_of_f[i].stage == None:
                        list_of_f[i].change(which)
                        pos = (list_of_f[i].x//(WIDTH//HM),
                               list_of_f[i].y//(HEIGHT//HM))
                        l = {}
                        l['lu'] = (pos[0]-1, pos[1]-1)
                        l['ld'] = (pos[0]+1, pos[1]+1)
                        l['ru'] = (pos[0]+1, pos[1]-1)
                        l['rd'] = (pos[0]-1, pos[1]+1)
                        l['u'] = (pos[0], pos[1]-1)
                        l['d'] = (pos[0], pos[1]+1)
                        l['l'] = (pos[0]-1, pos[1])
                        l['r'] = (pos[0]+1, pos[1])

                        l['lu1'] = (pos[0]-2, pos[1]-2)
                        l['ld1'] = (pos[0]+2, pos[1]+2)
                        l['ru1'] = (pos[0]+2, pos[1]-2)
                        l['rd1'] = (pos[0]-2, pos[1]+2)
                        l['u1'] = (pos[0], pos[1]-2)
                        l['d1'] = (pos[0], pos[1]+2)
                        l['l1'] = (pos[0]-2, pos[1])
                        l['r1'] = (pos[0]+2, pos[1])
                        for i in list(liste.keys()):
                            a = l[i]
                            b = liste[i]
                            try:
                                list_of_f[a[0], a[1]].crew(which, b[0], b[1])
                            except Exception:
                                pass

                        which = not which
            elif pygame.mouse.get_pressed()[0] == 1 and pygame.key.get_pressed()[pygame.K_DOWN]:
                pos = pygame.mouse.get_pos()
                d = list_of_f[pos[0]//(WIDTH//HM), pos[1]//(HEIGHT//HM)]
                print(d.hi)
                for f in ['g', 'v', 'l', 'r']:
                    if dict(d.hi)[f] == [True, True] and d.stage == True:
                        print(True)

                    elif dict(d.hi)[f] == [False, False] and d.stage == False:
                        print(False)
                    else:
                        print(None)

        for i in list_of_f:
            list_of_f[i].draw(screen)

        flag = True
        for i in list(list_of_f.values()):
            a = i.check()
            if i.stage == None:
                flag = False
            if a != None:
                ans = a
                mode = False
        if flag == True:
            mode = False
    elif mode == False:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                done = True
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                mode = True
                list_of_f = {}
                reset()
                which = True
                ans = None
        font = pygame.font.Font(pygame.font.match_font('arial'), WIDTH//10)
        text_surface = font.render(ANSWERS[ans], True, TEXTFILL)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH//2, HEIGHT//3)
        screen.blit(text_surface, text_rect)
        font = pygame.font.Font(pygame.font.match_font('arial'),  WIDTH//20)
        text_surface1 = font.render(NEXTN, True, TEXTFILL)
        text_rect1 = text_surface.get_rect()
        text_rect1.midtop = (WIDTH//2, HEIGHT//3*2)
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface1, text_rect1)
    pygame.display.flip()

pygame.quit()
