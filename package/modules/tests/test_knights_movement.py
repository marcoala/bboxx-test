import pytest

from package.modules.knights import Knight, KNIGHT_STATUSES, KnightIsDeadError


def test_Knight_creation():
    knight = Knight('A', 3, 4)
    assert knight.name == 'A'
    assert knight.x == 4
    assert knight.y == 3


@pytest.mark.parametrize(
    'direction,expected_y,expected_x',
    [
        ('N', 2, 4),
        ('S', 4, 4),
        ('E', 3, 5),
        ('W', 3, 3),
    ],
)
def test_Knight_move(direction, expected_y, expected_x):
    knight = Knight('A', 3, 4)
    knight.move(direction)
    assert knight.x == expected_x
    assert knight.y == expected_y


def test_Knight_drowning():
    knight = Knight('A', 3, 4)
    for _ in range(4):
        knight.move('N')
    assert knight.status == KNIGHT_STATUSES["DROWNED"], (knight.x, knight.y)


def test_Knight_move_only_if_alive():
    knight = Knight('A', 3, 4)
    for _ in range(4):
        knight.move('N')
    assert knight.status == KNIGHT_STATUSES["DROWNED"], (knight.x, knight.y)

    with pytest.raises(KnightIsDeadError):
        knight.move('N')
