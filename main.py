from Controller import *
from Model import *
from View import *
import random

def main():
    Mine = Controller.readDeck("FruitsDeck")
    Mine.shuffle()
    Your = Controller.readDeck("VegetablesDeck")
    Your.shuffle()
    MyField = Field()
    YourField = Field()
    MyHand = Hand([])
    YourHand = Hand([])
    Me = Player(input("Say my name: "),MyField,Mine,MyHand)
    You = Player("Enemy",YourField,Your,YourHand)
    match = Match(Me,You,random.choice([False,True]))
    match.begin()

if __name__ == "__main__":
    main()