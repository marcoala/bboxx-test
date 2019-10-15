import sys
from modules.moves import is_valid_move

moves_file = sys.argv[1]
print(f"📁 Loading {moves_file}... ")

f = open(moves_file, 'r')
lines = f.read().splitlines()
for line in lines:
    if is_valid_move(line):
        print(f"↗ Move {line}")


f.closed
