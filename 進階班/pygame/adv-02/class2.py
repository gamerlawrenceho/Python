######################匯入模組######################
from random import randint
import pygame
import sys
import os


####################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    "c" "判斷滑鼠是否在指定的區域內" ""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)

bg_x = bg.get_width()
bg_y = bg.get_height()
######################建立視窗######################
screen = pygame.display.set_mode((bg_x, bg_y))
pygame.display.set_caption("Snow")
####################撥放音樂######################

####################設定文字######################
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render("Start", True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()
####################設定雪花基本參數######################

####################新增fps######################

######################循環偵測######################
paint = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if check_click(pos, 20, 20, 20 + tit_w, 20 + tit_h):
                paint = not (paint)
            else:
                pass

    if paint:
        title = font.render("Start", True, (0, 0, 0))
    else:
        title = font.render("Stop", True, (0, 0, 0))

    screen.blit(bg, (0, 0))
    screen.blit(title, (20, 20))
    pygame.display.update()