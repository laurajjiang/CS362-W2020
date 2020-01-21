# -*- coding: utf-8 -*-
"""
Created on Sun January 12 16:20:25 2020

@author: jianglau / Laura Jiang
"""

import Dominion
import testUtility

# Get player names, refactored into testUtility
player_names = testUtility.getNames()

# number of curses and victory cards, refactored into testUtility
nV, nC = testUtility.calculate_nVnC(player_names)

# Define box, refactored into testUtility
box = testUtility.makeBox(nV)

# refactored into testUtility
supply_order = testUtility.createSupplyOrder()

# refactored into testUtility
supply = testUtility.createSupply(box, player_names, nC, 0)

# initialize the trash
trash = []
# Construct the Player objects
players = testUtility.createPlayers(player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)


# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc["VICTORY POINTS"]
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = " and ".join(winners) + " win!"
else:
    winstring = " ".join([winners[0], "wins!"])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)
