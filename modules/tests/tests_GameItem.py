from modules.items import GameItem


def test_test_GameItem_creation():
    item = GameItem('M', 5, 2, 1, 1)
    assert item.name == 'M'
    assert item.x == 5
    assert item.y == 2
    assert item.attack == 1
    assert item.defence == 1
