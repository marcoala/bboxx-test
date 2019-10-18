from package.modules.game import Game


def test_Game_creation_and_result():
    game = Game()
    assert game.get_result() == {
        "axe": [[(2, 2)], False],
        "blue": [[(7, 0)], "LIVE", "null", 1, 1],
        "dagger": [[(2, 5)], False],
        "green": [[(7, 7)], "LIVE", "null", 1, 1],
        "helmet": [[(5, 5)], False],
        "magic_staff": [[(5, 2)], False],
        "red": [[(0, 0)], "LIVE", "null", 1, 1],
        "yellow": [[(0, 7)], "LIVE", "null", 1, 1],
    }


def test_Game_drown_kingt():
    game = Game()
    game.execute_move('R:N')
    game.execute_move('Y:N')
    game.execute_move('G:S')
    game.execute_move('B:S')
    assert game.get_result() == {
        "axe": [[(2, 2)], False],
        "blue": ['null', "DROWNED", "null", 1, 1],
        "dagger": [[(2, 5)], False],
        "green": ['null', "DROWNED", "null", 1, 1],
        "helmet": [[(5, 5)], False],
        "magic_staff": [[(5, 2)], False],
        "red": ['null', "DROWNED", "null", 1, 1],
        "yellow": ['null', "DROWNED", "null", 1, 1],
    }
