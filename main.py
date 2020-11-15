import random
import objects
import pygame
import time
pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

list_of_f = {}
for i in range(0, 5):
    for j in range(0, 5):
        list_of_f[i, j] = objects.Field(i*120, j*120)

alli = ['lu', 'ld', 'ru', 'rd', 'u', 'd', 'l', 'r']
liste = {'lu': ('l', 1), 'ld': ('l', 0), 'ru': ('r', 1), 'rd': (
    'r', 0), 'u': ('v', 1), 'd': ('v', 0), 'l': ('g', 1), 'r': ('g', 0), }
done = False
which = True
answers = {True: 'Крестики выиграли', False: 'Нолики выиграли', None: 'Ничья'}
ans = None
while not done:
    screen.fill((0, 0, 0))
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
        if pygame.mouse.get_pressed()[0] == 1 and not pygame.key.get_pressed()[pygame.K_DOWN]:
            pos = pygame.mouse.get_pos()
            for i in list_of_f:
                if list_of_f[i].rect.collidepoint(pos) and list_of_f[i].stage == None:
                    list_of_f[i].change(which)
                    pos = (list_of_f[i].x//120, list_of_f[i].y//120)
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
            d = list_of_f[pos[0]//120, pos[1]//120]
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
            done = True
    if liza == True:
        done = True

    pygame.display.flip()


pygame.quit()
print(answers[ans])
