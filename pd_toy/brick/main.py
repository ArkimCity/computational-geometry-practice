import pygame
import sys
from Consts import consts
from Components import bricks, bar

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
pygame.display.set_caption("Brick Game!")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x, pos_y = 200, SCREEN_HEIGHT - 50
move_x = 20

white = (255, 255, 255) # rgb
black = (0, 0, 0)

clock = pygame.time.Clock()
user_bar = bar(screen, white, 10, 50)

## actual running loop
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= move_x
    elif key_event[pygame.K_RIGHT]:
        pos_x += move_x

    # if key_event[pygame.K_UP]:
    #     pos_y -= 1
    # if key_event[pygame.K_DOWN]:
    #     pos_y += 1

    screen.fill(black)
    # pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
    pygame.draw.rect(screen, white, (pos_x, pos_y, 50,10), 0)
    pygame.display.update()

