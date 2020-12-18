import unittest
from unittest import mock
from unittest.mock import patch, call
import numpy as np
from polar_maze import Game

class MakeGridTest(unittest.TestCase):
  @patch('polar_maze.Game.__init__', return_value = None)
  def test_check_grid_has_a_single_zero_row(self, mock_Game_init):
    game = Game()
    expected_result = np.array([0])
    actual_result = game.make_grid(1)
    self.assertEqual(expected_result, actual_result)

  @patch('polar_maze.Game.__init__', return_value = None)
  def test_check_grid_has_two_rows(self, mock_Game_init):
    game = Game()
    expected_result = np.array([[0,0],[0,0]])
    actual_result = game.make_grid(2,2)
    np.testing.assert_array_equal(expected_result, actual_result)

class InitialisePlayerTest(unittest.TestCase):
  @patch('polar_maze.Game.__init__', return_value = None)
  def test_player_starts_in_top_left_and_is_represented_by_1(self, mock_Game_init):
    game = Game()
    game.grid = np.array([
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    expected_result = np.array([
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    game.initialise_player_location()
    np.testing.assert_array_equal(expected_result, game.grid)

class MovePlayerTest(unittest.TestCase):
  @patch('polar_maze.Game.__init__', return_value = None)
  def test_player_starts_in_top_left_and_moves_right(self, mock_Game_init):
    game = Game()
    game.grid = np.array([
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])

    expected_result = np.array([
      [0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    game.move_player('R')
    np.testing.assert_array_equal(expected_result, game.grid)

  @patch('polar_maze.Game.__init__', return_value = None)
  def test_player_starts_in_top_left_and_moves_down(self, mock_Game_init):
    game = Game()
    game.grid = np.array([
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])

    expected_result = np.array([
      [0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    game.move_player('D')
    np.testing.assert_array_equal(expected_result, game.grid)

  @patch('polar_maze.Game.__init__', return_value = None)
  def test_player_can_move_up(self, mock_Game_init):
    game = Game()
    game.grid = np.array([
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])

    expected_result = np.array([
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    game.move_player('U')
    np.testing.assert_array_equal(expected_result, game.grid)

  @patch('polar_maze.Game.__init__', return_value = None)
  def test_player_can_move_left(self, mock_Game_init):
    game = Game()
    game.grid = np.array([
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])

    expected_result = np.array([
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    game.move_player('L')
    np.testing.assert_array_equal(expected_result, game.grid)

class InitialiseFinishLineTest(unittest.TestCase):
  @patch('polar_maze.Game.__init__', return_value = None)
  @patch('builtins.input')
  def test_finish_line_is_initialised_at_bottom_right_as_default_and_represented_by_2(
    self, mock_input, mock_Game_init
  ):
    game = Game()
    game.grid = np.array([
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    expected_result = np.array([
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 2],
    ])
    game.initialise_finish_line()
    np.testing.assert_array_equal(expected_result, game.grid)

  @patch('polar_maze.Game.__init__', return_value = None)
  @patch('builtins.input')
  def test_finish_line_does_not_have_to_be_bottom_right_if_other_coordinates_are_entered(
    self, mock_input, mock_Game_init
  ):
    game = Game()
    game.grid = np.array([
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    row = 2
    column = 3
    expected_result = np.array([
      [1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 2, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ])
    game.initialise_finish_line(row, column)
    np.testing.assert_array_equal(expected_result, game.grid)

  @patch('polar_maze.Game.__init__', return_value = None)
  @patch('builtins.input')
  @patch('builtins.print', return_value = "You won")
  def test_player_wins_if_crossing_finish_line(self, mock_print, mock_input, mock_Game_init):
    game = Game()
    game.grid = np.array([
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 1, 2],
    ])
    game.move_player("R")
    expected_result = call("You won")
    self.assertEqual(expected_result, mock_print.call_args_list[0])

class GetGridDimentionsTest(unittest.TestCase):
  @patch('builtins.input', side_effect = ["square", "5"])
  def test_get_grid_dimensions_returns_number_and_None_if_square(self, mock_input):
    expected_result = (5, None)
    actual_result = Game.get_grid_dimensions(self)

    self.assertEqual(actual_result, expected_result)
    self.assertEqual(mock_input.call_count, 2)
    self.assertEqual(mock_input.call_args_list[0], call("Do you want a square or rectangle?"))
    self.assertEqual(mock_input.call_args_list[1], call("What size of square?"))

  @patch('builtins.input', side_effect = ["rectangle", "4", "6"])
  def test_get_grid_dimensions_returns_two_numbers_if_rectangle(self, mock_input):
    expected_result = (4, 6)
    actual_result = Game.get_grid_dimensions(self)

    self.assertEqual(actual_result, expected_result)
    self.assertEqual(mock_input.call_count, 3)
    self.assertEqual(mock_input.call_args_list[0], call("Do you want a square or rectangle?"))
    self.assertEqual(mock_input.call_args_list[1], call("How many rows in the rectangle?"))
    self.assertEqual(mock_input.call_args_list[2], call("How many columns in the rectangle?"))

class GetPlayerMoveChoiceTest(unittest.TestCase):
  @patch('builtins.input', side_effect = ["square", 5, "L"])
  def test_get_player_move_choice_returns_L_for_input_L(self, mock_input):
    game = Game()

    expected_result = "L"
    actual_result = game.get_player_move_choice()

    self.assertEqual(actual_result, expected_result)
    self.assertGreaterEqual(mock_input.call_count, 1)
    self.assertEqual(mock_input.call_args_list[2], call("What direction do you want to move?\nType U D L or R\n"))
  
  @patch('builtins.input', side_effect = ["square", 5, "D"])
  def test_get_player_move_choice_returns_D_for_input_D(self, mock_input):
    game = Game()

    expected_result = "D"
    actual_result = game.get_player_move_choice()

    self.assertEqual(actual_result, expected_result)
    self.assertGreaterEqual(mock_input.call_count, 1)
    self.assertEqual(mock_input.call_args_list[2], call("What direction do you want to move?\nType U D L or R\n"))

## TO DO:

# class PrintGridTest(unittest.TestCase):
#   @patch('polar_maze.Game.__init__', return_value = None)
#   @patch('builtins.print', return_value = """[[1 0 0 0 0]
#       [0 0 0 0 0]]""")
#   def test_print_grid(self, mock_print, mock_init):
#     game = Game()
#     game.grid = np.array([
#       [1, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0],
#     ])
#     expected_result = call("""[[1 0 0 0 0]
#       [0 0 0 0 0]]""")
#     game.print_grid()
#     self.assertEqual(expected_result, mock_print.call_args_list[0])

if __name__ == '__main__':
  unittest.main(verbosity = 2)
