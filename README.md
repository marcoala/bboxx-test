# bbox-test

Builid the Docker image.

```bash
docker-compose build
```

Run the main script

```bash
docker-compose run --rm python python package/main.py

# to specify an input file
docker-compose run --rm python python package/main.py data/example_moves.txt
```

Run the tests

```bash
docker-compose run --rm python python -m pytest -v
```
