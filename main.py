import classes
import pygame
import os
from pygame.locals import *

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
spaceship_scale = (10,10)
spaceship_scale_abs = relative((500,413),spaceship_scale)
dragt = (50,50)
#palette
white = (255,255,255)

#asset import
red_spaceship_raw = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_raw,spaceship_scale_abs),270)
space_raw = pygame.image.load(os.path.join('Assets','space.png'))

#pygane init
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Malware")

def main():
    rrel= relative((width,height),(75,25))
    r = pygame.Rect(rrel[0],rrel[1],spaceship_scale_abs[0],spaceship_scale_abs[1])
    lclick = False
    drag = False
    dragl = [0,0]
    rpickup = 0
    offset = [0,0]
    
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
                        if is_over(r,(mx,my)):
                            rpickup =1
                            offset = [r.x-mx,r.y-my]

                            
                    lclick = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if drag:
                        print("cancelled")
                    if not drag:
                        exceute()
                    lclick = False
                    dragl = [0,0]
                    drag = False
                    rpickup =0
        if lclick:
            dragl = [mx-omx,my-omy]
            print(dragl)
            if abs(dragl[0]) > dragt[0] and abs(dragl[1]) > dragt[1]:
                drag = True
        if rpickup==1:
            r.x,r.y = mx+offset[0],my+offset[1]

    
        draw_window(r)
        
def draw_window(r:Rect):
    screen.blit(space_raw,(0,0))
    screen.blit(red_spaceship,(r.x,r.y))
    pygame.display.update()

def is_over(rect:Rect, pos):
    return rect.collidepoint(pos[0], pos[1])

# def transform(raw,x,y,r):
#
def exceute():
    pass
    
if __name__=="__main__":
    main()