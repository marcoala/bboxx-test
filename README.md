# bbox-test

Builid the Docker image.

```bash
docker-compose build
```

Run the main script

```bash
docker-compose run --rm python python scripts/main.py
```

|Run the tests

```bash
docker-compose run --rm python python -m pytest -v
```
