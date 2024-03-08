# import time
# import pyautogui
#
# def func():
#     time.sleep(2)
#     while True:
#         pyautogui.doubleClick()
#
#
# func()




# a = [1,2,3,4]
# b = [1,2,3,1]
#
# for i in b:
#     if b.count(i) > 1:
#         print('t')
#         break



# a = print('Взросл') if int(input(''))>20 else print('Мал')



import pygame
import random

def f():
    pygame.init()
    dis = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Test')
    apple = random.randint(1,120)* 10, random.randint(1,80) * 10
    red = (255, 0, 0)
    SIZE = 50
    SIZE_SNEACK = 50

    flag = True
    bg = (0, 0, 255)
    x = 600
    y = 400

    sneak = [(x , y)]

    x1_change = 0
    y1_change = 0

    clock = pygame.time.Clock()

    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
        x += x1_change
        y += y1_change
        dis.fill((0, 0, 0))
        # if sneak[-1] == apple:
        #     apple = random.randint(1, 120) * 10, random.randint(1, 80) * 10
        #     SIZE_SNEACK *= 2
        sneak.append((x, y))
        s = pygame.draw.rect(dis, bg, [sneak[-1][0], sneak[-1][1], SIZE_SNEACK, 50])
        pygame.draw.rect(dis, red, [*apple ,  50, 50])
        if sneak[-1] == apple:
            apple = random.randint(1, 120) * 10, random.randint(1, 80) * 10
            s += s
        pygame.display.update()

        clock.tick(20)
f()

































































