import pytest

from modules.knights import Knight


def test_Knight_creation():
    knight = Knight('A', 3, 4)
    assert knight.name == 'A'
    assert knight.x == 3
    assert knight.y == 4


@pytest.mark.parametrize(
    'direction,expected_x,expected_y',
    [
        ('N', 3, 3),
        ('S', 3, 5),
        ('E', 4, 4),
        ('W', 2, 4),
    ],
)
def test_Knight_move(direction, expected_x, expected_y):
    knight = Knight('A', 3, 4)
    knight.move(direction)
    assert knight.x == expected_x
    assert knight.y == expected_y
