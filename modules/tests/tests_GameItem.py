from modules.items import Knight, GameItem


def test_GameItem_creation():
    item = GameItem('M', 5, 2, 1, 1)
    assert item.name == 'M'
    assert item.x == 5
    assert item.y == 2
    assert item.attack == 1
    assert item.defence == 1


def test_Knight_equip_GameItem():
    item = GameItem('M', 5, 2, 1, 1)
    knight = Knight('A', 3, 4)
    knight.item = item
    assert knight.attack == 2
    assert knight.defence == 2

