import random

class Card:

    def __init__(self, name, atk, cost):
        self.name = name
        self.atk = atk
        self.cost = cost

    def __str__(self):
        return self.name+", ATK: "+str(self.atk)+", DEF: "+str(self.cost)


class Deck:

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def remove(self,card):
        for i in self.cards:
            if i == card:
                self.cards.remove(card)

    def give(self):
        if len(self.cards) > 0:
            return random.choice(self.cards)

    def draw(self):
        tmp = self.give()
        self.remove(tmp)
        return tmp

    def __str__(self):
        res = "| "+self.name+" | "
        for i in self.cards:
            res = res + str(i) + " | "
        return res


class Field:

    def __init__(self):
        self.slots=[]

    def avaible(self):
        if 3 - len(self.slots) > 0:
            return True
        return False

    def place(self,card):
        self.slots.append(card)

    def remove(self,card):
        self.slots.remove(card)

    def __str__(self):
        arr = []
        for i in self.slots:
            arr.append(str(i))
        return str(arr)


class Hand:
    
    def __init__(self,cards):
        self.cards=cards

    def avaible(self):
        if len(self.cards) > 0:
            return True
        return False

    def draw(self,card):
        self.cards.append(card)

    def discard(self,card):
        self.cards.remove(card)

    def __str__(self):
        arr = []
        for i in self.cards:
            arr.append(str(i))
        return str(arr)


class Player:

    def __init__(self,name,field,deck,hand):
        self.name=name
        self.field=field
        self.deck=deck
        self.hand=hand

    def start(self):
        self.draw(3)
    
    def draw(self):
        self.hand.draw(self.deck.draw())
    
    def draw(self,N):
        for i in range(N):
            self.hand.draw(self.deck.draw())

    def set(self, card):
        if self.field.avaible():
            self.hand.discard(card)
            self.field.place(card)

    def __str__(self):
        tmp1 = []
        tmp2 = []
        for i in self.field.slots:
            tmp1.append(str(i))
        for i in self.hand.cards:
            tmp2.append(str(i))
        return self.name+" | "+ str(tmp1) + " | " + str(tmp2)


#class Match
#2 player, relativi field
#asincrono bloccante
class Match:

    def __init__(self,player1,player2,turn):
        self.player1=player1
        self.player2=player2
        self.turn=turn
        self.counter=1

    def begin(self):
        allowedOp = ["set","atk","end","1","2","3"]
        self.player1.start()
        self.player2.start()
        while True:
            if self.turn:
                tmpN = {}
                for i in range(len(self.player1.hand.cards)):
                    tmpN[i+1]=self.player1.hand.cards[i]
                x=""
                while not x in allowedOp:
                    x = input("[" + str(self.counter) + "] [" + self.player1.name+ "] What do you want to do [1|set][2|atk][3|end]?\n" + str(self.player1.hand) + "\n" + str(self.player1.field) + "\n")
                    if x == "set" or x == "1":
                        if not self.player1.hand.avaible():
                            x=""
                            continue
                        for i in range(len(tmpN)):
                            print(i+1, tmpN[i+1])
                        toSet = int(input("Number: ")) - 1
                        self.player1.set(self.player1.hand.cards[toSet])
                    #elif x == "atk" or x == "2":
                    #elif x == "end" or x == "3":
                self.turn = False
                self.counter = self.counter + 1
            else:
                tmpN = {}
                for i in range(len(self.player2.hand.cards)):
                    tmpN[i+1]=self.player2.hand.cards[i]
                x=""
                while not x in allowedOp:
                    x = input("[" + str(self.counter) + "] [" + self.player2.name+ "] What do you want to do [1|set][2|atk][3|end]?\n" + str(self.player2.hand) + "\n" + str(self.player2.field) + "\n")
                    if x == "set" or x == "1":
                        if not self.player2.hand.avaible():
                            x=""
                            continue
                        for i in range(len(tmpN)):
                            print(i+1, tmpN[i+1])
                        toSet = int(input("Number: ")) - 1
                        self.player2.set(self.player2.hand.cards[toSet])
                    #elif x == "atk" or x == "2":
                    #elif x == "end" or x == "3":
                self.turn = True
                self.counter = self.counter + 1

    def __str__(self):
        return "|"+self.player1.name +"|\n|"+self.player2.name+"|\n|Turn: "+str(self.turn)+"||Time: "+str(self.counter)+"|"