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
import random,sys
class NotProperAmountOfDice(Exception):pass
class GameInitError(Exception):pass
class OutOfRange(Exception):pass
def roll(total=5):
    """roll(total=5)
    For many of your turns, you will roll 5, the default.
    You can set some aside, and roll the rest.  That is why
    you can do less than 5.  It returns a tuple.

    This function does no processing whatsoever,
    and just uses random.randint"""
##    random.seed(42)#for testing
    if total<=0:
        raise NotProperAmountOfDice("Less than zero")
    elif total>5:
        raise NotProperAmountOfDice("More than five")
    else:
        foo=[]
        for i in range(total):
            foo.append(random.randint(1,6))
        t=tuple(foo)
    return t
def find_dice_freq(roll):
    d={1:0,2:0,3:0,4:0,5:0,6:0}
    for i in roll:
        if i not in range(1,7):
            raise OutOfRange(1,7)
        else:
            d[i]+=1
    return d
def find_amt(dice_freq,amt):
    """Find amt of a number.  """
    dice_keys=list(dice_freq.keys())
    dice_values=list(dice_freq.values())
    if amt not in dice_values:return False
    for i in range(len(dice_values)):
        if dice_values[i]==amt:
            break
    return dice_keys[i],dice_values[i]
def find_full_house(dice_freq):
    foo=find_amt(dice_freq,3)
    if foo!=False:
        #we have three that are the same, let's check for two
        bar=find_amt(dice_freq,2)
        if bar!=False:
            return True
    return False
def determine_conditions(roll):
    """count how much each number appears.
    A full house is 3 of one, and 2 of another.
    A straight is 1 of each from 1-5 or 2-6
    A 3x of a number is number*100
    After that, just count points
    PROCESS IN THIS ORDER,SO YOU WILL GET HIGHER POINTS"""
    point_values={1:100,5:50,2:0,3:0,4:0,6:0}#one and five are the only
    #ones that get you points
##    print(roll)#testing
    dice_freq=find_dice_freq(roll)
    full_house=find_full_house(dice_freq)
    n=find_amt(dice_freq,3)
    if full_house==True:
        print("You got a full house!")
        return 1200
    elif n!=False:
        print("You got three-of-a-kind!")
        print("The number was %d"%n[0])
        if n[0]>1:
            return n[0]*100
        elif n[0]==1:return 1000
    else:
        #You must not have gotten anything special
        score=0
        for i in roll:
            score+=point_values[i]
        return score
def test_roll():
    """test the roll function to see how random it is."""
    a=[]
    i=0
    c=roll(5)
    while c not in a:
        a.append(c)
        i+=1;c=roll(5)
        if i%10==0:print(i)
    print(i)
def process_roll(player,roll):
    """Given a player object and a roll, process it.  If you can still roll, it
asks you if you want to and rolls the amount that are needed."""
    return determine_conditions(roll)
class Player():
    def __init__(self,name):
        self._name=name
        self._score=0
        self.__can__=False
        self.can_roll=True
    def roll(self):
        print("\n\t\tRolling for {}\n".format(self._name))
        this_turn=roll()
        print("You got %d, %d, %d, %d, %d"%this_turn)
        score=process_roll(self,this_turn)
        if self.get_score()==0:
            if score>500:
                self._score+=score
            else:
                print("Get at least 500 to get on the board")
        else:
            self._score+=score
            if self.__can__==True:
                self.can_roll=False
    def get_score(self):
        return self._score
    def get_name(self):
        return self._name
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
              players in range(2,11)):self.player_cnt=players
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
    def round(self):
        if len(self.players)==0:
            print("Get the player names before playing")
            self.get_players()
        for p in range(len(self.players)):
            self.players[p].roll()
            if self.players[p].get_score()>10000:
                print("%s has a score of 10,000\nYou won")
                sys.exit()#PUT STUFF FOR ONE_LAST_ROUND HERE
        print("\n\n********************SCORES********************")
        for p in self.players:
            print(" %10s:%15d"%(p._name,p.get_score()))
    def game(self):
        while True:
            self.round()
j=Player('Joshua')
game=Game(5)
game.get_players(['j','m','r','b','c'])
##game.round()
##for i in range(20):
##	print(determine_contitions(roll()))
game.game()
