KNIGHT_STATUSES = {
    "LIVE": "LIVE",
    "DEAD": "DEAD",
    "DROWNED": "DROWNED",
}


class Knight:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.status = KNIGHT_STATUSES["LIVE"]

    def move(self, direction):
        if direction == 'N':
            self.y = self.y - 1
        elif direction == 'S':
            self.y = self.y + 1
        elif direction == 'E':
            self.x = self.x + 1
        elif direction == 'W':
            self.x = self.x - 1
        self._check_drowing()

    def _check_drowing(self):
        if self.x < 0 or self.x > 7 or self.y < 0 or self.y > 7:
            self.status = KNIGHT_STATUSES["DROWNED"]
