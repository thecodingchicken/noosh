from functions import determine_conditions,find_amt,find_dice_freq
from functions import find_full_house,process_roll,roll,test_roll
from player import Player
import sys,time
class Game():
    def __init__(self,players=None):
        self.players=[]
        if players==None:
            print("You didn't give the number of players")
            print("Please enter the number of players")
            n='g'
            while type(n)!=int:
                try:n=int(input('Players( a number from 2 to 10):  '))
                except:
                    print("Please give an int")
                else:
                    if n in range(2,11):break
                    else:print("Enter a number from 2 to 10");n='a'
            self.player_cnt=n
        elif (type(players)==int and
              players in range(2,111)):#11
            self.player_cnt=players
        else:
            raise GameInitError("You didn't give a number from 2 to 10")
    def get_players(self,l=[]):
        if len(self.players)==0 and l==[]:
            for i in range(self.player_cnt):
                n=input("Player %2d:  "%int(i+1))
                self.players.append(Player(n))
        elif len(self.players)==0:
            for i in l:
                self.players.append(Player(i))
    def round(self, simulation =False):
        if len(self.players)==0:
            print("Get the player names before playing")
            self.get_players()
        for p in range(len(self.players)):
            self.players[p].roll( simulation )
            if simulation ==False:
                time.sleep(2)
            if self.players[p].get_score()>10000:
                print("%s has a score of 10,000"%self.players[p].get_name())
                print("You won")
                print("\n\n********************SCORES********************")
                for p in self.players:
                    print(" %10s:%15d"%(p._name,p.get_score()))
                sys.exit()#PUT STUFF FOR ONE_LAST_ROUND HERE
        print("\n\n********************SCORES********************")
        for p in self.players:
            print(" %10s:%15d"%(p._name,p.get_score()))
    def game(self,simulation=False):
        while True:
            self.round( simulation )
            if simulation==False:
                a=input("Press enter for another round:  ")
            else:pass
