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

#palette
white = (255,255,255)

#asset import
yellow_spaceship_raw = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
yellow_spaceship = pygame.transform.scale(yellow_spaceship_raw,relative((500,413),(10,10)))
red_spaceship_raw = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
space_raw = pygame.image.load(os.path.join('Assets','space.png'))

#pygane init
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Malware")

def main():
    clock =pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        pygame.event.pump()
        event = pygame.event.wait()
        if event.type == QUIT:
            run = False
        draw_window()
        
def draw_window():
    screen.blit(space_raw,(0,0))
    screen.blit(yellow_spaceship,relative((width,height),(25,25)))
    pygame.display.update()


# def transform(raw,x,y,r):


if __name__=="__main__":
    main()