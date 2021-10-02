import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 750))

rect(screen, (20, 30, 40), (0, 0, 500, 400))
rect(screen, (40, 50, 0), (0, 400, 500, 400))

# sky
circle(screen, (255, 255, 255), (300, 200), 75)
ellipse(screen, (110, 110, 110),[-200, 30, 500, 130])
ellipse(screen, (110, 110, 110),[300, 0, 800, 100])
ellipse(screen, (110, 110, 110),[220, 120, 600, 80])
ellipse(screen, (110, 110, 110),[180, 210, 500, 80])
ellipse(screen, (110, 110, 110),[-200, 180, 500, 80])
ellipse(screen, (60, 60, 60),[100, 90, 500, 70])
ellipse(screen, (60, 60, 60),[-200, 160, 400, 80])
ellipse(screen, (60, 60, 60),[120, 260, 440, 80])

# spaceship
polygon(screen, (80, 100, 120), [(84, 340), (132, 340), (222, 480), (4, 480)])
#polygon(screen, (60, 80, 0), [(84, 400), (132, 400), (222, 480), (4, 480)])
ellipse(screen, (160, 160, 160),[18, 274, 190, 68])
ellipse(screen, (200, 200, 200),[40, 270, 148, 46])
ellipse(screen, (255, 255, 255),[26, 305, 22, 10])
ellipse(screen, (255, 255, 255),[48, 318, 22, 10])
ellipse(screen, (255, 255, 255),[80, 324, 22, 10])
ellipse(screen, (255, 255, 255),[116, 324, 22, 10])
ellipse(screen, (255, 255, 255),[148, 318, 22, 10])
ellipse(screen, (255, 255, 255),[178, 306, 22, 10])

#alien
ellipse(screen, (190, 200, 180),[300, 440, 15, 12])
ellipse(screen, (190, 200, 180),[302, 450, 12, 6])
ellipse(screen, (190, 200, 180),[310, 458, 10, 10])
ellipse(screen, (190, 200, 180),[316, 470, 6, 8])

circle(screen, (190, 200, 180), (320, 488),8)
polygon(screen, (190, 200, 180), [(318,480),(320,480),(360,478),(370,482),(372,484),(374,486),(370,500),(366,508),(354,524),(350,528),(346,530),(348,530),(340,530),(336,528),(332,526),(320,510),(314,494),(320,500)])

ellipse(screen, (190, 200, 180),[366, 474, 10, 10])
ellipse(screen, (190, 200, 180),[370, 468, 6, 9])
ellipse(screen, (190, 200, 180),[374, 458, 9, 9])
ellipse(screen, (190, 200, 180),[386, 453, 8, 8])
ellipse(screen, (190, 200, 180),[398, 452, 12, 16])
ellipse(screen, (190, 200, 180),[320, 532, 32, 68])

circle(screen, (190, 200, 180), (322, 540), 8)
ellipse(screen, (190, 200, 180),[308, 544, 13, 10])
ellipse(screen, (190, 200, 180),[306, 556, 6, 8])

circle(screen, (190, 200, 180), (356, 542), 8)
ellipse(screen, (190, 200, 180),[358, 544, 14, 10])
ellipse(screen, (190, 200, 180),[370, 550, 18, 10])

ellipse(screen, (190, 200, 180),[314, 576, 15, 25])
ellipse(screen, (190, 200, 180),[311, 598, 11, 26])
circle(screen, (190, 200, 180), (306, 620,), 8)

ellipse(screen, (190, 200, 180),[342, 584, 15, 25])
ellipse(screen, (190, 200, 180),[346, 608, 11, 26])
circle(screen, (190, 200, 180), (362, 630,), 8)


circle(screen, (0, 0, 0), (330, 498), 9)
circle(screen, (0, 0, 0), (360, 500), 7)
circle(screen, (255, 255, 255), (332, 502), 2)
circle(screen, (255, 255, 255), (362, 502), 2)

#apple
circle(screen, (190, 0, 0), (394, 540), 15)
polygon(screen, (160, 200, 0), [(394, 522), (392, 520), (390, 512), (394, 518)])
line(screen, (0,0,0), (394,526), (400,510), 1)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
