import sys
from pprint import pprint

from modules.moves import is_valid_move
from modules.game import Game

moves_file = sys.argv[1]
print(f"📁 Loading {moves_file}... ")

f = open(moves_file, 'r')
lines = f.read().splitlines()
game = Game()
for line in lines:
    if is_valid_move(line):
        print(f"↗ Move {line}")
        game.execute_move(line)

f.closed
pprint(game.get_result())
