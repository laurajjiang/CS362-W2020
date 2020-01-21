from unittest import TestCase
import Dominion
import testUtility

"""
Functions to Test:
i. Action_card Class
    1. initialization
    2. ‘use’ function
    3. ‘augment’ function
ii. Player Class
    1. ‘action_balance’ function
    2. ‘calcpoints’ function
    3. ‘draw’ function
    4. ‘cardsummary’ function
iii. gameOver function
"""


class TestActionCard(TestCase):
    def test_init(self):
        # basic initialization test
        card = Dominion.Action_card("Test", 1, 1, 2, 1, 1)
        self.assertEqual("Test", card.name)
        self.assertEqual(1, card.cost)
        self.assertEqual(1, card.actions)
        self.assertEqual(2, card.cards)
        self.assertEqual(1, card.buys)
        self.assertEqual(1, card.coins)

    def test_use(self):
        # simple use test, expects hand appropriately count number of cards
        player = Dominion.Player("Annie")
        card = Dominion.Action_card("Test", 1, 1, 2, 1, 1)
        player.hand.append(card)
        self.assertEqual(6, len(player.hand))
        card.use(player, [])
        self.assertEqual(1, len(player.played))
        self.assertEqual(5, len(player.hand))

    def test_augment(self):
        # expects the card to have tangible effects on actions, buys, and purse
        player = Dominion.Player("Annie")
        card = Dominion.Action_card("Test", 1, 1, 2, 1, 1)
        player.actions = 1
        player.buys = 1
        player.purse = 1
        card.augment(player)
        self.assertEqual(2, player.actions)
        self.assertEqual(2, player.buys)
        self.assertEqual(2, player.purse)
        self.assertEqual(7, len(player.hand))


class TestPlayer(TestCase):
    def test_balance(self):
        # adds an action card to properly use the action balance functionality
        player = Dominion.Player("Annie")
        player.hand.append(Dominion.Moneylender())
        balance = 0
        self.assertEqual(0, balance)
        balance = player.action_balance()
        self.assertEqual(11, len(player.stack()))
        self.assertEqual(-6, int(balance))

    def test_calcpoints(self):
        # adds additional victory cards, then calculates
        player = Dominion.Player("Annie")
        player.deck.append(Dominion.Province())
        player.deck.append(Dominion.Gardens())
        points = 0
        self.assertEqual(0, points)
        points = player.calcpoints()
        self.assertEqual(10, points)

    def test_draw(self):
        # test base functionality of draw function
        player = Dominion.Player("Annie")
        self.assertEqual(5, len(player.deck))
        player.draw()
        self.assertEqual(6, len(player.hand))
        self.assertEqual(4, len(player.deck))

        # test case where deck is empty
        player.hand = []
        player.deck = []
        player.discard = [Dominion.Copper()] * 7 + [Dominion.Estate()] * 3
        self.assertEqual(10, len(player.discard))
        self.assertEqual(0, len(player.deck))
        c = player.draw()

        # then, player should draw from their shuffled deck
        temp_discard = [Dominion.Copper()] * 7 + [Dominion.Estate()] * 3
        self.assertEqual(len(player.deck), len(temp_discard) - 1)
        self.assertEqual(0, len(player.discard))
        self.assertEqual(True, bool(c))  # check that the card exists

    def test_summary(self):
        # tests for different possible categories and types
        player = Dominion.Player("Annie")
        player.deck.append(Dominion.Gardens())
        summary = player.cardsummary()
        self.assertEqual(4, len(summary))
        self.assertEqual(1, summary["Gardens"])
        self.assertEqual(7, summary["Copper"])
        self.assertEqual(3, summary["Estate"])
        self.assertEqual(4, summary["VICTORY POINTS"])


class TestGame(TestCase):
    def setData(self):
        # resets game data
        self.player_names = testUtility.getNames()
        self.nV, self.nC = testUtility.calculate_nVnC(self.player_names)
        self.box = testUtility.makeBox(self.nV)
        self.supply_order = testUtility.createSupplyOrder()
        self.supply = testUtility.createSupply(
            self.box, self.player_names, self.nC, self.nV
        )
        self.players = testUtility.createPlayers(self.player_names)

    def test_gameOver(self):
        # standard case where no conditions are met
        self.setData()
        result = Dominion.gameover(self.supply)
        self.assertEqual(False, result)

        # case where Provinces are empty
        self.supply["Province"] = []
        result = Dominion.gameover(self.supply)
        self.assertEqual(True, result)

        # case where only two supply piles are empty
        self.setData()
        self.supply["Copper"] = []
        self.supply["Estate"] = []
        result = Dominion.gameover(self.supply)
        self.assertEqual(False, result)

        # case where three supply piles are empty
        self.setData()
        self.supply["Copper"] = []
        self.supply["Duchy"] = []
        self.supply["Estate"] = []
        result = Dominion.gameover(self.supply)
        self.assertEqual(True, result)

