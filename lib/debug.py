#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

# self, player, game, score

sarah = Player('sarah')
val = Player('val')
tetris = Game('tetris')
pokemon = Game('pokemon')
sresults = Result(sarah, tetris, 5000)

ipdb.set_trace()
