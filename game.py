#!/usr/bin/python3

########################################################################
#
# Name:     Justin Calhoun
# Desc:     Left Center Right
#           This is a fully-automated game of Left Center Right.
#
########################################################################

# Imports here
from random import randint
from lcr_player import Player

#--Main Function--
def main():
    # Empty list of names
    playernames = []
    # Empty list of players
    players = []

    # Get all player names
    with open('playernames.txt', 'r') as f:
        for line in f:
            playernames.append(line.strip())

    # How many players?
    while True:
        numplayers = input('How many players (1-{})? '.format(len(playernames)))
        try:
            numplayers = int(numplayers)
            if numplayers in range(1,len(playernames)+1):
                break
        except ValueError:
            continue

    # Remove names down to the number of players selected
    while len(playernames) > numplayers:
        upper = randint(0,len(playernames)-1)
        playernames.pop(randint(0,upper))

    # Build players list
    index = 0
    for name in playernames:
        players.append({'Index' : index, 'Player' : Player(name)})
        index += 1


    # Start the game!
    game = True
    rounds = 0
    turns = 0
    while game:
        # Each player takes their turn
        rounds += 1
        print('\n### Round {}!'.format(rounds))
        for player in players:
            # Roll the dice
            turns += 1
            dice = player['Player'].Roll()
            if dice:
                print('\n{0} rolls {1}!'.format(player['Player'].Name, dice))
                # Something was returned, do things
                # For each die
                for die in dice:
                    # If they still have a token
                    if player['Player'].Tokens > 0:
                        if die == 'Left':
                            # Get the player to the left
                            leftplayer = (player['Index'] - 1) % numplayers
                            # Give them a token
                            players[leftplayer]['Player'].AddToken()
                            player['Player'].RemoveToken()
                            print('{0} gave a token to {1} on the left.'.format(
                                player['Player'].Name,
                                players[leftplayer]['Player'].Name))
                        elif die == 'Right':
                            # Get the player to the right
                            rightplayer = (player['Index'] + 1) % numplayers
                            # Give them a token
                            players[rightplayer]['Player'].AddToken()
                            player['Player'].RemoveToken()
                            print('{0} gave a token to {1} on the right.'.format(
                                player['Player'].Name,
                                players[rightplayer]['Player'].Name))
                        elif die == 'Center':
                            # Throw a token away
                            player['Player'].RemoveToken()
                            print('{0} threw a token to the center.'.format(
                                player['Player'].Name))
                # Turn is over, print status
                print('{0} now has {1} tokens!'.format(
                    player['Player'].Name,
                    player['Player'].Tokens))
            else:
                print('\n{0} has no tokens, skipping!'.format(player['Player'].Name))

            # Check the score
            score = []
            for player in players:
                if player['Player'].Tokens > 0:
                    score.append(player['Player'].Name)
            if len(score) == 1:
                # Someone has won
                print('\n{0} is the only player with tokens left, '
                      'and has won!'.format(score[0]))
                print('\nThis game took {0} rounds, {1} turns!'.format(
                    rounds,
                    turns))
                game = False
                break



# Run main function
if __name__ == '__main__':
    main()
