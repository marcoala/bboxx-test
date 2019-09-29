KNIGHT_STATUSES = {
    "LIVE": "LIVE",
    "DEAD": "DEAD",
    "DROWNED": "DROWNED",
}


class KnightIsDeadError(Exception):
    pass


class GameObject:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class Knight(GameObject):
    item = None
    _base_attack = 1
    _base_defence = 1

    def __init__(self, name, x, y):
        super().__init__(name, x, y)
        self.status = KNIGHT_STATUSES["LIVE"]

    def move(self, direction):
        if self.status != KNIGHT_STATUSES["LIVE"]:
            raise KnightIsDeadError
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

    @property
    def attack(self):
        if self.item:
            return self._base_attack + self.item.attack
        return self._base_attack

    @property
    def defence(self):
        if self.item:
            return self._base_defence + self.item.defence
        return self._base_defence


class GameItem(GameObject):
    def __init__(self, name, x, y, attack=0, defence=0):
        super().__init__(name, x, y)
        self.attack = attack
        self.defence = defence
