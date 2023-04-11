import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((20,0,200))# fill- värvid
pygame.display.set_caption("Esimine aken")# set_caption - 
ristkülik=pygame.Rect(0,300,640,180)
pygame.draw.rect(ekraani_pind,(0,255,0),ristkülik)


polygon=pygame.Rect(550,40,80,80)
pygame.draw.ellipse(ekraani_pind,(252,252,10),polygon)

#Maja
ristkülik=pygame.Rect(100,200,100,100)
pygame.draw.rect(ekraani_pind,(175,39,12),ristkülik)

#
#joon=pygame.Rect(0,0,100,100)
#pygame.draw.line(ekraani_pind(0,100,100),joon)

#pilt
pilt=pygame.image.load("vihm.png")
ekraani_pind.blit(pilt,(50,30))

#tekst
tekst_font=pygame.font.SysFont("Banschrift Light",40)#Tekat 1- schrift, 2- koht
sõnad="Tere tulemast!"
varv=[200,200,200]
teksti_lisamine=tekst_font.render(sõnad,False,varv)
ekraani_pind.blit(teksti_lisamine, (200,25))








pygame.display.flip()
while True:
    event=pygame.event.poll()# poll - proverjaet sobitija
    if event.type==pygame.QUIT:
        break
pygame.quit()