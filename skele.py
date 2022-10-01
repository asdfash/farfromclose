from classes import *
from moveffects import *
from cardeffects import *


#cardlist
card0 = card("defend", 0, defend)

#movelist
move1 = move("pass",4,skip,1)



#to edit for balance
hp = 30
hp1 = 20
hp2 = 20
energy = 3 
handsize = 4
buffs = []
cards = []
deck = [card0]
discard= []
moves = [move1]


you = player(hp,energy,handsize,cards,buffs,deck,discard)
baddie = enemy(hp1,hp2,energy,moves)
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
        print("Baddie   hp1:", baddie.hp1, "     hp2:",baddie.hp2)
        print("You       hp:",you.hp," energy:",you.energy)
        print("cards:", you.cards)
        done = False
        while not done:
            x = input("what do?")
            result = you.play(x)
            if (result == 2):
                yourturn = False
            if (result>0):
                done = True

        print()
        print()
    while not yourturn:
        result = baddie.play()
        if (result == 2):
            yourturn = True
            you.newturn()
