class Knight:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'N':
            self.y = self.y - 1
        elif direction == 'S':
            self.y = self.y + 1
        elif direction == 'E':
            self.x = self.x + 1
        elif direction == 'W':
            self.x = self.x - 1
