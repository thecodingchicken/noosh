import random,sys
from errors import *
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
amt=3
def find_full_house(dice_freq):
    foo=find_amt(dice_freq,3)
    if foo!=False:
        #we have three that are the same, let's check for two
        bar=find_amt(dice_freq,2)
        if bar!=False:
            return True
    return False
def nooshed(roll):
    dice_freq=find_dice_freq(roll)
    t=0
    if dice_freq[1]==0:
        t+=1
    if dice_freq[5]==0:
        t+=1

    if t==2:return True
def determine_conditions(roll,simulation=False):
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

def process_roll(player,roll,simulation=False):
    """Given a player object and a roll, process it.  If you can still roll, it
asks you if you want to and rolls the amount that are needed."""
    return determine_conditions(roll,simulation)


for i in range(20):
	n=roll()
	print(n);nooshed(n)
