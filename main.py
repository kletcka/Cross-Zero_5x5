import random
import objects
import pygame
import time
pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
hm = 5
list_of_f = {}
alli = ['lu', 'ld', 'ru', 'rd', 'u', 'd', 'l', 'r']
liste = {'lu': ('l', 1), 'ld': ('l', 0), 'ru': ('r', 1), 'rd': (
    'r', 0), 'u': ('v', 1), 'd': ('v', 0), 'l': ('g', 1), 'r': ('g', 0), }
for i in range(0, hm):
    for j in range(0, hm):
        list_of_f[i, j] = objects.Field(i*WIDTH//hm, j*HEIGHT//hm)

done = False
which = True
answers = {True: 'Крестики выиграли', False: 'Нолики выиграли', None: 'Ничья'}
ans = None
mode = True


while not done:
    screen.fill((0, 0, 0))
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
                        pos = (list_of_f[i].x//(WIDTH//hm), list_of_f[i].y//(HEIGHT//hm))
                        l = {}
                        l['lu'] = (pos[0]-1, pos[1]-1)
                        l['ld'] = (pos[0]+1, pos[1]+1)
                        l['ru'] = (pos[0]+1, pos[1]-1)
                        l['rd'] = (pos[0]-1, pos[1]+1)
                        l['u'] = (pos[0], pos[1]-1)
                        l['d'] = (pos[0], pos[1]+1)
                        l['l'] = (pos[0]-1, pos[1])
                        l['r'] = (pos[0]+1, pos[1])

                        for i in alli:
                            a = l[i]
                            b = liste[i]
                            try:
                                list_of_f[a[0], a[1]].crew(which, b[0], b[1])
                            except Exception:
                                pass

                        which = not which
            elif pygame.mouse.get_pressed()[0] == 1 and pygame.key.get_pressed()[pygame.K_DOWN]:
                pos = pygame.mouse.get_pos()
                d = list_of_f[pos[0]//(WIDTH//hm), pos[1]//(HEIGHT//hm)]
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

        liza = True
        for i in list(list_of_f.values()):
            a = i.check()
            if i.stage == None:
                liza = False
            if a != None:
                ans = a
                mode = False
        if liza == True:
            mode = False
    elif mode == False:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                done = True
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                mode = True
                list_of_f = {} 
                for f in range(0, hm):
                    for j in range(0, hm):
                        list_of_f[f, j] = objects.Field(f*WIDTH//hm, j*HEIGHT//hm)
                which = True
                ans = None
        font = pygame.font.Font(pygame.font.match_font('arial'), 70)
        text_surface = font.render(answers[ans], True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (300, 100)
        screen.blit(text_surface, text_rect)
        font = pygame.font.Font(pygame.font.match_font('arial'), 35)
        text_surface1 = font.render('Нажмите на пробел, чтобы продолжить', True, (255, 255, 255))
        text_rect1 = text_surface.get_rect()
        text_rect1.midtop = (290, 400)
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface1, text_rect1)
    pygame.display.flip()

pygame.quit()