from unittest import TestCase, main

from BattleShip.GameBoard import GameBoard


class TestGameboard(TestCase):

    def test_position_off_the_grid(self):
        game = GameBoard(10)
        game.add_ship([0, 0], "N")

        self.assertRaises(ValueError, game.add_ship, [0, -1], "N")
        self.assertRaises(ValueError, game.add_ship, [0, 0], "9")

    def test_direction_valid(self):
        game = GameBoard(10)
        game.add_ship([0, 0], "N")
        self.assertRaises(ValueError, game.add_ship, [0, 0], "9")

    def test_position_and_direction_valid(self):
        game = GameBoard(10)
        game.position_and_direction_valid([9, 9], "S")

    def test_final_position_from_move(self):
        game = GameBoard(10)
        self.assertEqual(game.final_position_from_move([0, 0], "N", "MMMRMMM"), (3, 3, 'E'))
        self.assertEqual(game.final_position_from_move([3, 3], "E", "RMMMRMMM"), (0, 0, 'W'))
        self.assertEqual(game.final_position_from_move([1, 1], "N", "MMMRMMM"), (4, 4, 'E'))

    def test_new_direction(self):
        game = GameBoard(10)
        self.assertEqual(game.new_direction("N", "right"), "E")

    def test_add_ship(self):
        game = GameBoard(10)
        game.add_ship([0, 0], "N")

        self.assertRaises(ValueError, game.add_ship, [0, -1], "N")
        self.assertRaises(ValueError, game.add_ship, [0, 0], "9")

    def test_move_ship_at_position(self):
        game = GameBoard(4)
        game.add_ship([0, 0], "N")
        game.move_ship_at_position([0, 0], "MMMRMMM")

        self.assertEqual(game.ship_record[0].position, [3, 3])
        self.assertEqual(game.ship_record[0].direction, "E")

        game.add_ship([0, 0], "N")
        self.assertRaises(ValueError, game.move_ship_at_position, [0, 0], "MMMRMMM")


    def test_sink_ship_at_position(self):
        game = GameBoard(10)
        game.add_ship([0, 0], "N")
        game.sink_ship_at_position([0, 0])

        self.assertEqual(game.ship_record[0].position, [0, 0])
        self.assertEqual(game.ship_record[0].direction, "N")
        self.assertEqual(game.ship_record[0].is_alive, False)

        game.add_ship([1, 1], "S")


if __name__ == '__main__':
    main()
