from package.modules.knights import KNIGHT_STATUSES, Knight, GameItem, fight


def test_GameItem_creation():
    item = GameItem('M', 5, 2, 1, 1)
    assert item.name == 'M'
    assert item.x == 5
    assert item.y == 2
    assert item.attack == 1
    assert item.defence == 1


def test_Knight_attack_and_defence():
    knight = Knight('A', 3, 4)
    assert knight.attack == 1
    assert knight.defence == 1


def test_Knight_equip_GameItem():
    item = GameItem('M', 5, 2, 1, 1)
    knight = Knight('A', 3, 4)
    knight.item = item
    assert knight.attack == 2
    assert knight.defence == 2


def test_fight_attacker_advantage():
    red = Knight('A', 3, 4)
    blue = Knight('B', 2, 4)
    fight(red, blue)
    assert red.status == KNIGHT_STATUSES["LIVE"]
    assert blue.status == KNIGHT_STATUSES["DEAD"]
