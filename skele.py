from classes import *
neutral = 0
lust = 1
love = -1
def main():
    #to edit for balance
    hp = 300
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
    global you, baddie1
    you = player(hp,armour,energy,handsize,cards,buffs,boostvalue,deck,discard)
    baddie1 = enemy(hp1,hp2,energy,moves,strengthvalue,buffs)
    
    turncounter = 0
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
    block = card("defend", 1, neutral, defend,4 , "Block 4 damage")
    flirt = card("flirt", 1,lust, lustdmg, 3, "Deal 3 Lust damage ")
    help = card("help", 1,love, lovedmg, 2, "Deal 2 Love damage")
    thoughtfulGift = card("Thoughtful gift",1, love, TG,(3,6), "Deal 3 Love Damage, if enemies Lust hp is higher, deal 6 Love damage instead") #(love dmg, if<dmg)
    visualAphrodisiac = card("Visual Aphrodisiac", 1, lust,VA, (1,VAbuff), "Deal 1 Lust Damage, Lust damage is doubled for 2 turns")
    scheduledMessage = card("Scheduled Message", 1, love,SM,3, "Shuffle one Surprise text into enemies draw pile, when drawn does 3 Love damage")
    gaslighting = card("Gaslighting", 2, love, GL,(1,GLBuff),"Lose 1 max energy per turn. deal 4 love damage per turn" )
    selfLove = card("Self Love", 1, love, SL,(1,SLbuff), "Everytime you take damage draw a card")
    streak = card("Streak", 1, lust, ST, (1,2),"Deal 1 Lust damage draw 2 cards")
    anklePic = card("Ankle Pic", 2, lust, AP,APbuff,"Deal 2 more Lust damage for the rest of combat")
    blockDM = card("Block DM", 3, lust, BDM,BDMbuff,"Become Invulnerable and unable to deal Love damage for one turn")
    wittyComeback = card("Witty Comeback", 1, neutral, WCB, (3,6),"Deal 3 lust damage, if you took sanity damage last turn deal 6 love damage instead") #(lust dmg, love dmg)
    admittingFault = card("Admitting Fault", 0, neutral, AF,(2,AFbuff),"Deal 2.5x damage. die next turn")
    drunkText = card("Drunk Text", 1, neutral, DT,(3,6),"Deal 3 Love damage, if you are below half sanity, deal 6 lust damage instead") #(love dmg, lust dmg)
    #movelist
    attack = move("Attack",1,neutral,sanitydmg,4,"Deals 4 sanity damage",2)
    coldShoulder = move("Cold Shoulder", 1,neutral,CS,(3,CSbuff),"Deal 3 Sanity damage, take halved lust damage and double love damage for one turn",1)
    diggingUpThePast = move("Digging Up The Past", 1, neutral, DUTP,0,"Reflect Lust Damage back at player",1)
    lastMinPlans = move("Last Minute Plans",2,neutral,LMP,(6,LMPbuff),"Deal 6 Sanity Damage, player draws one less card next turn",1)
    changeMyMind = move("Change My Mind",1, neutral,CMM,0,"Swap Lust and Love HP",1)
    holdThatAgainstYou = move("Hold That Against You",1, neutral, HTAY,HTAYbuff,"Every time you play a card take 1 unblockable damage",1)
    showingFriendsText = move("Show Friends Your Text",2,neutral,SYF,([4,1],SYFbuff),"permernantly raises sanity damage by 4",1)
    lovelanguage = move("Love Language",1, neutral,Love,Lbuff,"permernantly raises sanity damage by 1 for every love attack played during your next turn",1)
    k = move("k",3,neutral,K,12,"Deal 12 damage",1)

    you.deck = [block,block,block,block,filrt]
    baddie1.moves = [holdThatAgainstYou]
    baddie1.updateweight()
    random.shuffle(you.deck)
    you.newturn()


    print("Hello world")
    print("instructions and flavourtext go here")
    print()
    print()
    
    while True:
        print("---------------------------------------")
        turncounter += 1
        print("turn",turncounter)
        if baddie1.hp1 <=0 or baddie1.hp2 <= 0:
            print("you win!")
            return
        if you.hp<=0:
            print("you lose!")
            return
        while yourturn:
            print()
            print()
            print("Baddie   lust:", baddie1.hp1, "     love:",baddie1.hp2)
            print("You       hp:",you.hp," energy:",you.energy,"  armour:",you.armour )
            print("cards:", you.cards)
            print("Buffs:",you.buffs)
            print(baddie1.moves)
            done = False
            while not done:
                x = input("what do? ")
                result = you.play(x)
                if (result == 2):
                    yourturn = False
                if (result>0):
                    done = True

            print()
            print()
            if baddie1.hp1 <=0 or baddie1.hp2 <= 0:
                print("you win!")
                return
            if you.hp<=0:
                print("you lose!")
                return
        you.prevhp = you.hp
        baddie1.energy =3 - min(0,you.energy)
        while not yourturn:
            print()
            print()
            print("Baddie   lust:", baddie1.hp1, "     love:",baddie1.hp2)
            print("You       hp:",you.hp," energy:",you.energy,"  armour:",you.armour )
            print("cards:", you.cards)
            print("Buffs:",you.buffs)
            print(baddie1.moves)
            result = baddie1.play()
            if (result == 2):
                yourturn = True
                you.newturn()
        you.energy -= min(0,baddie1.energy)
        baddie1.prevhp1 = baddie1.hp1
        baddie1.prevhp2 = baddie1.hp2
                

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
    SMmove = move("Scheduled Message", 0,neutral, SME,(x),"bomb", 1)
    baddie1.moves.append(SMmove)
    baddie1.updateweight()

def GL(x):
    print(you.discard)
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

def energy(x):
    x[0].energy += x[1]

def discarddmg(x):
    you.hp -= x * len(you.discard)

def bdm(*x):
    you.bdm=1 


# helper effects
def skip(*args):
    pass

if __name__ == "__main__":
    main()