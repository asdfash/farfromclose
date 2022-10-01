from classes import *

def main():

    #cardlist
    card0 = card("defend", 0, defend,4)
    card1 = card("help",1,damage1,2)
    card2 = card("flirt",1,damage2,3)

    #movelist
    move1 = move("pass",10,skip,1)
    
    #to edit for balance
    hp = 30
    armour = 0 
    hp1 = 20
    hp2 = 20
    energy = 3 
    handsize = 4
    buffs = []
    cards = []
    deck = [card0,card0,card1,card1,card1,card2]
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
        baddie1.energy =3 - min(0,you.energy)
        while not yourturn:
            
            result = baddie1.play()
            if (result == 2):
                yourturn = True
                you.newturn()
        you.energy -= min(0,baddie1.energy)
                

#card effects

def defend(x):
    you.armour += x
    
def damage1(x):
    baddie1.hp1 -= x

def damage2(x):
    baddie1.hp2 -= x


#move effects
def skip():
    pass

if __name__ == "__main__":
    main()