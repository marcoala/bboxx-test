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


def test_Game_drown_scenario_1():
    """
    Scenario:
    Red pick up the Axe then drown

    Expected results:
    Red is DROWNED, the position is null
    Axe position is the last valide Red position
    Everthing else is the same
    """
    game = Game()
    game.execute_move('R:S')
    game.execute_move('R:S')
    game.execute_move('R:E')
    game.execute_move('R:E')
    game.execute_move('R:E')
    game.execute_move('R:W')
    game.execute_move('R:W')
    game.execute_move('R:W')
    game.execute_move('R:W')
    assert game.get_result() == {
        "axe": [[(2, 0)], False],
        "blue": [[(7, 0)], "LIVE", "null", 1, 1],
        "dagger": [[(2, 5)], False],
        "green": [[(7, 7)], "LIVE", "null", 1, 1],
        "helmet": [[(5, 5)], False],
        "magic_staff": [[(5, 2)], False],
        "red": ["null", "DROWNED", "null", 1, 1],
        "yellow": [[(0, 7)], "LIVE", "null", 1, 1],
    }


def test_Game_drown_scenario_2():
    """
    Scenario:
    Red pick up the Axe then attack Blue

    Expected results:
    Red is in a new position, with the Axe equipped
    Blue is dead
    """
    game = Game()
    game.execute_move('R:S')
    game.execute_move('R:S')
    game.execute_move('R:E')
    game.execute_move('R:E')
    game.execute_move('R:E')
    game.execute_move('R:W')
    game.execute_move('R:W')
    game.execute_move('R:W')
    game.execute_move('R:S')
    game.execute_move('R:S')
    game.execute_move('R:S')
    game.execute_move('R:S')
    game.execute_move('R:S')
    assert game.get_result() == {
        "axe": [[(7, 0)], True],
        "blue": [[(7, 0)], "DEAD", "null", 1, 1],
        "dagger": [[(2, 5)], False],
        "green": [[(7, 7)], "LIVE", "null", 1, 1],
        "helmet": [[(5, 5)], False],
        "magic_staff": [[(5, 2)], False],
        "red": [[(7, 0)], "LIVE", "A", 3, 1],
        "yellow": [[(0, 7)], "LIVE", "null", 1, 1],
    }


def test_Game_drown_scenario_3():
    """
    Scenario:
    Red pick up the Axe, Yellow pick up the Dagger, Red attacks Yellow

    Expected results:
    Yellow is dead, The Dagger is a new position, Red is anew position, the Axe
    is a new position
    """
    game = Game()
    game.execute_move('R:S')
    game.execute_move('R:S')
    game.execute_move('R:E')
    game.execute_move('R:E')
    game.execute_move('R:E')

    game.execute_move('Y:S')
    game.execute_move('Y:S')
    game.execute_move('Y:W')
    game.execute_move('Y:W')

    game.execute_move('R:E')
    game.execute_move('R:E')

    assert game.get_result() == {
        "axe": [[(2, 5)], True],
        "blue": [[(7, 0)], "LIVE", "null", 1, 1],
        "dagger": [[(2, 5)], False],
        "green": [[(7, 7)], "LIVE", "null", 1, 1],
        "helmet": [[(5, 5)], False],
        "magic_staff": [[(5, 2)], False],
        "red": [[(2, 5)], "LIVE", "A", 3, 1],
        "yellow": [[(2, 5)], "DEAD", "null", 1, 1],
    }
