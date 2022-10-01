from bisect import bisect_left
import random

class player():
    def __init__(self,hp:int,armour:int,energy:int,handsize:int,cards:list,buffs:list,deck:list,discard:list):
        self.hp = hp
        self.maxhp = hp
        self.armour = armour
        self.energy = energy
        self.baseenergy =energy
        self.handsize = handsize
        self.buffs = buffs
        self.cards = cards
        self.deck = deck
        self.discard = discard
        random.shuffle(self.deck)
        self.newturn()
        self.prevhp = hp

    def draw(self):
        if len(self.deck) > 0:
            self.cards.append(self.deck.pop())
        elif len(self.discard) > 0:
            self.deck = self.discard[::]
            self.discard = []
            random.shuffle(self.deck)
            self.cards.append(self.deck.pop())
        else:
            raise("tried to draw, ran out of cards!")
    
    def play(self,istr:str):
        if istr == "end turn":
            return 2
        elif istr.isnumeric():
            i = int(istr)
            if i>=0 and i < len(self.cards):
                card = self.cards[i]
                self.cards.remove(card)
                self.discard.append(card)
                self.energy -= card.activate()
                if self.energy <= 0 or len(self.cards)<=0:
                    return 2
                return 1
        print("error card cannot be played")
        return 0

    def newturn(self,extraenergy=0):
        self.armour = 0
        while self.handsize>len(self.cards) and (len(self.deck)>0 or len(self.discard)>0):
            self.draw()
        for i in self.buffs:
            delete = i.activate()
            if delete:
                self.buffs.remove(i)
        self.energy = self.baseenergy + extraenergy

class card():
    def __init__(self,name,cost,type,effect,args,description):
        self.name = name
        self.type = type
        self.cost = cost
        self.effect = effect
        self.args = args
        self.description = description

    def activate(self):
        self.effect(self.args)
        return self.cost
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()
    

class buff():
    def __init__(self,name,duration,effect):
        self.name = name
        self.duration = duration
        self.effect = effect

    def activate(self):
        self.duration -= 1
        self.effect()
        if self.duration <= 0:
            return 1
        return 0

class enemy():
    def __init__(self,hp1:int,hp2:int,energy:int,moves:list):
        self.hp1 = hp1
        self.hp2 = hp2
        self.energy = energy
        self.moves = moves
        self.weightsum = 0
        self.weights = []
        self.updateweight()
        self.prevhp1 = hp1
        self.prevhp2 = hp2
            
    def updateweight(self):
        self.weightsum = 0
        self.weights = []
        for i in self.moves:
            w = i.weight
            self.weightsum += w
            self.weights.append(self.weightsum)

    def play(self):
        randomizer = random.random() * self.weightsum
        index = bisect_left(self.weights, randomizer)
        action = self.moves[index]
        print("baddie played",action.name)
        self.energy -= action.activate()
        if self.energy <= 0:
            return 2
        return 1

class move(card):
    def __init__(self,name,cost,type,effect,args,description,weight):
        super.__init__(name,cost,type,effect,args,description)
        self.weight = weight #chance to be used
