from package.modules.knights import Knight, GameItem


class Game:
    def __init__(self):
        self.knights = {
            'R': Knight('R', 0, 0),
            'B': Knight('B', 7, 0),
            'Y': Knight('Y', 0, 7),
            'G': Knight('G', 7, 7),
        }
        self.items = {
            'A': GameItem('A', 2, 2, 2, 0),
            'D': GameItem('D', 2, 5, 1, 0),
            'M': GameItem('M', 5, 2, 1, 1),
            'H': GameItem('H', 5, 5, 0, 1),
        }

    def _knight_status(self, code):
        knight = self.knights[code]
        return [
            [knight.position],
            knight.status,
            knight.item or 'null',
            knight.attack,
            knight.defence
        ]

    def _item_status(self, code):
        item = self.items[code]
        return [
            [item.position],
            item.equipped,
        ]

    def get_result(self):
        return {
            "red": self._knight_status('R'),
            "blue": self._knight_status('B'),
            "green": self._knight_status('G'),
            "yellow": self._knight_status('Y'),
            "magic_staff": self._item_status('M'),
            "helmet": self._item_status('H'),
            "dagger": self._item_status('D'),
            "axe": self._item_status('A'),
        }
