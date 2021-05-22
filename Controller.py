from Model import Card
from Model import Deck


class MyIO:

    def readDeck(path):
        f = open(path,"r")
        cards = []
        for i in f:
            tmp = Card(i.split(";")[0],int(i.split(";")[1]),int(i.split(";")[2]))
            cards.append(tmp)
        f.close()
        return Deck(path,cards)
