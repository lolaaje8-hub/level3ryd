import pygame
from pygame import font, display, draw, event

pygame.init()
screen = display.set_mode((600,600))
display.set_caption("testing ... testing...")

box = pygame.Rect(100, 100, 200, 200)
draw.rect(screen, "red", box)

while True:
    display.update()