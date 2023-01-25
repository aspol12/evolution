from sys import *
import pygame
import numpy as np
pygame.init()

# nothing = 0
# wall = 1
# goal = 2
# death = 3
# robot = 4

PIXEL_SIZE = 20
title = "Evolution"
icontitle = ""

gridWidth = 32
gridHeight = 32
grid = np.zeros((gridWidth, gridHeight), dtype=np.int32)
selected = 1

pygame.display.set_caption(title, icontitle)

size = w, h = 640, 740
screen = pygame.display.set_mode(size)

robot_image = pygame.Surface((25, 25))
robot_image.fill((255, 0, 0))
robot_rect = robot_image.get_rect()

inputs = []

robots = 0

gui_height = 100
gui_section = pygame.Surface((640, gui_height))
gui_section.fill((200, 200, 200))

mouse_pressed = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pressed = True

        elif event.type == pygame.MOUSEMOTION:
            if(mouse_pressed):
                row = event.pos[0] // PIXEL_SIZE
                col = event.pos[1] // PIXEL_SIZE
                if 0 <= row < gridHeight and 0 <= col < gridWidth:
                    if(selected == 1):
                        pygame.draw.rect(screen, (18, 181, 29), (row*20, col*20, 20, 20))
                        grid[row][col] = 1
                    elif(selected == 2):
                        pygame.draw.rect(screen, (255, 0, 255), (row*20, col*20, 20, 20))
                        grid[row][col] = 2
                    elif(selected == 3):
                        pygame.draw.rect(screen, (20, 16, 235), (row*20, col*20, 20, 20))
                        grid[row][col] = 3
                    elif((selected == 4) and (robots < 1)):
                        pygame.draw.rect(screen, (255, 0, 0), (row*20, col*20, 20, 20))
                        grid[row][col] = 4
                        robots += 1

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_pressed = False
            

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                grid = np.zeros((gridHeight, gridWidth), dtype=np.int32)
                screen.fill((0, 0, 0))
                robots = 0
            elif event.key == pygame.K_1:
                selected = 1
            elif event.key == pygame.K_2:
                selected = 2
            elif event.key == pygame.K_3:
                selected = 3
            elif event.key == pygame.K_4:
                selected = 4

        screen.blit(gui_section, (0, 640))

    mouse_pos = pygame.mouse.get_pos()
    pygame.display.flip()

