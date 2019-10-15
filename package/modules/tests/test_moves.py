import pytest

from package.modules.moves import is_valid_move


@pytest.mark.parametrize('direction', ['N', 'S', 'O', 'E'])
@pytest.mark.parametrize('knight', ['R', 'B', 'G', 'Y'])
def test_valid_moves(knight, direction):
    move = f"{knight}:{direction}"
    assert is_valid_move(move)


@pytest.mark.parametrize(
    'move',
    [
        'GAME-START',
        'GAME-END',
        'A:B',
        'A:B:C',
        'example string',
    ]
)
def test_invalid_moves(move):
    assert not is_valid_move(move)
