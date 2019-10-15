def is_valid_move(move):
    chunks = move.split(':')
    if len(chunks) != 2:
        return False
    is_valid_knight = chunks[0] in ['R', 'B', 'G', 'Y']
    is_valid_direction = chunks[1] in ['N', 'S', 'O', 'E']
    return is_valid_knight and is_valid_direction
