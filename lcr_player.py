#!/usr/bin/python3
#
# lcr_player.py - python3 script
#
# Author:	houn
# Desc:     Contains the Player class for the LCR game

# Imports ###################
## random.randint - Random Numbers
from random import randint

# Don't run this alone
if __name__ == '__main__':
    raise Exception('This file is not meant to be run by itself.  Run ' \
                    '"main.py" instead.')

class Player(object):
    """
    Class to simulate each player in the LCR game
    """

    def __init__(self, Name = '', Tokens = 3):
        """
        Initialize a new Player instance
        """

        #Attributes
        self.__Name = Name
        self.__Tokens = Tokens

    #--Properties
    #Name
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Value):
        self.__Name = Value

    #Tokens
    @property
    def Tokens(self):
        return self.__Tokens

    @Tokens.setter
    def Tokens(self, Value):
        self.__Tokens = Value

    #--Methods--
    def Roll(self):
        """
        Roll the dice, if able

        :returns: A list of dice rolls.  Will be empty if there were no
                  tokens, and thus nothing rolled.
        """
        # Define the die
        die = ['Circle', 'Circle', 'Circle', 'Left', 'Right', 'Center' ]
        # Initialize variables
        rolls = []
        dice = 0

        # Never use more than 3 dice
        if self.__Tokens > 3:
            dice = 3
        else:
            dice = self.__Tokens

        # Roll the dice
        for i in range(dice):
            rolls.append(die[randint(0,5)])

        return rolls

    def AddToken(self):
        """
        Add a token
        """
        self.__Tokens += 1

    def RemoveToken(self):
        """
        Remove a token
        """
        self.__Tokens -= 1
