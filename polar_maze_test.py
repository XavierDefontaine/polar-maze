import unittest
from unittest import mock
from unittest.mock import patch, call
import numpy as np
from polar_maze import Game

class MakeGridTest(unittest.TestCase):
  
  def test_check_grid_has_a_single_zero_row(self):
    game = Game()
    expected_result = np.array([0])
    actual_result = game.make_grid(1)
    self.assertEqual(expected_result, actual_result)

  def test_check_grid_has_two_rows(self):
    game = Game()
    expected_result = np.array([[0,0],[0,0]])
    actual_result = game.make_grid(2,2)
    np.testing.assert_array_equal(expected_result, actual_result)

class InitialisePlayerTest(unittest.TestCase):
  def test_player_starts_in_top_left_and_is_represented_by_1(self):
    game = Game()
    grid = np.array([
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
    actual_result = game.initialise_player_location(grid)
    np.testing.assert_array_equal(expected_result, actual_result)

class MovePlayerTest(unittest.TestCase):
 
  def test_player_starts_in_top_left_and_moves_right(self):
    game = Game()
    grid = np.array([
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
    actual_result = game.move_player(grid, 'R')
    np.testing.assert_array_equal(expected_result, actual_result)

  def test_player_starts_in_top_left_and_moves_down(self):
    game = Game()
    grid = np.array([
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
    actual_result = game.move_player(grid, 'D')
    np.testing.assert_array_equal(expected_result, actual_result)

  def test_player_can_move_up(self):
    game = Game()
    grid = np.array([
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
    actual_result = game.move_player(grid, 'U')
    np.testing.assert_array_equal(expected_result, actual_result)

  def test_player_can_move_left(self):
    game = Game()
    grid = np.array([
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
    actual_result = game.move_player(grid, 'L')
    np.testing.assert_array_equal(expected_result, actual_result)

class InitialiseFinishLineTest(unittest.TestCase):
  def test_finish_line_is_initialised_at_bottom_right_as_default_and_represented_by_2(self):
    game = Game()
    grid = np.array([
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
    actual_result = game.initialise_finish_line(grid)
    np.testing.assert_array_equal(expected_result, actual_result)

  def test_finish_line_does_not_have_to_be_bottom_right_if_other_coordinates_are_entered(self):
    game = Game()
    grid = np.array([
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
    actual_result = game.initialise_finish_line(grid, row, column)
    np.testing.assert_array_equal(expected_result, actual_result)

  @patch('builtins.print', return_value = "You won")
  def test_player_wins_if_crossing_finish_line(self, mock_print):
    game = Game()
    grid = np.array([
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 1, 2],
    ])
    game.move_player(grid, "R")
    expected_result = call("You won")
    self.assertEqual(expected_result, mock_print.call_args_list[0])

  @patch('builtins.input', return_value)
  def test_get_grid_dimentions_if_square(self):
    






if __name__ == '__main__':
  unittest.main(verbosity = 2)
