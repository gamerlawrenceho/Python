from random import randint
import pygame
import sys


def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否在指定的區域內"""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()
width = 640
height = 320

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lawrence")

bg = pygame.Surface((width, height))  # 建立畫布
bg.fill((0, 250, 255))  # 畫布顏色

typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render("Start", True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()

# for i in range(10, 251, 10):
#     pygame.draw.rect(bg, (0, i, 255), [0, 0, i, i], 10)

# for i in range(10, 251, 10):
#     pygame.draw.circle(bg, (0, i, 255), (width, 0), i, 10)

# pygame.draw.rect(bg, (0, 10, 255), [0, 0, 10, 10], 10)
paint = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if check_click(pos, 20, 20, 20 + tit_w, 20 + tit_h):
                for i in range(10, 251, 10):
                    pygame.draw.rect(bg, (0, i, 255), [0, 0, i, i], 10)

                for i in range(10, 251, 10):
                    pygame.draw.circle(bg, (0, i, 255), (width, 0), i, 10)
            else:
                if event.button == 1:
                    color = (255, 0, 0)
                if event.button == 3:
                    color = (255, 255, 255)
                paint = not (paint)

    if paint:
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(bg,
                           (randint(0, 255), randint(0, 255), randint(0, 255)),
                           (x, y), 30, 0)
        # pygame.draw.circle(bg, (0, 150, 255), (x, y), 10, 0)

        # pygame.draw.circle(bg, (0, 0, 255), (x, y), 5, 0)

    screen.blit(bg, (0, 0))
    screen.blit(title, (20, 20))
    pygame.display.update()
