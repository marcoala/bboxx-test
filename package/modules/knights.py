KNIGHT_STATUSES = {
    "LIVE": "LIVE",  # this should probably be ALIVE
    "DEAD": "DEAD",
    "DROWNED": "DROWNED",
}

SURPRISE_ELEMENT = 0.5


class KnightIsDeadError(Exception):
    pass


class GameObject:
    def __init__(self, name, y, x):
        self.name = name
        self.x = x
        self.y = y

    @property
    def position(self):
        return self.y, self.x


class Knight(GameObject):
    item = None
    _base_attack = 1
    _base_defence = 1

    def __init__(self, name, y, x):
        super().__init__(name, y, x)
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

    def die(self):
        self.drop_item()
        self.status = KNIGHT_STATUSES["DEAD"]

    def equip_item(self, item):
        self.item = item
        self.item.equipped = True

    def drop_item(self):
        if self.item:
            self.item.equipped = False
            self.item = None


class GameItem(GameObject):
    equipped = False

    def __init__(self, name, y, x, attack=0, defence=0):
        super().__init__(name, y, x)
        self.attack = attack
        self.defence = defence


def fight(attacker, defender):
    if attacker.attack + SURPRISE_ELEMENT > defender.defence:
        defender.die()
    if attacker.attack + SURPRISE_ELEMENT < defender.defence:
        attacker.die()
