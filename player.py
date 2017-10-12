from functions import determine_conditions,find_amt,find_dice_freq
from functions import find_full_house,process_roll,roll,test_roll
class Player():
    def __init__(self,name):
        self._name=name
        self._score=0
        self.__can__=False
        self.can_roll=True
    def roll(self, simulation=False):
        print("\n\t\tRolling for {}\n".format(self._name))
        this_turn=roll()
        print("You got %d, %d, %d, %d, %d"%this_turn)
        score=process_roll(self,this_turn,simulation)
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
