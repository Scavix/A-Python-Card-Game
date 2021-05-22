from Controller import MyIO
from Model import *
import random

Mine = MyIO.readDeck("FruitsDeck")
Mine.shuffle()
Your = MyIO.readDeck("VegetablesDeck")
Your.shuffle()
MyField = Field()
YourField = Field()
MyHand = Hand([])
YourHand = Hand([])
Me = Player(input("Say my name: "),MyField,Mine,MyHand)
You = Player("Enemy",YourField,Your,YourHand)
match = Match(Me,You,random.choice([False,True]))
match.begin()