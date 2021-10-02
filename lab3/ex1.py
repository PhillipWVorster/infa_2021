import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (200, 200, 200), (0, 0, 400, 400))

circle(screen, (255, 250, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 1)

circle(screen, (255, 0, 0), (155, 155), 20)
circle(screen, (0, 0, 0), (155, 155), 20, 1)
circle(screen, (0, 0, 0), (155, 155), 8)
polygon(screen, (0, 0, 0), [(180, 140), (183, 130), (93, 100), (90, 110)])


circle(screen, (255, 0, 0), (245, 155), 16)
circle(screen, (0, 0, 0), (245, 155), 16, 1)
circle(screen, (0, 0, 0), (245, 155), 8)
polygon(screen, (0, 0, 0), [(222, 140), (220, 130), (300, 118), (302, 128)])

rect(screen, (0, 0, 0), (150, 220, 100, 22))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
