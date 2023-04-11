import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((20,0,200))# fill- värvid
pygame.display.set_caption("Esimine aken")# set_caption - 
ristkülik=pygame.Rect(0,300,640,180)
pygame.draw.rect(ekraani_pind,(0,255,0),ristkülik)
