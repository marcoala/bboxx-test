# BBOXX-test

## Run the script

The solution of this test is based on Docker, to build the image run

```bash
docker-compose build
```

To runt the script you will need an input file with the moves, place it into the folder `data`, an example is provided in `data/example_moves.txt`. You don't need to rebuild the Docker image since `data` is mounted as a volume.

The main script is located in `package/main.py` and can be run using the following command, specify the name of the file with the moves.

```bash
docker-compose run --rm python python package/main.py data/example_moves.txt
```

## Tests 

This implementation uses pytest for testing, you can run all the test with the following command.

```bash
docker-compose run --rm python python -m pytest -v
```

## Solution

This solution uses 3 main objects, Knight that manages the Knight properties and actions, Item that manages the Item properties. And last Game that orchestrates a game.

Knight and Items are located in `package/modules/knights.py`, Game is in `package/modules/game.py`.

There a couple of orphans functions that could be moved inside the game object, or - if the project is meant to scale - to a specific support library.

The script in `package/main.py` reads the moves from a file and then return the result in the standard output.

## Test Strategy

This solution uses a series of unit test to check specific functions and end to end test to check the entire game.

While the unit tests allow to easily debug smaller function and to check for regression while debugging the end to end check that the final game works.

the 3 end to end test are in `package/modules/tests/test_game.py`, and are named `test_Game_drown_scenario_1`, `test_Game_drown_scenario_2`, and `test_Game_drown_scenario_3`.

### Scenario 1
Red pick up the Axe then drown

Expected results:
Red is DROWNED, the position is null
Axe position is the last valid Red position

### Scenario 2
Red pick up the Axe then attack Blue

Expected results:
Red is in a new position, with the Axe equipped
Blue is dead

### Scenario 3
Red pick up the Axe, Yellow pick up the Dagger, Red attacks Yellow

Expected results:
Yellow is dead, The Dagger is a new position, Red is anew position, the Axe
is a new position
