from classes import *
neutral = 0
lust = 1
love = -1
def main():

    #cardlist
    block = card("defend", 1, neutral, defend,4 , "Block 4 damage")
    firt = card("help", 1,lust, lustdmg, 3, "Deal 3 Lust damage ")
    help = card("flirt", 1,love, lovedmg, 2, "Deal 2 Love damage")
    thoughtfulGift = card("Thoughtful gift",1, love, TG,(3,6), "Deal 3 Love Damage, if enemies Lust hp is higher, deal 6 Love damage") #(love dmg, if<dmg)
    #visualAphrodisiac = card("Visual Aphrodisiac", 1, lust, (1,2), "Deal 1 Lust Damage, Lust damage is doubled for 2 turns)
    scheduledMessage = card("Scheduled Message", 1, love,SM,3, "Shuffle one Surprise text into enemies draw pile, when drawn does 3 Love damage")
    #gaslighting = card("Gaslighting", 0, love, GL,1,"Lose 1 max energy per turn. deal 4 love damage per turn" )
    #selfLove = card("Self Love", 1, love, SL,1)
    streak = card("Streak", 1, lust, ST, (1,2)) #tupple (dmg,carddraw)
    #anklePic = card("Ankle Pic", 2, lust, AP,2)
    #blockDM = card("Block DM", 3, lust, BDM,1)
    wittyComeback = card("Witty Comeback", 1, neutral, WCB, (3,6)) #(lust dmg, love dmg)
    #admittingFault = card("Admitting Fault", 0, neutral, AF, 2)
    drunkText = card("Drunk Text", 1, neutral, DT,(3,6)) #(love dmg, lust dmg)

    #movelist
    move1 = move("pass",10,neutral,skip,1,1)
    #coldShoulder = move("Cold Shoulder", 1,neutral,CS,3,1)
    diggingUpThePast = move("Digging Up The Past", 1, neutral, DUTP,0,1)
    #lastMinPlans = move("Last Minute Plans",2,neutral,LMP,6)
    changeMyMind = move("Change My Mind",1, CMM,0,1)
    #holdThatAgainstYou = move("Hold That Against You",1, neutral, HTAY,0,1)
    k = move("k",3,neutral,K,12,1)

    
    #to edit for balance
    hp = 30
    armour = 0 
    hp1 = 20
    hp2 = 20
    energy = 3 
    handsize = 4
    buffs = []
    cards = []
    deck = []
    discard= []
    moves = [move1]
    global you, baddie1
    you = player(hp,armour,energy,handsize,cards,buffs,deck,discard)
    baddie1 = enemy(hp1,hp2,energy,moves)
    turncounter = 0
    yourturn= 1


    print("Hello world")
    print("instructions and flavourtext go here")
    print()
    print()
    while True:
        print("---------------------------------------")
        turncounter += 1
        print("turn",turncounter)
        while yourturn:
            print()
            print()
            print("Baddie   hp1:", baddie1.hp1, "     hp2:",baddie1.hp2)
            print("You       hp:",you.hp," energy:",you.energy,"  armour:",you.armour )
            print("cards:", you.cards)
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
    baddie1.hp1 -= x

def lovedmg(x):
    baddie1.hp2 -= x

def TG(x):
    if baddie1.hp2<baddie1.hp1:
        baddie1.hp2 -=x[0]

    else:
        baddie1.hp2 -=x[1]

def SM(x):
    SM = move("Scheduled Message", 0, SME(x), 1)
    baddie1.moves.append(SM)

def GL(x):
    return

def SL(x):
    for i in you.discard:
        if i.name == "Self Love":
            you.discard.remove(i)
    return

def ST(x):
    lustdmg(x[0])
    for i in range(x[1]):
        you.draw()

def AP(x):
    return

def WCB(x):
    if you.prevhp>you.hp:
        lovedmg(x[1])
    else:
        lustdmg(x[0])
def AF(x):
    return

def DT(x):
    if you.maxhp/2 >= you.hp:
        lovedmg(x[0])
    else:
        lustdmg(x[1])


#move effects
def skip():
    pass
def sanitydmg(x):
    you.hp-=x
def SME(x):
    baddie1.hp2 -= x
    baddie1.moves.remove(SM)

def CS(x):
    sanitydmg(x)

def DUTP(x):
    temp = baddie1.prevhp1 - baddie1.hp1
    sanitydmg(temp)

def LMP(x):
    sanitydmg(x)

def CMM(x):
    baddie1.hp1,baddie1.hp2 = baddie1.hp2,baddie1.hp1

def HTAY(x):
    return

def K(x):
    sanitydmg(x)




if __name__ == "__main__":
    main()