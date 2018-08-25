from .GameBoard import GameBoard
from .text_parsing_helpers import remove_comments_and_whitespace, parse_initial_states_text_into_args_list, \
    group_list_arguments_by_3, parse_actions_text_into_arg


class Simulation(object):
    """
        Used to simulate the game, it uses a gameboard to keep track of everything
    """

    def __init__(self, input_filename: str, output_filename: str):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def write_output_text(self, game_board: GameBoard):
        """
        :param game_board:
        :return None:
        """
        with open(self.output_filename, 'w') as file:

            for ship in game_board.ship_record:
                x, y = ship.position
                direction = ship.direction
                if ship.is_alive:
                    file.write("({}, {}, {})\n".format(x, y, direction))
                else:
                    file.write("({}, {}, {}) SUNK\n".format(x, y, direction))

    def run_simulation(self):
        """
        Run the simulation for the given input file
        :return None:

        """
        # As to avoid magic numbers
        grid_line = 0
        initial_state_line = 1
        action_line_start = 2

        # get the lines and then remove the comments
        with open(self.input_filename) as f:
            lines = f.readlines()
        f.close()

        lines = [remove_comments_and_whitespace(line) for line in lines]

        grid_size = int(lines[grid_line])
        game_board = GameBoard(grid_size)

        initial_states_text = lines[initial_state_line]
        initial_state_list = parse_initial_states_text_into_args_list(initial_states_text)
        initial_state_list = group_list_arguments_by_3(initial_state_list)

        # add all the ships
        for ship_args in initial_state_list:
            x = int(ship_args[0])
            y = int(ship_args[1])
            direction = ship_args[2]
            game_board.add_ship([x, y], direction)

        # perform running actions
        number_of_args_for_sink_action = 2
        for line in lines[action_line_start::]:
            arg_list = parse_actions_text_into_arg(line)

            if len(arg_list) is number_of_args_for_sink_action:
                x = int(arg_list[0])
                y = int(arg_list[1])
                game_board.sink_ship_at_position([x, y])

            else:  # i.e its a move action
                x = int(arg_list[0])
                y = int(arg_list[1])
                movement_sequence = arg_list[2]
                game_board.move_ship_at_position([x, y], movement_sequence)

        # Output the log and finish
        self.write_output_text(game_board)
