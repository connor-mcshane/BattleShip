"""

Ship class

"""


class Ship:

    """
        Used to generate ship objects for the game
    """

    def __init__(self, start_position, start_direction):
        self._position = start_position
        self._direction = start_direction
        self._is_alive = True

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, state):
        self._is_alive = state





