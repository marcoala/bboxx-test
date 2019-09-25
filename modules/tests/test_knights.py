from modules.knights import Knight


def test_Knight_creation():
    knight = Knight('A', 3, 4)
    assert knight.name == 'A'
    assert knight.x == 3
    assert knight.y == 4
