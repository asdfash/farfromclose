
from turtle import st
import pygame
import os
from pygame.locals import *
from classes import *


neutral = 0
lust = 1
love = -1

                

#card effects
#hp1 is lust hp
#hp2 is love hp

def defend(x):
    you.armour += x

def lustdmg(x):
    baddie1.hp1 -= int((x + you.boost[0])*you.boost[1])

def lovedmg(x):
    baddie1.hp2 -= int((x + you.boost[2])*you.boost[3]*you.bdm)

def TG(x):
    if baddie1.hp2<=baddie1.hp1:
        lovedmg(x[0])

    else:
        lovedmg(x[1])

def SM(x):
    global SMmove
    SMmove = move("Scheduled Message", 1,neutral, SME,(x),"bomb", 1)
    baddie1.moves.append(SMmove)
    baddie1.updateweight()

def GL(x):
    for i in you.discard:
        if i.name == "Gaslighting":
            you.discard.remove(i)
    you.energy -=x[0]
    you.buffs.append(x[1])

def SL(x):
    for i in you.discard:
        if i.name == "Self Love":
            you.discard.remove(i)
    you.selflove += x[0]
    you.buffs.append(x[1])

def ST(x):
    lustdmg(x[0])
    for i in range(x[1]):
        you.draw()

def AP(x):
    for i in you.discard:
        if i.name == "Ankle Pic":
            you.discard.remove(i)
    boost([2,1,0,1])
    you.buffs.append(x)

def WCB(x):
    if you.prevhp>you.hp:
        lovedmg(x[1])
    else:
        lustdmg(x[0])
def AF(x):
    boost([0,2.5,0,2.5])
    you.buffs.append(x[1])

def DT(x):
    if you.maxhp/2 <= you.hp:
        lovedmg(x[0])
    else:
        lustdmg(x[1])

def VA(x):
    lustdmg(x[0])
    for i in you.buffs:
        if i.name == "aroused":
            i.duration += 2
            return
    you.buffs.append(x[1])

    boost([0,1.5,0,1])

def BDM(x):
    you.buffs.append(x)
    you.bdm =0

#move effects


def sanitydmg(x):
    damage =  int((x + baddie1.strength[0])*baddie1.strength[1]*you.bdm)
    if you.armour >= damage:
        you.armour -= damage
    else:
        damage -= you.armour
        you.armour =0
        you.hp -= damage
        if you.selflove > 0 :
            you.temp += you.selflove

def SME(x):
    lovedmg(x)
    baddie1.moves.remove(SMmove)
    baddie1.updateweight()

def CS(x):
    sanitydmg(x[0])
    for i in you.buffs:
        if i.name == "ignored":
            i.duration += 1
            return
    boost([0,0.5,0,2])
    you.buffs.append(x[1])




def DUTP(x):
    temp = baddie1.prevhp1 - baddie1.hp1
    sanitydmg(temp)

def LMP(x):
    sanitydmg(x[0])
    you.temp-=1


def CMM(x):
    baddie1.hp1,baddie1.hp2 = baddie1.hp2,baddie1.hp1
    for i in baddie1.moves:
        if i.name == "Change My Mind":
            baddie1.moves.remove(i)
    baddie1.updateweight()
def HTAY(x):
    you.htay += 1
    you.buffs.append(x)

def K(x):
    sanitydmg(x)

def Love(x):
    for i in you.buffs:
        if i.name == "loved":
            i.duration += 1
            return
    you.buffs.append(x)

def SYF(x):
    strength(x[0])
    you.buffs.append(x[1])



#buffs aeffects/deffects

def boost(x):
    you.boost[0] += x[0]
    you.boost[1] *= x[1]
    you.boost[2] += x[2]
    you.boost[3] *= x[3]

def strength(x):
    baddie1.strength[0] += x[0]
    baddie1.strength[1] *= x[1]

def die(*args):
    you.hp = -99999

def carddraw(x):
    for i in range(x):
        you.draw()

def discarddmg(x):
    you.hp -= x * len(you.discard)

def bdm(*x):
    you.bdm=1 


# helper effects
def skip(*args):
    pass








# aaaaa



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
textareadown = (300,645,600,75)
textareaup = (300,60,670,145)
endturnsize = (80,75)
endturndx = 900
endturndown = 645
endturnup = 200
messagelistmax = 6
messageoffset = (0,5)

messagelist =[]

#palette
white = (255,255,255)

#global settings
cardview_toggle = False
clickable = []
textbox= pygame.Rect(textareadown)

#asset import
hp_bar_raw = pygame.image.load(os.path.join('Assets','hp bar.png'))
hp_bar = pygame.transform.scale(hp_bar_raw, hpbarscale)
armor_bar = pygame.image.load(os.path.join('Assets','armor bar.png'))
energy_bar = pygame.image.load(os.path.join('Assets','energy bar.png'))
lust_bar = pygame.image.load(os.path.join('Assets','lust bar.png'))
love_bar = pygame.image.load(os.path.join('Assets','love bar.png'))
messenger = pygame.image.load(os.path.join('Assets','messenger.png'))
cardview = pygame.image.load(os.path.join('Assets','cardview bottom.png'))
bf = pygame.image.load(os.path.join('Assets','bf.png'))
gf = pygame.image.load(os.path.join('Assets','gf.png'))
cardviewtop =pygame.image.load(os.path.join('Assets','cardview top.png'))
bgm =  os.path.join('Assets','loopable.mp3')

#cards/moves
anklepic_asset = pygame.image.load(os.path.join('Assets','cards','ankle pic.png'))
brb_asset = pygame.image.load(os.path.join('Assets','cards','brb.png'))
changemymind_asset = pygame.image.load(os.path.join('Assets','cards','change my mind.png'))
comeback_asset = pygame.image.load(os.path.join('Assets','cards','comeback.png'))
coldshoulder_asset =  pygame.image.load(os.path.join('Assets','cards','cold shoulder.png'))
defend_asset = pygame.image.load(os.path.join('Assets','cards','defend.png'))
dutp_asset =  pygame.image.load(os.path.join('Assets','cards','digging up the past.png'))
drunk_asset = pygame.image.load(os.path.join('Assets','cards','drunk text.png'))
exposed_asset = pygame.image.load(os.path.join('Assets','cards','exposed.png'))
flatter_asset = pygame.image.load(os.path.join('Assets','cards','flatter.png'))
flirt_asset = pygame.image.load(os.path.join('Assets','cards','flirt.png'))
gaslight_asset = pygame.image.load(os.path.join('Assets','cards','gaslight.png'))
gift_asset = pygame.image.load(os.path.join('Assets','cards','gift.png'))
htay_asset = pygame.image.load(os.path.join('Assets','cards','hold that against you.png'))
k_asset = pygame.image.load(os.path.join('Assets','cards','k.png'))
lasminplans_asset = pygame.image.load(os.path.join('Assets','cards','last min plans.png'))
lovelanguage_asset = pygame.image.load(os.path.join('Assets','cards','love language.png'))
roast_asset = pygame.image.load(os.path.join('Assets','cards','roast.png'))
scheduledmessage_asset = pygame.image.load(os.path.join('Assets','cards','scheduled message.png'))
selflove_asset = pygame.image.load(os.path.join('Assets','cards','self love.png'))
selfie_asset = pygame.image.load(os.path.join('Assets','cards','selfie.png'))
tease_asset = pygame.image.load(os.path.join('Assets','cards','tease.png'))
yesmyfault_asset = pygame.image.load(os.path.join('Assets','cards','yes my fault.png'))

#moves


cardhitboxlist = [pygame.Rect((330 + (i%3) * (cardoffsetx+cardsizex)),(280 + (i//3) * (cardoffsety+cardsizey)),cardsizex,cardsizey) for i in range(9)]
endturnhitbox = pygame.Rect(endturndx,endturndown,endturnsize[0],endturnsize[1])



#pygane init
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(gamename)

def main2():
    hp = 30
    armour = 0 
    hp1 = 20
    hp2 = 20
    energy = 3 
    handsize = 5
    buffs = []
    cards = []
    deck = []
    discard= []
    boostvalue=[0,1,0,1]
    strengthvalue = [0,1]
    moves = []
    global you, baddie1,yourturn
    you = player(hp,armour,energy,handsize,cards,buffs,boostvalue,deck,discard)
    baddie1 = enemy(hp1,hp2,energy,moves,strengthvalue,buffs)

    yourturn= 1

    #bufflist
    VAbuff = buff("aroused",2,[1,0],skip,boost,[0,2/3,0,1])
    GLBuff = buff("gaslit",-1,[1,0],lovedmg,skip,4)
    BDMbuff= buff("DM's blocked",1,[1,0],skip,bdm,0)
    AFbuff = buff("Death sentenced",1,[1,0],skip,die,0)
    CSbuff = buff("ignored",2,[1,0],skip,boost,[0,2,0,0.5])
    LMPbuff = buff("busy",1,[1,0],skip,skip,1)
    SLbuff = buff("Empowered",-1,[0,0],skip,skip,0)
    Lbuff = buff("loved",2,[0,1],strength,skip,[1,1])
    APbuff = buff("Smexy",-1,[0,0],skip,skip,0)
    SYFbuff = buff("Embarassed",-1,[0,0],skip,skip,0)
    HTAYbuff = buff("Pressured",-1,[0,0],skip,skip,0)

    #cardlist
    block = card("defend", 1, neutral, defend,4 , defend_asset)
    flirt = card("flirt", 1,lust, lustdmg, 3, flirt_asset)
    help = card("help", 1,love, lovedmg, 2, flatter_asset)
    thoughtfulGift = card("Thoughtful gift",1, love, TG,(3,6),gift_asset) #(love dmg, if<dmg)
    visualAphrodisiac = card("Visual Aphrodisiac", 1, lust,VA, (3,VAbuff), selfie_asset)
    scheduledMessage = card("Scheduled Message", 1, love,SM,3, scheduledmessage_asset)
    gaslighting = card("Gaslighting", 2, love, GL,(1,GLBuff),gaslight_asset )
    selfLove = card("Self Love", 1, love, SL,(1,SLbuff), selflove_asset)
    streak = card("Streak", 1, lust, ST, (3,2),tease_asset)
    anklePic = card("Ankle Pic", 2, lust, AP,APbuff,anklepic_asset)
    blockDM = card("Block DM", 3, lust, BDM,BDMbuff,brb_asset)
    wittyComeback = card("Witty Comeback", 1, neutral, WCB, (3,6),comeback_asset) #(lust dmg, love dmg)
    admittingFault = card("Admitting Fault", 0, neutral, AF,(2,AFbuff),yesmyfault_asset)
    drunkText = card("Drunk Text", 1, neutral, DT,(3,6),drunk_asset) #(love dmg, lust dmg)
    
    #movelist
    attack = move("Attack",1,neutral,sanitydmg,4,roast_asset,2)
    coldShoulder = move("Cold Shoulder", 1,neutral,CS,(3,CSbuff),coldshoulder_asset,1)
    diggingUpThePast = move("Digging Up The Past", 1, neutral, DUTP,0,dutp_asset,1)
    lastMinPlans = move("Last Minute Plans",2,neutral,LMP,(6,LMPbuff),lasminplans_asset,1)
    changeMyMind = move("Change My Mind",1, neutral,CMM,0,changemymind_asset,1)
    holdThatAgainstYou = move("Hold That Against You",1, neutral, HTAY,HTAYbuff,htay_asset,1)
    showingFriendsText = move("Show Friends Your Text",2,neutral,SYF,([4,1],SYFbuff),exposed_asset,1)
    lovelanguage = move("Love Language",1, neutral,Love,Lbuff,lovelanguage_asset,1)
    k = move("k",3,neutral,K,12,"Deal 12 damage",1)

    you.deck = [block,block,block,block, flirt,flirt,help,help,anklePic,visualAphrodisiac,streak,selfLove,drunkText,\
                thoughtfulGift,scheduledMessage,gaslighting,blockDM,wittyComeback,admittingFault]
    baddie1.moves = [attack,coldShoulder,diggingUpThePast,lastMinPlans,changeMyMind,holdThatAgainstYou,\
                     showingFriendsText,lovelanguage,k]
    baddie1.updateweight()
    random.shuffle(you.deck)
    you.newturn()
    

    pygame.mixer.music.load(bgm)
    pygame.mixer.music.play(-1)
    lclick = False
    drag = False
    dragl = [0,0]
    clock =pygame.time.Clock()
    run = True
    while run:
        x=-1
        if baddie1.hp1 <=0 or baddie1.hp2 <= 0:
            print("you win!")
            return
        if you.hp<=0:
            print("you lose!")
            return
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
                    lclick=True

            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if drag:
                        print("cancelled")
                    if not drag:
                        x=exceute((mx,my))
                    lclick = False
                    dragl = [0,0]
                    drag = False

        if lclick:
            dragl = [mx-omx,my-omy]
            if abs(dragl[0]) > dragt[0] and abs(dragl[1]) > dragt[1]:
                drag = True
        msg = main(x)
        messagehandler(msg) 
        draw_window()


def main(x):
    global yourturn
    if yourturn and x!= -1:
        result,msg = you.play(x)
        if (result == 2):
            yourturn = False
        if (result>0):
            you.prevhp = you.hp
            baddie1.energy =3 - min(0,you.energy)
    elif not yourturn:
        result,msg = baddie1.play()
        if (result == 2):
            yourturn = True
            you.newturn()
            you.energy -= min(0,baddie1.energy)
            baddie1.prevhp1 = baddie1.hp1
            baddie1.prevhp2 = baddie1.hp2
    else:
        msg =""
    return msg
    
        


def messagehandler(msg=""):
    if type(msg)!= str:
        global messagelist
        if len(messagelist)>=messagelistmax:
            messagelist.pop()
        messagelist = [msg] + messagelist

        
def draw_window():
    screen.blit(bf,(0,0))
    screen.blit(gf,(0,0))
    screen.blit(messenger,(0,0))
    
    for i in range(you.hp):
        is_mid =0
        if i%10 >= 5:
            is_mid = 1
        x = 1040 + (i%10) * (baroffsetx+hpbarscale[0])+ midoffsetx*is_mid
        y = 555 + (i//10) * (baroffsety+hpbarscale[1])
        screen.blit(hp_bar,(x,y))

    for i in range(you.armour):
        x = 1110 + (i%5) * (baroffsetx+barsizex)
        y = 670 + (i//5) * (baroffsety+barsizey)
        screen.blit(armor_bar,(x,y))
    
    for i in range(you.energy):
        x = 1110 + (i%5) * (baroffsetx+barsizex)
        y = 620 + (i//5) * (baroffsety+barsizey)
        screen.blit(energy_bar,(x,y))

    for i in range(baddie1.hp1):
        is_mid =0
        if i%10 >= 5:
            is_mid = 1
        x = 100 + (i%10) * (baroffsetx+barsizex)+ midoffsetx*is_mid
        y = 575 + (i//10) * (baroffsety+barsizey)
        screen.blit(lust_bar,(x,y))

    for i in range(baddie1.hp2):
        is_mid =0
        if i%10 >= 5:
            is_mid = 1
        x = 100 + (i%10) * (baroffsetx+barsizex)+ midoffsetx*is_mid
        y = 640 + (i//10) * (baroffsety+barsizey)
        screen.blit(love_bar,(x,y))

    for i in range(len(messagelist)):
        x = 110 + (messageoffset[0]+cardsizex)
        y = 500 - i * (messageoffset[1]+cardsizey)
        screen.blit(messagelist[i],(x,y))
        
    if cardview_toggle:
        screen.blit(cardview,(0,0))
        for i in range(len(you.cards)):
            x = 35 + (i%3) * (cardoffsetx+cardsizex)
            y = 280 + (i//3) * (cardoffsety+cardsizey)
            screen.blit(you.cards[i].asset,(x,y))
    screen.blit(cardviewtop,(0,0))
    
    pygame.display.update()

def is_over(rect:Rect, pos):
    return rect.collidepoint(pos[0], pos[1])

def exceute(pos):
    x = -1
    if cardview_toggle:
        for i in range(len(cardhitboxlist)):
            if is_over(cardhitboxlist[i],pos):
                x=i
    if is_over(endturnhitbox, pos):
        x = 10
    if is_over(textbox,pos):
        toggle_cards()
    return x

def toggle_cards():
    global textbox,cardview_toggle
    cardview_toggle = not cardview_toggle
    if textbox.y == textareaup[1]:  #down
        textbox.y = textareadown[1]
        textbox.size = (textareadown[2],textareadown[3])
        endturnhitbox.y = endturndown

    else:
        textbox.y = textareaup[1] # up
        textbox.size = (textareaup[2],textareaup[3])
        endturnhitbox.y = endturnup
if __name__=="__main__":
    main2()