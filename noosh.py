#noosh.py
"""noosh.py
This file is the main program for a noosh game.

A noosh game consists of 5 dice and several players(the more the better)
You need 500 points to get on the board
You win at 10000 points.
1 one =100
1 five = 50
3x %d=100*%d
5x one=10000-your_points
3x %d and 2x %d2 = 1200

once everyone is on the board, you can build off of others.

a 'noosh' is when you roll and you don't get any of the above
"""
from functions import determine_conditions,find_amt,find_dice_freq
from functions import find_full_house,process_roll,roll,test_roll
import random,sys
from player import Player
from game import Game



j=Player('Joshua')
game=Game(5)
game.get_players(['j','m','r','b','c'])
game2=Game(26)
game2.get_players(['q','w','e','r','t','y','u','i','o','p','a',
                  's','d','f','g','h','j','k','l','z','x','c',
                  'v','b','n','m'])
##game.round()
##for i in range(20):
##	print(determine_contitions(roll()))
##game.game()
##
game2.game(True)
