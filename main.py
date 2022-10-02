
import pygame
import os
from pygame.locals import *
from classes import *


#helper functions
def relative(original_pixel,intended_relative_amt,divisor=100):
    '''
    helper function to convert from absolute to relative sizes. Divisor is used to increase precision. First 2 variables are tuples in the form of width, height
    '''
    ow,oh = original_pixel
    nw,nh = intended_relative_amt
    return ow*nw/divisor,oh*nh/divisor

#settings
width,height = 1280,720 #16x9
fps = 60
barsizex,barsizey = 18,20
baroffsetx,baroffsety =1,1
cardsizex,cardsizey = 205,118
cardoffsetx,cardoffsety =8,20
hpbarscale = relative((barsizex,barsizey),(90,90))
midoffsetx = 2
dragt = (50,50)
gamename = "E"

hp = 30
lust = 20
love = 20 
armor = 0
energy = 3
cardlist = []
#palette
white = (255,255,255)

#global settings
cardview_toggle = False
clickable = []

#asset import
hp_bar_raw = pygame.image.load(os.path.join('Assets','hp bar.png'))
hp_bar = pygame.transform.scale(hp_bar_raw, hpbarscale)
armor_bar = pygame.image.load(os.path.join('Assets','armor bar.png'))
energy_bar = pygame.image.load(os.path.join('Assets','energy bar.png'))
lust_bar = pygame.image.load(os.path.join('Assets','lust bar.png'))
love_bar = pygame.image.load(os.path.join('Assets','love bar.png'))
messenger = pygame.image.load(os.path.join('Assets','messenger.png'))
cardview = pygame.image.load(os.path.join('Assets','cardview.png'))
bf = pygame.image.load(os.path.join('Assets','bf.png'))
gf = pygame.image.load(os.path.join('Assets','gf.png'))
bgm =  os.path.join('Assets','loopable.mp3')

    #cards
ankle_pic_asset = pygame.image.load(os.path.join('Assets','cards','ankle pic.png'))
brb_asset = pygame.image.load(os.path.join('Assets','cards','brb.png'))
comeback_asset = pygame.image.load(os.path.join('Assets','cards','comeback.png'))
defend_asset = pygame.image.load(os.path.join('Assets','cards','defend.png'))
drunk_asset = pygame.image.load(os.path.join('Assets','cards','drunk text.png'))
flatter_asset = pygame.image.load(os.path.join('Assets','cards','flatter.png'))
cardlist = [brb_asset for i in range(9)]


#pygane init
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(gamename)

def main():
    pygame.mixer.music.load(bgm)
    pygame.mixer.music.play(-1)
    lclick = False
    drag = False
    dragl = [0,0]
    
    clock =pygame.time.Clock()
    run = True
    while run:
        mx,my = pygame.mouse.get_pos()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if lclick == False:
                        #on click
                        omx,omy = mx,my

            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if drag:
                        print("cancelled")
                    if not drag:
                        exceute()
                    lclick = False
                    dragl = [0,0]
                    drag = False
                    
        if lclick:
            dragl = [mx-omx,my-omy]
            if abs(dragl[0]) > dragt[0] and abs(dragl[1]) > dragt[1]:
                drag = True
        draw_window()
        
def draw_window():
    screen.blit(bf,(0,0))
    screen.blit(gf,(0,0))
    screen.blit(messenger,(0,0))

    for i in range(hp):
        is_mid =0
        if i%10 >= 5:
            is_mid = 1
        x = 1040 + (i%10) * (baroffsetx+hpbarscale[0])+ midoffsetx*is_mid
        y = 555 + (i//10) * (baroffsety+hpbarscale[1])
        screen.blit(hp_bar,(x,y))

    for i in range(armor):
        x = 1110 + (i%5) * (baroffsetx+barsizex)
        y = 670 + (i//5) * (baroffsety+barsizey)
        screen.blit(armor_bar,(x,y))
    
    for i in range(energy):
        x = 1110 + (i%5) * (baroffsetx+barsizex)
        y = 620 + (i//5) * (baroffsety+barsizey)
        screen.blit(energy_bar,(x,y))

    for i in range(lust):
        is_mid =0
        if i%10 >= 5:
            is_mid = 1
        x = 100 + (i%10) * (baroffsetx+barsizex)+ midoffsetx*is_mid
        y = 575 + (i//10) * (baroffsety+barsizey)
        screen.blit(lust_bar,(x,y))

    for i in range(love):
        is_mid =0
        if i%10 >= 5:
            is_mid = 1
        x = 100 + (i%10) * (baroffsetx+barsizex)+ midoffsetx*is_mid
        y = 640 + (i//10) * (baroffsety+barsizey)
        screen.blit(love_bar,(x,y))

    if cardview_toggle:
        screen.blit(cardview,(0,0))
        for i in range(len(cardlist)):
            x = 330 + (i%3) * (cardoffsetx+cardsizex)
            y = 280 + (i//3) * (cardoffsety+cardsizey)
            screen.blit(cardlist[i],(x,y))
    
    pygame.display.update()

def is_over(rect:Rect, pos):
    return rect.collidepoint(pos[0], pos[1])

def exceute():
    global cardview_toggle
    cardview_toggle = not cardview_toggle
    
if __name__=="__main__":
    main()