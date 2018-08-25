"""
Gameboard class

"""
from .Ship import Ship


class GameBoard:
    """
        Used to manage ship positions and interactions, the size
    """

    VALID_DIRECTIONS = ["N", "W", "S", "E"]
    NUM_DIRECTIONS = 4

    def __init__(self, board_size):

        if board_size < 1:
            raise ValueError("Size must be at least 1x1")

        self.size = board_size
        self.grid = [[None for i in range(board_size)] for j in range(board_size)]  # generate grid of None objects
        self.ship_record = []

    # Helper functions for ship actions

    def position_on_grid(self, position: list):
        """
        If position is within the grid
        :param position:
        :return bool:
        """
        x, y = position
        return (0 <= x < self.size) and (0 <= y < self.size)

    def direction_valid(self, direction: str):
        """
        :param direction:
        :return bool:
        """
        return direction in self.VALID_DIRECTIONS

    def position_and_direction_valid(self, position: list, direction: str):
        """
        :param position:
        :param direction:
        :return bool:
        """
        return self.position_on_grid(position) and self.direction_valid(direction)

    def final_position_from_move(self, position: list, direction: str, movement_sequence: str):
        """
        :param position:
        :param direction:
        :param movement_sequence:
        :return new_x (int), new_y (int), direction (str):
        """

        orientation_to_y = {"N": 1, "S": -1}
        orientation_to_x = {"W": -1, "E": 1}

        # could have made this just one dictionary with list entries, but then would of needed a position
        # class with a specific 'add' function that adds the values (like in numpy arrays)
        new_x, new_y = position

        for move in movement_sequence:
            if move is "M":
                if direction is "N" or direction is "S":
                    new_y += orientation_to_y[direction]
                else:
                    new_x += orientation_to_x[direction]

            if move is "L":
                direction = self.new_direction(direction, "left")

            if move is "R":
                direction = self.new_direction(direction, "right")

        return new_x, new_y, direction

    def new_direction(self, initial_direction: str, way_to_turn: str):
        """
        Given a which way to turn and an initial direction, return the new direction
        :param initial_direction:
        :param way_to_turn:
        :return new_direction (str):
        """

        current_direction_index = self.VALID_DIRECTIONS.index(initial_direction)

        if way_to_turn is "right":
            new_direction_index = (current_direction_index - 1) % self.NUM_DIRECTIONS
        elif way_to_turn is "left":
            new_direction_index = (current_direction_index + 1) % self.NUM_DIRECTIONS
        else:
            raise ValueError("turn direction passed is not valid")

        new_direction = self.VALID_DIRECTIONS[new_direction_index]

        return new_direction

    def add_ship(self, position: list, direction: str):
        """
        :param position:
        :param direction:
        """

        x, y = position
        ship_at_position = self.grid[x][y]

        if ship_at_position:
            raise ValueError("spot taken!")

        if self.position_and_direction_valid(position, direction):
            new_ship = Ship(position, direction)
            self.grid[x][y] = new_ship
            self.ship_record.append(new_ship)

        else:
            raise ValueError("{} position and {} direction not valid".format(position, direction))

    def move_ship_at_position(self, position: list, movement: str):
        """
        Given the position and movement sequence, move the ship.
        :param position:
        :param movement:
        :return:

        Function logic is as follows:
        1. Check if the ship being moved exists, if true..
        2. Check that the final position is still on the board, if true..
        4. Check the final position is free, if true..
        3. Move the ship to that position
        """

        x_start, y_start = position
        ship_to_move = self.grid[x_start][y_start]
        if ship_to_move is None:
            raise ValueError("ship at {} does not exist".format(position))

        initial_direction = ship_to_move.direction
        x_end, y_end, final_direction = self.final_position_from_move([x_start, y_start], initial_direction, movement)

        if self.position_on_grid([x_end, y_end]) is False:
            raise ValueError("final position {} from the movement is invalid".format([x_end, y_end]))

        ship_at_desired_position = self.grid[x_end][y_end]
        if ship_at_desired_position:
            raise ValueError("{} is already taken".format([x_end, y_end]))

        ship_to_move.position = [x_end, y_end]
        ship_to_move.direction = final_direction

        # empty the old cell and populate the new one
        self.grid[x_start][y_start] = None
        self.grid[x_end][y_end] = ship_to_move

    def sink_ship_at_position(self, position: list):
        """
        :param position:
        """
        x, y = position
        ship_to_sink = self.grid[x][y]

        # If the ship exists and is at the position
        if ship_to_sink:
            ship_to_sink.is_alive = False

            # and empty the cell
            self.grid[x][y] = None

        # Else, we missed
