import Dominion
import random
from collections import defaultdict

"""
Function: getNames()
Parameters: n/a
Pre-conditions: n/a
Post-Conditions: returns an array/list of strings to be used as the list of players
"""


def getNames():
    return ["Annie", "*Ben", "*Carla"]


"""
Function: makeBox()
Parameters: nV, the number of victory cards
Pre-conditions: nV is a non-negative integers
Post-Conditions: returns box, a dictionary of all Dominion cards
"""


def makeBox(nV):
    box = {}
    box["Woodcutter"] = [Dominion.Woodcutter()] * 10
    box["Smithy"] = [Dominion.Smithy()] * 10
    box["Laboratory"] = [Dominion.Laboratory()] * 10
    box["Village"] = [Dominion.Village()] * 10
    box["Festival"] = [Dominion.Festival()] * 10
    box["Market"] = [Dominion.Market()] * 10
    box["Chancellor"] = [Dominion.Chancellor()] * 10
    box["Workshop"] = [Dominion.Workshop()] * 10
    box["Moneylender"] = [Dominion.Moneylender()] * 10
    box["Chapel"] = [Dominion.Chapel()] * 10
    box["Cellar"] = [Dominion.Cellar()] * 10
    box["Remodel"] = [Dominion.Remodel()] * 10
    box["Adventurer"] = [Dominion.Adventurer()] * 10
    box["Feast"] = [Dominion.Feast()] * 10
    box["Mine"] = [Dominion.Mine()] * 10
    box["Library"] = [Dominion.Library()] * 10
    box["Gardens"] = [Dominion.Gardens()] * nV
    box["Moat"] = [Dominion.Moat()] * 10
    box["Council Room"] = [Dominion.Council_Room()] * 10
    box["Witch"] = [Dominion.Witch()] * 10
    box["Bureaucrat"] = [Dominion.Bureaucrat()] * 10
    box["Militia"] = [Dominion.Militia()] * 10
    box["Spy"] = [Dominion.Spy()] * 10
    box["Thief"] = [Dominion.Thief()] * 10
    box["Throne Room"] = [Dominion.Throne_Room()] * 10
    return box


"""
Function: calculate_nVnC(player_names)
Parameters: 
Pre-conditions: n/a
Post-Conditions: 
"""


def calculate_nVnC(player_names):
    nC = -10 + 10 * len(player_names)
    if len(player_names) > 2:
        return [12, nC]
    else:
        return [8, nC]


"""
Function: createSupplyOrder()
Parameters: n/a
Pre-conditions: n/a
Post-Conditions: returns supply_order, a dictionary of costs associated with each Dominion card
"""


def createSupplyOrder():
    supply_order = {
        0: ["Curse", "Copper"],
        2: ["Estate", "Cellar", "Chapel", "Moat"],
        3: ["Silver", "Chancellor", "Village", "Woodcutter", "Workshop"],
        4: [
            "Gardens",
            "Bureaucrat",
            "Feast",
            "Militia",
            "Moneylender",
            "Remodel",
            "Smithy",
            "Spy",
            "Thief",
            "Throne Room",
        ],
        5: [
            "Duchy",
            "Market",
            "Council Room",
            "Festival",
            "Laboratory",
            "Library",
            "Mine",
            "Witch",
        ],
        6: ["Gold", "Adventurer"],
        8: ["Province"],
    }
    return supply_order


"""
Function: createSupply()
Parameters: box - a dictionary of all possible cards| player-names - a list of strings | nC - number of curses | nV - the number of victory cards
Pre-conditions: box contains at least ten cards, nC and nV are non-negative integers
Post-Conditions: return supply, filled with ten random cards from the box as well as Treasure, victory, and curse cards
"""


def createSupply(box, player_names, nC, nV):

    # Pick 10 cards from box to be in the supply.
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    supply = defaultdict(list, [(k, box[k]) for k in random10])

    # The supply always has these cards
    supply["Copper"] = [Dominion.Copper()] * (60 - len(player_names) * 7)
    supply["Silver"] = [Dominion.Silver()] * 40
    supply["Gold"] = [Dominion.Gold()] * 30
    supply["Estate"] = [Dominion.Estate()] * nV
    supply["Duchy"] = [Dominion.Duchy()] * nV
    supply["Province"] = [Dominion.Province()] * nV
    supply["Curse"] = [Dominion.Curse()] * nC
    return supply


"""
Function: createPlayers()
Parameters: player_names, an array of strtings containing the names of players
Pre-conditions: player_names exists
Post-Conditions: returns a new array of players
"""


def createPlayers(player_names):
    players = []
    for name in player_names:
        if name[0] == "*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0] == "^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players
