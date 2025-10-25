import pygame
from pygame import font, display, draw, event

pygame.init()
screen = display.set_mode((600,600))
display.set_caption("testing ... testing...")


tail = pygame.Rect(10,120,140,50)
backLeg = pygame.Rect(160,120,50,170)
tummy = pygame.Rect(220,120,50,100)
frontLeg = pygame.Rect(280,120,50,170)
neck = pygame.Rect(340,110,50,85)
head = pygame.Rect(400,80,90,65)
nose = pygame.Rect(450,80,40,15)
eye1 = pygame.Rect(410,92,10,10)
eye2 = pygame.Rect(432,92,10,10)

draw.rect(screen, "green", tail)
draw.rect(screen, "purple", backLeg)
draw.rect(screen, "yellow", tummy)
draw.rect(screen, "coral", frontLeg)
draw.rect(screen, "blue", neck)
draw.rect(screen, "red", head)
draw.rect(screen, "black", nose)
draw.rect(screen, "pink", eye1)
draw.rect(screen, "cyan", eye2)
while True:
    display.update()